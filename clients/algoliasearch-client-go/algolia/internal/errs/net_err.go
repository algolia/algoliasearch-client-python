package errs

import "net"

type netError struct {
	msg         string
	isTimeout   bool
	isTemporary bool
}

func NetError(err net.Error, msg string) net.Error {
	return &netError{
		msg:         msg,
		isTimeout:   err.Timeout(),
		isTemporary: false,
	}
}

func (e *netError) Error() string   { return e.msg }
func (e *netError) Timeout() bool   { return e.isTimeout }
func (e *netError) Temporary() bool { return e.isTemporary }
