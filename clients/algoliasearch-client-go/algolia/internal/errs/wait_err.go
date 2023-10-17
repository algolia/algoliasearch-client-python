package errs

type WaitError struct{}

func (e *WaitError) Error() string {
	return "wait error"
}

type WaitKeyUpdateError struct{}

func (e *WaitKeyUpdateError) Error() string {
	return "`apiKey` is required when waiting for an `update` operation."
}

type WaitKeyOperationError struct{}

func (e *WaitKeyOperationError) Error() string {
	return "`operation` must be one of `add`, `update` or `delete`."
}
