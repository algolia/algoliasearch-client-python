package transport

import (
	"net"
	"net/http"
	"time"
)

const (
	DefaultConnectTimeout      = 2 * time.Second
	DefaultKeepAliveDuration   = 5 * time.Minute
	DefaultMaxIdleConnsPerHost = 64
	DefaultTLSHandshakeTimeout = 2 * time.Second
)

// DefaultHTTPClient exposes the default *http.Client used by the different
// Client instances of the Algolia API client.
//
// Most users should not need to access this http.Client.
//
// This helper is only useful for users who wish to keep the default behavior of
// the Algolia API client (by wrapping it in a user-defined instance of
// transport.Requester) but would like to wrap it into a middleware layer or
// pass it to an HTTP interceptor.
func DefaultHTTPClient() *http.Client {
	return &http.Client{
		Transport: defaultTransport,
	}
}

var defaultTransport = &http.Transport{
	DialContext: (&net.Dialer{
		KeepAlive: DefaultKeepAliveDuration,
		Timeout:   DefaultConnectTimeout,
	}).DialContext,
	DisableKeepAlives:   false,
	MaxIdleConnsPerHost: DefaultMaxIdleConnsPerHost,
	Proxy:               http.ProxyFromEnvironment,
	TLSHandshakeTimeout: DefaultTLSHandshakeTimeout,
}

type Requester interface {
	Request(req *http.Request) (*http.Response, error)
}

type defaultRequester struct {
	client *http.Client
}

func newDefaultRequester() *defaultRequester {
	return &defaultRequester{
		client: DefaultHTTPClient(),
	}
}

func (r *defaultRequester) Request(req *http.Request) (*http.Response, error) {
	return r.client.Do(req)
}
