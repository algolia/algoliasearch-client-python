package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func printResponse(res any) {
	bJson, _ := json.Marshal(res)

	fmt.Printf("response json:   %s\n", string(bJson))
	fmt.Printf("response string: %s\n", res)
}

func getEnvWithDefault(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok && value != "" {
		return value
	}
	return fallback
}
