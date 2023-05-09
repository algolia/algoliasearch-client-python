package tests

import (
	"bytes"
	"io"
	"net/http"
	"net/url"
)

type echoRequester struct {
	path   string
	method string
	body   *string
	header http.Header
	query  url.Values
}

func (e *echoRequester) Request(req *http.Request) (*http.Response, error) {
	e.path = req.URL.Path
	e.method = req.Method
	e.header = req.Header
	e.query = req.URL.Query()
	if req.Body != nil {
		body, _ := io.ReadAll(req.Body)
		strBody := string(body)
		e.body = &strBody
	} else {
		e.body = nil
	}

	return &http.Response{
		StatusCode: 200,
		Body:       io.NopCloser(bytes.NewBufferString("")),
	}, nil
}
