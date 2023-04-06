package errs

var ErrNoMoreHostToTry = NewNoMoreHostToTryError()

type NoMoreHostToTryErr struct {
	intermediateNetworkErrors []error
}

func NewNoMoreHostToTryError(errs ...error) *NoMoreHostToTryErr {
	return &NoMoreHostToTryErr{
		intermediateNetworkErrors: errs,
	}
}

func (e *NoMoreHostToTryErr) IntermediateNetworkErrors() []error {
	return e.intermediateNetworkErrors
}

func (e *NoMoreHostToTryErr) Error() string {
	return "all hosts have been contacted unsuccessfully, it can either be a server or a network error or wrong appID/key credentials were used. You can use opt.ExposeIntermediateNetworkErrors(true) to investigate."
}
