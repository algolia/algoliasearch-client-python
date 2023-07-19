// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package search

import (
	"encoding/json"
	"fmt"
)

// SearchRulesParams Rules search parameters.
type SearchRulesParams struct {
	// Rule object query.
	Query     *string    `json:"query,omitempty"`
	Anchoring *Anchoring `json:"anchoring,omitempty"`
	// Restricts responses to the specified [contextual rule](https://www.algolia.com/doc/guides/managing-results/rules/rules-overview/how-to/customize-search-results-by-platform/#creating-contextual-rules).
	Context *string `json:"context,omitempty"`
	// Requested page (the first page is page 0).
	Page *int32 `json:"page,omitempty"`
	// Maximum number of hits per page.
	HitsPerPage *int32 `json:"hitsPerPage,omitempty"`
	// Restricts responses to enabled rules. When not specified (default), _all_ rules are retrieved.
	Enabled NullableBool `json:"enabled,omitempty"`
	// Request options to send with the API call.
	RequestOptions []map[string]interface{} `json:"requestOptions,omitempty"`
}

type SearchRulesParamsOption func(f *SearchRulesParams)

func WithSearchRulesParamsQuery(val string) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.Query = &val
	}
}

func WithSearchRulesParamsAnchoring(val Anchoring) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.Anchoring = &val
	}
}

func WithSearchRulesParamsContext(val string) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.Context = &val
	}
}

func WithSearchRulesParamsPage(val int32) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.Page = &val
	}
}

func WithSearchRulesParamsHitsPerPage(val int32) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.HitsPerPage = &val
	}
}

func WithSearchRulesParamsEnabled(val NullableBool) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.Enabled = val
	}
}

func WithSearchRulesParamsRequestOptions(val []map[string]interface{}) SearchRulesParamsOption {
	return func(f *SearchRulesParams) {
		f.RequestOptions = val
	}
}

// NewSearchRulesParams instantiates a new SearchRulesParams object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSearchRulesParams(opts ...SearchRulesParamsOption) *SearchRulesParams {
	this := &SearchRulesParams{}
	for _, opt := range opts {
		opt(this)
	}
	return this
}

// NewSearchRulesParamsWithDefaults instantiates a new SearchRulesParams object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSearchRulesParamsWithDefaults() *SearchRulesParams {
	this := &SearchRulesParams{}
	var query string = ""
	this.Query = &query
	var hitsPerPage int32 = 20
	this.HitsPerPage = &hitsPerPage
	return this
}

// GetQuery returns the Query field value if set, zero value otherwise.
func (o *SearchRulesParams) GetQuery() string {
	if o == nil || o.Query == nil {
		var ret string
		return ret
	}
	return *o.Query
}

// GetQueryOk returns a tuple with the Query field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetQueryOk() (*string, bool) {
	if o == nil || o.Query == nil {
		return nil, false
	}
	return o.Query, true
}

// HasQuery returns a boolean if a field has been set.
func (o *SearchRulesParams) HasQuery() bool {
	if o != nil && o.Query != nil {
		return true
	}

	return false
}

// SetQuery gets a reference to the given string and assigns it to the Query field.
func (o *SearchRulesParams) SetQuery(v string) {
	o.Query = &v
}

// GetAnchoring returns the Anchoring field value if set, zero value otherwise.
func (o *SearchRulesParams) GetAnchoring() Anchoring {
	if o == nil || o.Anchoring == nil {
		var ret Anchoring
		return ret
	}
	return *o.Anchoring
}

// GetAnchoringOk returns a tuple with the Anchoring field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetAnchoringOk() (*Anchoring, bool) {
	if o == nil || o.Anchoring == nil {
		return nil, false
	}
	return o.Anchoring, true
}

// HasAnchoring returns a boolean if a field has been set.
func (o *SearchRulesParams) HasAnchoring() bool {
	if o != nil && o.Anchoring != nil {
		return true
	}

	return false
}

// SetAnchoring gets a reference to the given Anchoring and assigns it to the Anchoring field.
func (o *SearchRulesParams) SetAnchoring(v Anchoring) {
	o.Anchoring = &v
}

// GetContext returns the Context field value if set, zero value otherwise.
func (o *SearchRulesParams) GetContext() string {
	if o == nil || o.Context == nil {
		var ret string
		return ret
	}
	return *o.Context
}

// GetContextOk returns a tuple with the Context field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetContextOk() (*string, bool) {
	if o == nil || o.Context == nil {
		return nil, false
	}
	return o.Context, true
}

// HasContext returns a boolean if a field has been set.
func (o *SearchRulesParams) HasContext() bool {
	if o != nil && o.Context != nil {
		return true
	}

	return false
}

// SetContext gets a reference to the given string and assigns it to the Context field.
func (o *SearchRulesParams) SetContext(v string) {
	o.Context = &v
}

// GetPage returns the Page field value if set, zero value otherwise.
func (o *SearchRulesParams) GetPage() int32 {
	if o == nil || o.Page == nil {
		var ret int32
		return ret
	}
	return *o.Page
}

// GetPageOk returns a tuple with the Page field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetPageOk() (*int32, bool) {
	if o == nil || o.Page == nil {
		return nil, false
	}
	return o.Page, true
}

// HasPage returns a boolean if a field has been set.
func (o *SearchRulesParams) HasPage() bool {
	if o != nil && o.Page != nil {
		return true
	}

	return false
}

// SetPage gets a reference to the given int32 and assigns it to the Page field.
func (o *SearchRulesParams) SetPage(v int32) {
	o.Page = &v
}

