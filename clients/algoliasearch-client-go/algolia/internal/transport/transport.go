package transport

import (
	"context"
	"errors"
	"fmt"
	"net"
	"net/http"
	"time"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/call"
	"github.com/algolia/algoliasearch-client-go/v4/algolia/compression"
	"github.com/algolia/algoliasearch-client-go/v4/algolia/debug"
	"github.com/algolia/algoliasearch-client-go/v4/algolia/internal/errs"
)

type Transport struct {
	requester     Requester
	retryStrategy *RetryStrategy
	compression   compression.Compression
}

func New(
	hosts []*StatefulHost,
	requester Requester,
	readTimeout time.Duration,
	writeTimeout time.Duration,
	compression compression.Compression,
) *Transport {
	if requester == nil {
		requester = newDefaultRequester()
	}

	return &Transport{
		requester:     requester,
		retryStrategy: newRetryStrategy(hosts, readTimeout, writeTimeout),
		compression:   compression,
	}
}

func (t *Transport) Request(ctx context.Context, req *http.Request, k call.Kind) (*http.Response, error) {
	exposeIntermediateNetworkErrors := false // todo: expose this option to the user
	var intermediateNetworkErrors []error

	// Add Content-Encoding header, if needed
	if t.compression == compression.GZIP && shouldCompress(t.compression, req.Method, req.Body) {
		req.Header.Add("Content-Encoding", "gzip")
	}

	for _, h := range t.retryStrategy.GetTryableHosts(k) {
		// Handle per-request timeout by using a context with timeout.
		// Note that because we are in a loop, the cancel() callback cannot be
		// deferred. Instead, we call it precisely after the end of each loop or
		// before the early returns, but when we do so, we do it **after**
		// reading the body content of the response. Otherwise, a `context
		// cancelled` error may happen when the body is read.
		perRequestCtx, cancel := context.WithTimeout(ctx, h.timeout)
		req = req.WithContext(perRequestCtx)
		res, err := t.request(req, h.host)

		code := 0
		if res != nil {
			code = res.StatusCode
		}

		// Context error only returns a non-nil error upon context
		// cancellation, which is a signal we interpret as an early return.
		// Indeed, we do not want to retry on other hosts if the context is
		// already cancelled.
		if ctx.Err() != nil {
			cancel()
			return res, err
		}

		switch t.retryStrategy.Decide(h, code, err) {
		case Success, Failure:
			cancel()
			return res, err
		default:
			if err != nil {
				intermediateNetworkErrors = append(intermediateNetworkErrors, err)
			}
			if res != nil && res.Body != nil {
				if err = res.Body.Close(); err != nil {
					cancel()
					return res, fmt.Errorf("cannot close response's body before retry: %v", err)
				}
			}
		}

		cancel()
	}

	if exposeIntermediateNetworkErrors {
		return nil, errs.NewNoMoreHostToTryError(intermediateNetworkErrors...)
	}

	return nil, errs.ErrNoMoreHostToTry
}

func (t *Transport) request(req *http.Request, host string) (*http.Response, error) {
	req.URL.Scheme = "https"
	req.URL.Host = host

	debug.Display(req)
	res, err := t.requester.Request(req)
	debug.Display(res)

	if err != nil {
		msg := fmt.Sprintf("cannot perform request:\n\terror=%v\n\tmethod=%s\n\turl=%s", err, req.Method, req.URL)
		nerr, ok := err.(net.Error)
		if ok {
			// Because net.Error and error have different meanings for the
			// retry strategy, we cannot simply return a new error, which
			// would make all net.Error simple errors instead. To keep this
			// behaviour, we wrap the message into a custom netError that
			// implements the net.Error interface if the original error was
			// already a net.Error.
			err = errs.NetError(nerr, msg)
		} else {
			err = errors.New(msg)
		}
		return nil, err
	}

	return res, nil
}

func shouldCompress(c compression.Compression, method string, body any) bool {
	isValidMethod := method == http.MethodPut || method == http.MethodPost
	isCompressionEnabled := c != compression.None
	isBodyNonEmpty := body != nil
	return isCompressionEnabled && isValidMethod && isBodyNonEmpty
}
