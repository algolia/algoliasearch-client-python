// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package ingestion

import (
	"encoding/json"
	"fmt"
)

// SourceUpdate struct for SourceUpdate
type SourceUpdate struct {
	Name  *string            `json:"name,omitempty"`
	Input *SourceUpdateInput `json:"input,omitempty"`
	// The authentication UUID.
	AuthenticationID *string `json:"authenticationID,omitempty"`
}

type SourceUpdateOption func(f *SourceUpdate)

func WithSourceUpdateName(val string) SourceUpdateOption {
	return func(f *SourceUpdate) {
		f.Name = &val
	}
}

func WithSourceUpdateInput(val SourceUpdateInput) SourceUpdateOption {
	return func(f *SourceUpdate) {
		f.Input = &val
	}
}

func WithSourceUpdateAuthenticationID(val string) SourceUpdateOption {
	return func(f *SourceUpdate) {
		f.AuthenticationID = &val
	}
}

// NewSourceUpdate instantiates a new SourceUpdate object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSourceUpdate(opts ...SourceUpdateOption) *SourceUpdate {
	this := &SourceUpdate{}
	for _, opt := range opts {
		opt(this)
	}
	return this
}

// NewSourceUpdateWithDefaults instantiates a new SourceUpdate object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSourceUpdateWithDefaults() *SourceUpdate {
	this := &SourceUpdate{}
	return this
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *SourceUpdate) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceUpdate) GetNameOk() (*string, bool) {
	if o == nil || o.Name == nil {
		return nil, false
	}
	return o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *SourceUpdate) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *SourceUpdate) SetName(v string) {
	o.Name = &v
}

// GetInput returns the Input field value if set, zero value otherwise.
func (o *SourceUpdate) GetInput() SourceUpdateInput {
	if o == nil || o.Input == nil {
		var ret SourceUpdateInput
		return ret
	}
	return *o.Input
}

// GetInputOk returns a tuple with the Input field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceUpdate) GetInputOk() (*SourceUpdateInput, bool) {
	if o == nil || o.Input == nil {
		return nil, false
	}
	return o.Input, true
}

// HasInput returns a boolean if a field has been set.
func (o *SourceUpdate) HasInput() bool {
	if o != nil && o.Input != nil {
		return true
	}

	return false
}

// SetInput gets a reference to the given SourceUpdateInput and assigns it to the Input field.
func (o *SourceUpdate) SetInput(v SourceUpdateInput) {
	o.Input = &v
}

// GetAuthenticationID returns the AuthenticationID field value if set, zero value otherwise.
func (o *SourceUpdate) GetAuthenticationID() string {
	if o == nil || o.AuthenticationID == nil {
		var ret string
		return ret
	}
	return *o.AuthenticationID
}

// GetAuthenticationIDOk returns a tuple with the AuthenticationID field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceUpdate) GetAuthenticationIDOk() (*string, bool) {
	if o == nil || o.AuthenticationID == nil {
		return nil, false
	}
	return o.AuthenticationID, true
}

// HasAuthenticationID returns a boolean if a field has been set.
func (o *SourceUpdate) HasAuthenticationID() bool {
	if o != nil && o.AuthenticationID != nil {
		return true
	}

	return false
}

// SetAuthenticationID gets a reference to the given string and assigns it to the AuthenticationID field.
func (o *SourceUpdate) SetAuthenticationID(v string) {
	o.AuthenticationID = &v
}

func (o SourceUpdate) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if o.Name != nil {
		toSerialize["name"] = o.Name
	}
	if o.Input != nil {
		toSerialize["input"] = o.Input
	}
	if o.AuthenticationID != nil {
		toSerialize["authenticationID"] = o.AuthenticationID
	}
	return json.Marshal(toSerialize)
}

func (o SourceUpdate) String() string {
	out := "SourceUpdate {\n"
	out += fmt.Sprintf("  name=%v\n", o.Name)
	out += fmt.Sprintf("  input=%v\n", o.Input)
	out += fmt.Sprintf("  authenticationID=%v\n", o.AuthenticationID)
	out += "}"
	return out
}

type NullableSourceUpdate struct {
	value *SourceUpdate
	isSet bool
}

func (v NullableSourceUpdate) Get() *SourceUpdate {
	return v.value
}

func (v *NullableSourceUpdate) Set(val *SourceUpdate) {
	v.value = val
	v.isSet = true
}

func (v NullableSourceUpdate) IsSet() bool {
	return v.isSet
}

func (v *NullableSourceUpdate) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSourceUpdate(val *SourceUpdate) *NullableSourceUpdate {
	return &NullableSourceUpdate{value: val, isSet: true}
}

func (v NullableSourceUpdate) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSourceUpdate) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}