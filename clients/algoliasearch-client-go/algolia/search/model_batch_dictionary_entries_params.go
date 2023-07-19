// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package search

import (
	"encoding/json"
	"fmt"
)

// BatchDictionaryEntriesParams `batchDictionaryEntries` parameters.
type BatchDictionaryEntriesParams struct {
	// Incidates whether to replace all custom entries in the dictionary with the ones sent with this request.
	ClearExistingDictionaryEntries *bool `json:"clearExistingDictionaryEntries,omitempty"`
	// Operations to batch.
	Requests []BatchDictionaryEntriesRequest `json:"requests" validate:"required"`
}

type BatchDictionaryEntriesParamsOption func(f *BatchDictionaryEntriesParams)

func WithBatchDictionaryEntriesParamsClearExistingDictionaryEntries(val bool) BatchDictionaryEntriesParamsOption {
	return func(f *BatchDictionaryEntriesParams) {
		f.ClearExistingDictionaryEntries = &val
	}
}

// NewBatchDictionaryEntriesParams instantiates a new BatchDictionaryEntriesParams object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBatchDictionaryEntriesParams(requests []BatchDictionaryEntriesRequest, opts ...BatchDictionaryEntriesParamsOption) *BatchDictionaryEntriesParams {
	this := &BatchDictionaryEntriesParams{}
	this.Requests = requests
	for _, opt := range opts {
		opt(this)
	}
	return this
}

// NewBatchDictionaryEntriesParamsWithDefaults instantiates a new BatchDictionaryEntriesParams object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBatchDictionaryEntriesParamsWithDefaults() *BatchDictionaryEntriesParams {
	this := &BatchDictionaryEntriesParams{}
	var clearExistingDictionaryEntries bool = false
	this.ClearExistingDictionaryEntries = &clearExistingDictionaryEntries
	return this
}

// GetClearExistingDictionaryEntries returns the ClearExistingDictionaryEntries field value if set, zero value otherwise.
func (o *BatchDictionaryEntriesParams) GetClearExistingDictionaryEntries() bool {
	if o == nil || o.ClearExistingDictionaryEntries == nil {
		var ret bool
		return ret
	}
	return *o.ClearExistingDictionaryEntries
}

// GetClearExistingDictionaryEntriesOk returns a tuple with the ClearExistingDictionaryEntries field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BatchDictionaryEntriesParams) GetClearExistingDictionaryEntriesOk() (*bool, bool) {
	if o == nil || o.ClearExistingDictionaryEntries == nil {
		return nil, false
	}
	return o.ClearExistingDictionaryEntries, true
}

// HasClearExistingDictionaryEntries returns a boolean if a field has been set.
func (o *BatchDictionaryEntriesParams) HasClearExistingDictionaryEntries() bool {
	if o != nil && o.ClearExistingDictionaryEntries != nil {
		return true
	}

	return false
}

// SetClearExistingDictionaryEntries gets a reference to the given bool and assigns it to the ClearExistingDictionaryEntries field.
func (o *BatchDictionaryEntriesParams) SetClearExistingDictionaryEntries(v bool) {
	o.ClearExistingDictionaryEntries = &v
}

// GetRequests returns the Requests field value
func (o *BatchDictionaryEntriesParams) GetRequests() []BatchDictionaryEntriesRequest {
	if o == nil {
		var ret []BatchDictionaryEntriesRequest
		return ret
	}

	return o.Requests
}

// GetRequestsOk returns a tuple with the Requests field value
// and a boolean to check if the value has been set.
func (o *BatchDictionaryEntriesParams) GetRequestsOk() ([]BatchDictionaryEntriesRequest, bool) {
	if o == nil {
		return nil, false
	}
	return o.Requests, true
}

// SetRequests sets field value
func (o *BatchDictionaryEntriesParams) SetRequests(v []BatchDictionaryEntriesRequest) {
	o.Requests = v
}

func (o BatchDictionaryEntriesParams) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if o.ClearExistingDictionaryEntries != nil {
		toSerialize["clearExistingDictionaryEntries"] = o.ClearExistingDictionaryEntries
	}
	if true {
		toSerialize["requests"] = o.Requests
	}
	return json.Marshal(toSerialize)
}

func (o BatchDictionaryEntriesParams) String() string {
	out := ""
	out += fmt.Sprintf("  clearExistingDictionaryEntries=%v\n", o.ClearExistingDictionaryEntries)
	out += fmt.Sprintf("  requests=%v\n", o.Requests)
	return fmt.Sprintf("BatchDictionaryEntriesParams {\n%s}", out)
}

type NullableBatchDictionaryEntriesParams struct {
	value *BatchDictionaryEntriesParams
	isSet bool
}

func (v NullableBatchDictionaryEntriesParams) Get() *BatchDictionaryEntriesParams {
	return v.value
}

func (v *NullableBatchDictionaryEntriesParams) Set(val *BatchDictionaryEntriesParams) {
	v.value = val
	v.isSet = true
}

func (v NullableBatchDictionaryEntriesParams) IsSet() bool {
	return v.isSet
}

func (v *NullableBatchDictionaryEntriesParams) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBatchDictionaryEntriesParams(val *BatchDictionaryEntriesParams) *NullableBatchDictionaryEntriesParams {
	return &NullableBatchDictionaryEntriesParams{value: val, isSet: true}
}

func (v NullableBatchDictionaryEntriesParams) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBatchDictionaryEntriesParams) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
