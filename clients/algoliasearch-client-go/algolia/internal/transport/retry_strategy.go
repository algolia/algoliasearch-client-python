package transport

import (
	"context"
	"net"
	"strings"
	"sync"
	"time"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/call"
)

type Outcome int

const (
	DefaultReadTimeout  = 5 * time.Second
	DefaultWriteTimeout = 30 * time.Second

	Success Outcome = iota
	Failure
	Retry
)

type Host struct {
	host    string
	timeout time.Duration
}

type RetryStrategy struct {
	sync.RWMutex
	hosts        []*StatefulHost
	writeTimeout time.Duration
	readTimeout  time.Duration
}

func newRetryStrategy(hosts []*StatefulHost, readTimeout, writeTimeout time.Duration) *RetryStrategy {
	if readTimeout == 0 {
		readTimeout = DefaultReadTimeout
	}

	if writeTimeout == 0 {
		writeTimeout = DefaultWriteTimeout
	}

	return &RetryStrategy{
		hosts:        hosts,
		readTimeout:  readTimeout,
		writeTimeout: writeTimeout,
	}
}

func (s *RetryStrategy) GetTryableHosts(k call.Kind) (hosts []Host) {
	s.Lock()
	defer s.Unlock()

	for _, h := range s.hosts {
		if h.isExpired() {
			h.reset()
		}
	}

	var baseTimeout time.Duration

	switch k {
	case call.Read:
		baseTimeout = s.readTimeout
	case call.Write:
		baseTimeout = s.writeTimeout
	default:
		baseTimeout = DefaultWriteTimeout
	}

	for _, h := range s.hosts {
		if !h.isDown && h.accept(k) {
			hosts = append(hosts, Host{h.host, time.Duration(h.retryCount+1) * baseTimeout})
		}
	}

	if len(hosts) > 0 {
		return hosts
	}

	for _, h := range s.hosts {
		if h.accept(k) {
			h.reset()
			hosts = append(hosts, Host{h.host, time.Duration(h.retryCount+1) * baseTimeout})
		}
	}

	return hosts
}

func (s *RetryStrategy) Decide(h Host, code int, err error) Outcome {
	s.Lock()
	defer s.Unlock()

	if err == nil && is2xx(code) {
		s.markUp(h)
		return Success
	}

	if isTimeoutError(err) {
		s.markTimeout(h)
		return Retry
	}

	if !(isZero(code) || is4xx(code) || is2xx(code)) || isNetworkError(err) {
		s.markDown(h)
		return Retry
	}

	return Failure
}

func (s *RetryStrategy) markUp(host Host) {
	for _, h := range s.hosts {
		if h.host == host.host {
			h.markUp()
			return
		}
	}
}

func (s *RetryStrategy) markTimeout(host Host) {
	for _, h := range s.hosts {
		if h.host == host.host {
			h.markTimeout()
			return
		}
	}
}

func (s *RetryStrategy) markDown(host Host) {
	for _, h := range s.hosts {
		if h.host == host.host {
			h.markDown()
			return
		}
	}
}

func isNetworkError(err error) bool {
	if err == nil {
		return false
	}
	_, ok := err.(net.Error)
	// We need to ensure that the error is a net.Error but not a
	// context.DeadlineExceeded error (which is actually a net.Error), because
	// we do not want to consider context.DeadlineExceeded as an error.
	return ok && !isTimeoutError(err)
}

func isTimeoutError(err error) bool {
	if err == nil {
		return false
	}
	return strings.Contains(err.Error(), context.DeadlineExceeded.Error())
}

func isZero(code int) bool { return code == 0 }
func is2xx(code int) bool  { return 200 <= code && code < 300 }
func is4xx(code int) bool  { return 400 <= code && code < 500 }
