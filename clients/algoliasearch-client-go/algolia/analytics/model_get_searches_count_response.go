// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package analytics

import (
	"encoding/json"
	"fmt"
)

// GetSearchesCountResponse struct for GetSearchesCountResponse
type GetSearchesCountResponse struct {
	// Number of occurrences.
	Count int32 `json:"count" validate:"required"`
	// Search events with their associated dates and hit counts.
	Dates []SearchEvent `json:"dates" validate:"required"`
}

// NewGetSearchesCountResponse instantiates a new GetSearchesCountResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewGetSearchesCountResponse(count int32, dates []SearchEvent) *GetSearchesCountResponse {
	this := &GetSearchesCountResponse{}
	this.Count = count
	this.Dates = dates
	return this
}

// NewGetSearchesCountResponseWithDefaults instantiates a new GetSearchesCountResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewGetSearchesCountResponseWithDefaults() *GetSearchesCountResponse {
	this := &GetSearchesCountResponse{}
	return this
}

// GetCount returns the Count field value
func (o *GetSearchesCountResponse) GetCount() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.Count
}

// GetCountOk returns a tuple with the Count field value
// and a boolean to check if the value has been set.
func (o *GetSearchesCountResponse) GetCountOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Count, true
}

// SetCount sets field value
func (o *GetSearchesCountResponse) SetCount(v int32) {
	o.Count = v
}

// GetDates returns the Dates field value
func (o *GetSearchesCountResponse) GetDates() []SearchEvent {
	if o == nil {
		var ret []SearchEvent
		return ret
	}

	return o.Dates
}

// GetDatesOk returns a tuple with the Dates field value
// and a boolean to check if the value has been set.
func (o *GetSearchesCountResponse) GetDatesOk() ([]SearchEvent, bool) {
	if o == nil {
		return nil, false
	}
	return o.Dates, true
}

// SetDates sets field value
func (o *GetSearchesCountResponse) SetDates(v []SearchEvent) {
	o.Dates = v
}

func (o GetSearchesCountResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if true {
		toSerialize["count"] = o.Count
	}
	if true {
		toSerialize["dates"] = o.Dates
	}
	return json.Marshal(toSerialize)
}

func (o GetSearchesCountResponse) String() string {
	out := ""
	out += fmt.Sprintf("  count=%v\n", o.Count)
	out += fmt.Sprintf("  dates=%v\n", o.Dates)
	return fmt.Sprintf("GetSearchesCountResponse {\n%s}", out)
}

type NullableGetSearchesCountResponse struct {
	value *GetSearchesCountResponse
	isSet bool
}

func (v NullableGetSearchesCountResponse) Get() *GetSearchesCountResponse {
	return v.value
}

func (v *NullableGetSearchesCountResponse) Set(val *GetSearchesCountResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableGetSearchesCountResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableGetSearchesCountResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableGetSearchesCountResponse(val *GetSearchesCountResponse) *NullableGetSearchesCountResponse {
	return &NullableGetSearchesCountResponse{value: val, isSet: true}
}

func (v NullableGetSearchesCountResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableGetSearchesCountResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
