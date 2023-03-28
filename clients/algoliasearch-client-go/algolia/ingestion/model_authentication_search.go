// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package ingestion

import (
	"encoding/json"
	"fmt"
)

// AuthenticationSearch Payload to search for multiple authentications, based on the given `authenticationIDs`.
type AuthenticationSearch struct {
	AuthenticationIDs []string `json:"authenticationIDs"`
}

// NewAuthenticationSearch instantiates a new AuthenticationSearch object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewAuthenticationSearch(authenticationIDs []string) *AuthenticationSearch {
	this := &AuthenticationSearch{}
	this.AuthenticationIDs = authenticationIDs
	return this
}

// NewAuthenticationSearchWithDefaults instantiates a new AuthenticationSearch object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewAuthenticationSearchWithDefaults() *AuthenticationSearch {
	this := &AuthenticationSearch{}
	return this
}

// GetAuthenticationIDs returns the AuthenticationIDs field value
func (o *AuthenticationSearch) GetAuthenticationIDs() []string {
	if o == nil {
		var ret []string
		return ret
	}

	return o.AuthenticationIDs
}

// GetAuthenticationIDsOk returns a tuple with the AuthenticationIDs field value
// and a boolean to check if the value has been set.
func (o *AuthenticationSearch) GetAuthenticationIDsOk() ([]string, bool) {
	if o == nil {
		return nil, false
	}
	return o.AuthenticationIDs, true
}

// SetAuthenticationIDs sets field value
func (o *AuthenticationSearch) SetAuthenticationIDs(v []string) {
	o.AuthenticationIDs = v
}

func (o AuthenticationSearch) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if true {
		toSerialize["authenticationIDs"] = o.AuthenticationIDs
	}
	return json.Marshal(toSerialize)
}

func (o AuthenticationSearch) String() string {
	out := "AuthenticationSearch {\n"
	out += fmt.Sprintf("  authenticationIDs=%v\n", o.AuthenticationIDs)
	out += "}"
	return out
}

type NullableAuthenticationSearch struct {
	value *AuthenticationSearch
	isSet bool
}

func (v NullableAuthenticationSearch) Get() *AuthenticationSearch {
	return v.value
}

func (v *NullableAuthenticationSearch) Set(val *AuthenticationSearch) {
	v.value = val
	v.isSet = true
}

func (v NullableAuthenticationSearch) IsSet() bool {
	return v.isSet
}

func (v *NullableAuthenticationSearch) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableAuthenticationSearch(val *AuthenticationSearch) *NullableAuthenticationSearch {
	return &NullableAuthenticationSearch{value: val, isSet: true}
}

func (v NullableAuthenticationSearch) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableAuthenticationSearch) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}