// GetHitsPerPage returns the HitsPerPage field value if set, zero value otherwise.
func (o *SearchRulesParams) GetHitsPerPage() int32 {
	if o == nil || o.HitsPerPage == nil {
		var ret int32
		return ret
	}
	return *o.HitsPerPage
}

// GetHitsPerPageOk returns a tuple with the HitsPerPage field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetHitsPerPageOk() (*int32, bool) {
	if o == nil || o.HitsPerPage == nil {
		return nil, false
	}
	return o.HitsPerPage, true
}

// HasHitsPerPage returns a boolean if a field has been set.
func (o *SearchRulesParams) HasHitsPerPage() bool {
	if o != nil && o.HitsPerPage != nil {
		return true
	}

	return false
}

// SetHitsPerPage gets a reference to the given int32 and assigns it to the HitsPerPage field.
func (o *SearchRulesParams) SetHitsPerPage(v int32) {
	o.HitsPerPage = &v
}

// GetEnabled returns the Enabled field value if set, zero value otherwise (both if not set or set to explicit null).
func (o *SearchRulesParams) GetEnabled() bool {
	if o == nil || o.Enabled.Get() == nil {
		var ret bool
		return ret
	}
	return *o.Enabled.Get()
}

// GetEnabledOk returns a tuple with the Enabled field value if set, nil otherwise
// and a boolean to check if the value has been set.
// NOTE: If the value is an explicit nil, `nil, true` will be returned
func (o *SearchRulesParams) GetEnabledOk() (*bool, bool) {
	if o == nil {
		return nil, false
	}
	return o.Enabled.Get(), o.Enabled.IsSet()
}

// HasEnabled returns a boolean if a field has been set.
func (o *SearchRulesParams) HasEnabled() bool {
	if o != nil && o.Enabled.IsSet() {
		return true
	}

	return false
}

// SetEnabled gets a reference to the given NullableBool and assigns it to the Enabled field.
func (o *SearchRulesParams) SetEnabled(v bool) {
	o.Enabled.Set(&v)
}

// SetEnabledNil sets the value for Enabled to be an explicit nil
func (o *SearchRulesParams) SetEnabledNil() {
	o.Enabled.Set(nil)
}

// UnsetEnabled ensures that no value is present for Enabled, not even an explicit nil
func (o *SearchRulesParams) UnsetEnabled() {
	o.Enabled.Unset()
}

// GetRequestOptions returns the RequestOptions field value if set, zero value otherwise.
func (o *SearchRulesParams) GetRequestOptions() []map[string]interface{} {
	if o == nil || o.RequestOptions == nil {
		var ret []map[string]interface{}
		return ret
	}
	return o.RequestOptions
}

// GetRequestOptionsOk returns a tuple with the RequestOptions field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SearchRulesParams) GetRequestOptionsOk() ([]map[string]interface{}, bool) {
	if o == nil || o.RequestOptions == nil {
		return nil, false
	}
	return o.RequestOptions, true
}

// HasRequestOptions returns a boolean if a field has been set.
func (o *SearchRulesParams) HasRequestOptions() bool {
	if o != nil && o.RequestOptions != nil {
		return true
	}

	return false
}

// SetRequestOptions gets a reference to the given []map[string]interface{} and assigns it to the RequestOptions field.
func (o *SearchRulesParams) SetRequestOptions(v []map[string]interface{}) {
	o.RequestOptions = v
}

func (o SearchRulesParams) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if o.Query != nil {
		toSerialize["query"] = o.Query
	}
	if o.Anchoring != nil {
		toSerialize["anchoring"] = o.Anchoring
	}
	if o.Context != nil {
		toSerialize["context"] = o.Context
	}
	if o.Page != nil {
		toSerialize["page"] = o.Page
	}
	if o.HitsPerPage != nil {
		toSerialize["hitsPerPage"] = o.HitsPerPage
	}
	if o.Enabled.IsSet() {
		toSerialize["enabled"] = o.Enabled.Get()
	}
	if o.RequestOptions != nil {
		toSerialize["requestOptions"] = o.RequestOptions
	}
	return json.Marshal(toSerialize)
}

func (o SearchRulesParams) String() string {
	out := ""
	out += fmt.Sprintf("  query=%v\n", o.Query)
	out += fmt.Sprintf("  anchoring=%v\n", o.Anchoring)
	out += fmt.Sprintf("  context=%v\n", o.Context)
	out += fmt.Sprintf("  page=%v\n", o.Page)
	out += fmt.Sprintf("  hitsPerPage=%v\n", o.HitsPerPage)
	out += fmt.Sprintf("  enabled=%v\n", o.Enabled)
	out += fmt.Sprintf("  requestOptions=%v\n", o.RequestOptions)
	return fmt.Sprintf("SearchRulesParams {\n%s}", out)
}

type NullableSearchRulesParams struct {
	value *SearchRulesParams
	isSet bool
}

func (v NullableSearchRulesParams) Get() *SearchRulesParams {
	return v.value
}

func (v *NullableSearchRulesParams) Set(val *SearchRulesParams) {
	v.value = val
	v.isSet = true
}

func (v NullableSearchRulesParams) IsSet() bool {
	return v.isSet
}

func (v *NullableSearchRulesParams) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSearchRulesParams(val *SearchRulesParams) *NullableSearchRulesParams {
	return &NullableSearchRulesParams{value: val, isSet: true}
}

func (v NullableSearchRulesParams) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSearchRulesParams) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
