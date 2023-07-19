// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package analytics

import (
	"encoding/json"
	"fmt"
)

// GetUsersCountResponse struct for GetUsersCountResponse
type GetUsersCountResponse struct {
	// Number of occurrences.
	Count int32 `json:"count" validate:"required"`
	// User count.
	Dates []UserWithDate `json:"dates" validate:"required"`
}

// NewGetUsersCountResponse instantiates a new GetUsersCountResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewGetUsersCountResponse(count int32, dates []UserWithDate) *GetUsersCountResponse {
	this := &GetUsersCountResponse{}
	this.Count = count
	this.Dates = dates
	return this
}

// NewGetUsersCountResponseWithDefaults instantiates a new GetUsersCountResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewGetUsersCountResponseWithDefaults() *GetUsersCountResponse {
	this := &GetUsersCountResponse{}
	return this
}

// GetCount returns the Count field value
func (o *GetUsersCountResponse) GetCount() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.Count
}

// GetCountOk returns a tuple with the Count field value
// and a boolean to check if the value has been set.
func (o *GetUsersCountResponse) GetCountOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Count, true
}

// SetCount sets field value
func (o *GetUsersCountResponse) SetCount(v int32) {
	o.Count = v
}

// GetDates returns the Dates field value
func (o *GetUsersCountResponse) GetDates() []UserWithDate {
	if o == nil {
		var ret []UserWithDate
		return ret
	}

	return o.Dates
}

// GetDatesOk returns a tuple with the Dates field value
// and a boolean to check if the value has been set.
func (o *GetUsersCountResponse) GetDatesOk() ([]UserWithDate, bool) {
	if o == nil {
		return nil, false
	}
	return o.Dates, true
}

// SetDates sets field value
func (o *GetUsersCountResponse) SetDates(v []UserWithDate) {
	o.Dates = v
}

func (o GetUsersCountResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if true {
		toSerialize["count"] = o.Count
	}
	if true {
		toSerialize["dates"] = o.Dates
	}
	return json.Marshal(toSerialize)
}

func (o GetUsersCountResponse) String() string {
	out := ""
	out += fmt.Sprintf("  count=%v\n", o.Count)
	out += fmt.Sprintf("  dates=%v\n", o.Dates)
	return fmt.Sprintf("GetUsersCountResponse {\n%s}", out)
}

type NullableGetUsersCountResponse struct {
	value *GetUsersCountResponse
	isSet bool
}

func (v NullableGetUsersCountResponse) Get() *GetUsersCountResponse {
	return v.value
}

func (v *NullableGetUsersCountResponse) Set(val *GetUsersCountResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableGetUsersCountResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableGetUsersCountResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableGetUsersCountResponse(val *GetUsersCountResponse) *NullableGetUsersCountResponse {
	return &NullableGetUsersCountResponse{value: val, isSet: true}
}

func (v NullableGetUsersCountResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableGetUsersCountResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
