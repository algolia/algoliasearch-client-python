package debug

import (
	"fmt"
	"net/http"
	"time"
)

var debug bool

// Enable enables debug logging. After this call, all Algolia HTTP requests and
// responses will be displayed. A minor overhead is expected when debug logging
// is enabled.
func Enable() {
	debug = true
}

// Disable disables debug logging. After this call, Algolia requests and
// responses will not be logged anymore. The minor overhead introduced when
// debug logging is enabled should not happen anymore.
func Disable() {
	debug = false
}

// Display displays the given parameter on the standard output in a custom way,
// depending on the given input type. This function is internally used by the
// Algolia API client to display, for instance, HTTP requests and responses when
// debug logging is enabled.
func Display(input any) {
	if !debug {
		return
	}
	start := time.Now()
	var msg string
	switch v := input.(type) {
	case *http.Request:
		msg = debugRequest(v)
	case *http.Response:
		msg = debugResponse(v)
	default:
		msg = fmt.Sprintf("do not know how to display %#v", v)
	}
	Println(msg)
	fmt.Printf("took %s\n", time.Since(start))
}

func Println(a ...any) {
	Printf("%s", fmt.Sprintln(a...))
}

func Printf(format string, a ...any) {
	if !debug {
		return
	}
	msg := fmt.Sprintf(format, a...)
	fmt.Printf("> ALGOLIA DEBUG: %s", msg)
}
