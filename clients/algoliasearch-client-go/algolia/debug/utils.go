package debug

import (
	"bytes"
	"compress/gzip"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"

	"github.com/algolia/algoliasearch-client-go/v4/algolia/compression"
)

func copyReadCloser(r io.ReadCloser) (io.ReadCloser, string) {
	if r == nil {
		return nil, ""
	}
	data, err := io.ReadAll(r)
	_ = r.Close()
	if err != nil {
		return nil, ""
	}
	return io.NopCloser(bytes.NewReader(data)), string(data)
}

func decodeGzipContent(in string) (string, error) {
	gr, err := gzip.NewReader(strings.NewReader(in))
	if err != nil {
		return in, fmt.Errorf("cannot open content with gzip.Reader: %v", err)
	}
	out, err := io.ReadAll(gr)
	if err != nil {
		return in, fmt.Errorf("cannot read content from gzip.Reader: %v", err)
	}
	return string(out), nil
}

func extractBody(body io.ReadCloser, c compression.Compression) (io.ReadCloser, string) {
	if body == nil {
		return nil, ""
	}

	reader, content := copyReadCloser(body)

	switch c {
	case compression.GZIP:
		decodedContent, err := decodeGzipContent(content)
		if err == nil {
			content = decodedContent
		}
	default:
		// Do nothing
	}

	return reader, content
}

func prettyPrintJSON(input string) string {
	var b bytes.Buffer
	err := json.Indent(&b, []byte(input), "\t", "  ")
	if err != nil {
		return input
	}
	return strings.TrimSuffix(b.String(), "\n")
}

func debugRequest(req *http.Request) string {
	if req == nil {
		return ""
	}

	var body string

	switch req.Header.Get("Content-Encoding") {
	case "gzip":
		req.Body, body = extractBody(req.Body, compression.GZIP)
	default:
		req.Body, body = extractBody(req.Body, compression.None)
	}

	msg := "> ALGOLIA DEBUG request:\n"
	msg += fmt.Sprintf("\tmethod=%q\n", req.Method)
	msg += fmt.Sprintf("\turl=%q\n", req.URL)

	for k, v := range req.Header {
		str := strings.Join(v, ",")
		if strings.Contains(strings.ToLower(k), "algolia") {
			str = strings.Repeat("*", len(str))
		}
		msg += fmt.Sprintf("\theader=%s:%q\n", k, str)
	}
	msg += fmt.Sprintf("\tbody=\n\t%s\n", prettyPrintJSON(body))

	return msg
}

func debugResponse(res *http.Response) string {
	if res == nil {
		return ""
	}

	var body string
	res.Body, body = extractBody(res.Body, compression.None)

	msg := "> ALGOLIA DEBUG response:\n"
	msg += fmt.Sprintf("\tbody=\n\t%s\n", prettyPrintJSON(body))

	return msg
}
