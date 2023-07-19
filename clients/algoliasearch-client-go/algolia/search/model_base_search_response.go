// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package search

import (
	"encoding/json"
	"fmt"
)

// BaseSearchResponse struct for BaseSearchResponse
type BaseSearchResponse struct {
	// A/B test ID. This is only included in the response for indices that are part of an A/B test.
	AbTestID *int32 `json:"abTestID,omitempty"`
	// Variant ID. This is only included in the response for indices that are part of an A/B test.
	AbTestVariantID *int32 `json:"abTestVariantID,omitempty"`
	// Computed geographical location.
	AroundLatLng *string `json:"aroundLatLng,omitempty"`
	// Automatically-computed radius.
	AutomaticRadius *string `json:"automaticRadius,omitempty"`
	// Indicates whether the facet count is exhaustive (exact) or approximate.
	ExhaustiveFacetsCount *bool `json:"exhaustiveFacetsCount,omitempty"`
	// Indicates whether the number of hits `nbHits` is exhaustive (exact) or approximate.
	ExhaustiveNbHits bool `json:"exhaustiveNbHits" validate:"required"`
	// Indicates whether the search for typos was exhaustive (exact) or approximate.
	ExhaustiveTypo *bool `json:"exhaustiveTypo,omitempty"`
	// Mapping of each facet name to the corresponding facet counts.
	Facets *map[string]map[string]int32 `json:"facets,omitempty"`
	// Statistics for numerical facets.
	FacetsStats *map[string]FacetsStats `json:"facets_stats,omitempty"`
	// Number of hits per page.
	HitsPerPage int32 `json:"hitsPerPage" validate:"required"`
	// Index name used for the query.
	Index *string `json:"index,omitempty"`
	// Index name used for the query. During A/B testing, the targeted index isn't always the index used by the query.
	IndexUsed *string `json:"indexUsed,omitempty"`
	// Warnings about the query.
	Message *string `json:"message,omitempty"`
	// Number of hits the search query matched.
	NbHits int32 `json:"nbHits" validate:"required"`
	// Number of pages of results for the current query.
	NbPages int32 `json:"nbPages" validate:"required"`
	// Number of hits selected and sorted by the relevant sort algorithm.
	NbSortedHits *int32 `json:"nbSortedHits,omitempty"`
	// Page to retrieve (the first page is `0`, not `1`).
	Page int32 `json:"page" validate:"required"`
	// URL-encoded string of all search parameters.
	Params   string                      `json:"params" validate:"required"`
	Redirect *BaseSearchResponseRedirect `json:"redirect,omitempty"`
	// Post-[normalization](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/#what-does-normalization-mean) query string that will be searched.
	ParsedQuery *string `json:"parsedQuery,omitempty"`
	// Time the server took to process the request, in milliseconds.
	ProcessingTimeMS int32 `json:"processingTimeMS" validate:"required"`
	// Text to search for in an index.
	Query string `json:"query" validate:"required"`
	// Markup text indicating which parts of the original query have been removed to retrieve a non-empty result set.
	QueryAfterRemoval *string `json:"queryAfterRemoval,omitempty"`
	// Host name of the server that processed the request.
	ServerUsed *string `json:"serverUsed,omitempty"`
	// Lets you store custom data in your indices.
	UserData         map[string]interface{} `json:"userData,omitempty"`
	RenderingContent *RenderingContent      `json:"renderingContent,omitempty"`
}

type BaseSearchResponseOption func(f *BaseSearchResponse)

func WithBaseSearchResponseAbTestID(val int32) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.AbTestID = &val
	}
}

func WithBaseSearchResponseAbTestVariantID(val int32) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.AbTestVariantID = &val
	}
}

func WithBaseSearchResponseAroundLatLng(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.AroundLatLng = &val
	}
}

func WithBaseSearchResponseAutomaticRadius(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.AutomaticRadius = &val
	}
}

func WithBaseSearchResponseExhaustiveFacetsCount(val bool) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.ExhaustiveFacetsCount = &val
	}
}

func WithBaseSearchResponseExhaustiveTypo(val bool) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.ExhaustiveTypo = &val
	}
}

func WithBaseSearchResponseFacets(val map[string]map[string]int32) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.Facets = &val
	}
}

func WithBaseSearchResponseFacetsStats(val map[string]FacetsStats) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.FacetsStats = &val
	}
}

func WithBaseSearchResponseIndex(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.Index = &val
	}
}

func WithBaseSearchResponseIndexUsed(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.IndexUsed = &val
	}
}

func WithBaseSearchResponseMessage(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.Message = &val
	}
}

func WithBaseSearchResponseNbSortedHits(val int32) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.NbSortedHits = &val
	}
}

func WithBaseSearchResponseRedirect(val BaseSearchResponseRedirect) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.Redirect = &val
	}
}

func WithBaseSearchResponseParsedQuery(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.ParsedQuery = &val
	}
}

func WithBaseSearchResponseQueryAfterRemoval(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.QueryAfterRemoval = &val
	}
}

func WithBaseSearchResponseServerUsed(val string) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.ServerUsed = &val
	}
}

func WithBaseSearchResponseUserData(val map[string]interface{}) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.UserData = val
	}
}

func WithBaseSearchResponseRenderingContent(val RenderingContent) BaseSearchResponseOption {
	return func(f *BaseSearchResponse) {
		f.RenderingContent = &val
	}
}

// NewBaseSearchResponse instantiates a new BaseSearchResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBaseSearchResponse(exhaustiveNbHits bool, hitsPerPage int32, nbHits int32, nbPages int32, page int32, params string, processingTimeMS int32, query string, opts ...BaseSearchResponseOption) *BaseSearchResponse {
	this := &BaseSearchResponse{}
	this.ExhaustiveNbHits = exhaustiveNbHits
	this.HitsPerPage = hitsPerPage
	this.NbHits = nbHits
	this.NbPages = nbPages
	this.Page = page
	this.Params = params
	this.ProcessingTimeMS = processingTimeMS
	this.Query = query
	for _, opt := range opts {
		opt(this)
	}
	return this
}

// NewBaseSearchResponseWithDefaults instantiates a new BaseSearchResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBaseSearchResponseWithDefaults() *BaseSearchResponse {
	this := &BaseSearchResponse{}
	var hitsPerPage int32 = 20
	this.HitsPerPage = hitsPerPage
	var page int32 = 0
	this.Page = page
	var query string = ""
	this.Query = query
	return this
}

// GetAbTestID returns the AbTestID field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetAbTestID() int32 {
	if o == nil || o.AbTestID == nil {
		var ret int32
		return ret
	}
	return *o.AbTestID
}

// GetAbTestIDOk returns a tuple with the AbTestID field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetAbTestIDOk() (*int32, bool) {
	if o == nil || o.AbTestID == nil {
		return nil, false
	}
	return o.AbTestID, true
}

// HasAbTestID returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasAbTestID() bool {
	if o != nil && o.AbTestID != nil {
		return true
	}

	return false
}

// SetAbTestID gets a reference to the given int32 and assigns it to the AbTestID field.
func (o *BaseSearchResponse) SetAbTestID(v int32) {
	o.AbTestID = &v
}

// GetAbTestVariantID returns the AbTestVariantID field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetAbTestVariantID() int32 {
	if o == nil || o.AbTestVariantID == nil {
		var ret int32
		return ret
	}
	return *o.AbTestVariantID
}

// GetAbTestVariantIDOk returns a tuple with the AbTestVariantID field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetAbTestVariantIDOk() (*int32, bool) {
	if o == nil || o.AbTestVariantID == nil {
		return nil, false
	}
	return o.AbTestVariantID, true
}

// HasAbTestVariantID returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasAbTestVariantID() bool {
	if o != nil && o.AbTestVariantID != nil {
		return true
	}

	return false
}

// SetAbTestVariantID gets a reference to the given int32 and assigns it to the AbTestVariantID field.
func (o *BaseSearchResponse) SetAbTestVariantID(v int32) {
	o.AbTestVariantID = &v
}

// GetAroundLatLng returns the AroundLatLng field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetAroundLatLng() string {
	if o == nil || o.AroundLatLng == nil {
		var ret string
		return ret
	}
	return *o.AroundLatLng
}

// GetAroundLatLngOk returns a tuple with the AroundLatLng field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetAroundLatLngOk() (*string, bool) {
	if o == nil || o.AroundLatLng == nil {
		return nil, false
	}
	return o.AroundLatLng, true
}

// HasAroundLatLng returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasAroundLatLng() bool {
	if o != nil && o.AroundLatLng != nil {
		return true
	}

	return false
}

// SetAroundLatLng gets a reference to the given string and assigns it to the AroundLatLng field.
func (o *BaseSearchResponse) SetAroundLatLng(v string) {
	o.AroundLatLng = &v
}

// GetAutomaticRadius returns the AutomaticRadius field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetAutomaticRadius() string {
	if o == nil || o.AutomaticRadius == nil {
		var ret string
		return ret
	}
	return *o.AutomaticRadius
}

// GetAutomaticRadiusOk returns a tuple with the AutomaticRadius field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetAutomaticRadiusOk() (*string, bool) {
	if o == nil || o.AutomaticRadius == nil {
		return nil, false
	}
	return o.AutomaticRadius, true
}

// HasAutomaticRadius returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasAutomaticRadius() bool {
	if o != nil && o.AutomaticRadius != nil {
		return true
	}

	return false
}

// SetAutomaticRadius gets a reference to the given string and assigns it to the AutomaticRadius field.
func (o *BaseSearchResponse) SetAutomaticRadius(v string) {
	o.AutomaticRadius = &v
}

// GetExhaustiveFacetsCount returns the ExhaustiveFacetsCount field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetExhaustiveFacetsCount() bool {
	if o == nil || o.ExhaustiveFacetsCount == nil {
		var ret bool
		return ret
	}
	return *o.ExhaustiveFacetsCount
}

// GetExhaustiveFacetsCountOk returns a tuple with the ExhaustiveFacetsCount field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetExhaustiveFacetsCountOk() (*bool, bool) {
	if o == nil || o.ExhaustiveFacetsCount == nil {
		return nil, false
	}
	return o.ExhaustiveFacetsCount, true
}

// HasExhaustiveFacetsCount returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasExhaustiveFacetsCount() bool {
	if o != nil && o.ExhaustiveFacetsCount != nil {
		return true
	}

	return false
}

// SetExhaustiveFacetsCount gets a reference to the given bool and assigns it to the ExhaustiveFacetsCount field.
func (o *BaseSearchResponse) SetExhaustiveFacetsCount(v bool) {
	o.ExhaustiveFacetsCount = &v
}

// GetExhaustiveNbHits returns the ExhaustiveNbHits field value
func (o *BaseSearchResponse) GetExhaustiveNbHits() bool {
	if o == nil {
		var ret bool
		return ret
	}

	return o.ExhaustiveNbHits
}

// GetExhaustiveNbHitsOk returns a tuple with the ExhaustiveNbHits field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetExhaustiveNbHitsOk() (*bool, bool) {
	if o == nil {
		return nil, false
	}
	return &o.ExhaustiveNbHits, true
}

// SetExhaustiveNbHits sets field value
func (o *BaseSearchResponse) SetExhaustiveNbHits(v bool) {
	o.ExhaustiveNbHits = v
}

// GetExhaustiveTypo returns the ExhaustiveTypo field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetExhaustiveTypo() bool {
	if o == nil || o.ExhaustiveTypo == nil {
		var ret bool
		return ret
	}
	return *o.ExhaustiveTypo
}

// GetExhaustiveTypoOk returns a tuple with the ExhaustiveTypo field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetExhaustiveTypoOk() (*bool, bool) {
	if o == nil || o.ExhaustiveTypo == nil {
		return nil, false
	}
	return o.ExhaustiveTypo, true
}

// HasExhaustiveTypo returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasExhaustiveTypo() bool {
	if o != nil && o.ExhaustiveTypo != nil {
		return true
	}

	return false
}

// SetExhaustiveTypo gets a reference to the given bool and assigns it to the ExhaustiveTypo field.
func (o *BaseSearchResponse) SetExhaustiveTypo(v bool) {
	o.ExhaustiveTypo = &v
}

// GetFacets returns the Facets field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetFacets() map[string]map[string]int32 {
	if o == nil || o.Facets == nil {
		var ret map[string]map[string]int32
		return ret
	}
	return *o.Facets
}

// GetFacetsOk returns a tuple with the Facets field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetFacetsOk() (*map[string]map[string]int32, bool) {
	if o == nil || o.Facets == nil {
		return nil, false
	}
	return o.Facets, true
}

// HasFacets returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasFacets() bool {
	if o != nil && o.Facets != nil {
		return true
	}

	return false
}

// SetFacets gets a reference to the given map[string]map[string]int32 and assigns it to the Facets field.
func (o *BaseSearchResponse) SetFacets(v map[string]map[string]int32) {
	o.Facets = &v
}

// GetFacetsStats returns the FacetsStats field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetFacetsStats() map[string]FacetsStats {
	if o == nil || o.FacetsStats == nil {
		var ret map[string]FacetsStats
		return ret
	}
	return *o.FacetsStats
}

// GetFacetsStatsOk returns a tuple with the FacetsStats field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetFacetsStatsOk() (*map[string]FacetsStats, bool) {
	if o == nil || o.FacetsStats == nil {
		return nil, false
	}
	return o.FacetsStats, true
}

// HasFacetsStats returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasFacetsStats() bool {
	if o != nil && o.FacetsStats != nil {
		return true
	}

	return false
}

// SetFacetsStats gets a reference to the given map[string]FacetsStats and assigns it to the FacetsStats field.
func (o *BaseSearchResponse) SetFacetsStats(v map[string]FacetsStats) {
	o.FacetsStats = &v
}

// GetHitsPerPage returns the HitsPerPage field value
func (o *BaseSearchResponse) GetHitsPerPage() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.HitsPerPage
}

// GetHitsPerPageOk returns a tuple with the HitsPerPage field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetHitsPerPageOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.HitsPerPage, true
}

// SetHitsPerPage sets field value
func (o *BaseSearchResponse) SetHitsPerPage(v int32) {
	o.HitsPerPage = v
}

// GetIndex returns the Index field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetIndex() string {
	if o == nil || o.Index == nil {
		var ret string
		return ret
	}
	return *o.Index
}

// GetIndexOk returns a tuple with the Index field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetIndexOk() (*string, bool) {
	if o == nil || o.Index == nil {
		return nil, false
	}
	return o.Index, true
}

// HasIndex returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasIndex() bool {
	if o != nil && o.Index != nil {
		return true
	}

	return false
}

// SetIndex gets a reference to the given string and assigns it to the Index field.
func (o *BaseSearchResponse) SetIndex(v string) {
	o.Index = &v
}

// GetIndexUsed returns the IndexUsed field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetIndexUsed() string {
	if o == nil || o.IndexUsed == nil {
		var ret string
		return ret
	}
	return *o.IndexUsed
}

// GetIndexUsedOk returns a tuple with the IndexUsed field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetIndexUsedOk() (*string, bool) {
	if o == nil || o.IndexUsed == nil {
		return nil, false
	}
	return o.IndexUsed, true
}

// HasIndexUsed returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasIndexUsed() bool {
	if o != nil && o.IndexUsed != nil {
		return true
	}

	return false
}

// SetIndexUsed gets a reference to the given string and assigns it to the IndexUsed field.
func (o *BaseSearchResponse) SetIndexUsed(v string) {
	o.IndexUsed = &v
}

// GetMessage returns the Message field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetMessage() string {
	if o == nil || o.Message == nil {
		var ret string
		return ret
	}
	return *o.Message
}

// GetMessageOk returns a tuple with the Message field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetMessageOk() (*string, bool) {
	if o == nil || o.Message == nil {
		return nil, false
	}
	return o.Message, true
}

// HasMessage returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasMessage() bool {
	if o != nil && o.Message != nil {
		return true
	}

	return false
}

// SetMessage gets a reference to the given string and assigns it to the Message field.
func (o *BaseSearchResponse) SetMessage(v string) {
	o.Message = &v
}

// GetNbHits returns the NbHits field value
func (o *BaseSearchResponse) GetNbHits() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.NbHits
}

// GetNbHitsOk returns a tuple with the NbHits field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetNbHitsOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.NbHits, true
}

// SetNbHits sets field value
func (o *BaseSearchResponse) SetNbHits(v int32) {
	o.NbHits = v
}

// GetNbPages returns the NbPages field value
func (o *BaseSearchResponse) GetNbPages() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.NbPages
}

// GetNbPagesOk returns a tuple with the NbPages field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetNbPagesOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.NbPages, true
}

// SetNbPages sets field value
func (o *BaseSearchResponse) SetNbPages(v int32) {
	o.NbPages = v
}

// GetNbSortedHits returns the NbSortedHits field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetNbSortedHits() int32 {
	if o == nil || o.NbSortedHits == nil {
		var ret int32
		return ret
	}
	return *o.NbSortedHits
}

// GetNbSortedHitsOk returns a tuple with the NbSortedHits field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetNbSortedHitsOk() (*int32, bool) {
	if o == nil || o.NbSortedHits == nil {
		return nil, false
	}
	return o.NbSortedHits, true
}

// HasNbSortedHits returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasNbSortedHits() bool {
	if o != nil && o.NbSortedHits != nil {
		return true
	}

	return false
}

// SetNbSortedHits gets a reference to the given int32 and assigns it to the NbSortedHits field.
func (o *BaseSearchResponse) SetNbSortedHits(v int32) {
	o.NbSortedHits = &v
}

// GetPage returns the Page field value
func (o *BaseSearchResponse) GetPage() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.Page
}

// GetPageOk returns a tuple with the Page field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetPageOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Page, true
}

// SetPage sets field value
func (o *BaseSearchResponse) SetPage(v int32) {
	o.Page = v
}

// GetParams returns the Params field value
func (o *BaseSearchResponse) GetParams() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Params
}

// GetParamsOk returns a tuple with the Params field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetParamsOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Params, true
}

// SetParams sets field value
func (o *BaseSearchResponse) SetParams(v string) {
	o.Params = v
}

// GetRedirect returns the Redirect field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetRedirect() BaseSearchResponseRedirect {
	if o == nil || o.Redirect == nil {
		var ret BaseSearchResponseRedirect
		return ret
	}
	return *o.Redirect
}

// GetRedirectOk returns a tuple with the Redirect field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetRedirectOk() (*BaseSearchResponseRedirect, bool) {
	if o == nil || o.Redirect == nil {
		return nil, false
	}
	return o.Redirect, true
}

// HasRedirect returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasRedirect() bool {
	if o != nil && o.Redirect != nil {
		return true
	}

	return false
}

// SetRedirect gets a reference to the given BaseSearchResponseRedirect and assigns it to the Redirect field.
func (o *BaseSearchResponse) SetRedirect(v BaseSearchResponseRedirect) {
	o.Redirect = &v
}

// GetParsedQuery returns the ParsedQuery field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetParsedQuery() string {
	if o == nil || o.ParsedQuery == nil {
		var ret string
		return ret
	}
	return *o.ParsedQuery
}

// GetParsedQueryOk returns a tuple with the ParsedQuery field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetParsedQueryOk() (*string, bool) {
	if o == nil || o.ParsedQuery == nil {
		return nil, false
	}
	return o.ParsedQuery, true
}

// HasParsedQuery returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasParsedQuery() bool {
	if o != nil && o.ParsedQuery != nil {
		return true
	}

	return false
}

// SetParsedQuery gets a reference to the given string and assigns it to the ParsedQuery field.
func (o *BaseSearchResponse) SetParsedQuery(v string) {
	o.ParsedQuery = &v
}

// GetProcessingTimeMS returns the ProcessingTimeMS field value
func (o *BaseSearchResponse) GetProcessingTimeMS() int32 {
	if o == nil {
		var ret int32
		return ret
	}

	return o.ProcessingTimeMS
}

// GetProcessingTimeMSOk returns a tuple with the ProcessingTimeMS field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetProcessingTimeMSOk() (*int32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.ProcessingTimeMS, true
}

// SetProcessingTimeMS sets field value
func (o *BaseSearchResponse) SetProcessingTimeMS(v int32) {
	o.ProcessingTimeMS = v
}

// GetQuery returns the Query field value
func (o *BaseSearchResponse) GetQuery() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Query
}

// GetQueryOk returns a tuple with the Query field value
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetQueryOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Query, true
}

// SetQuery sets field value
func (o *BaseSearchResponse) SetQuery(v string) {
	o.Query = v
}

// GetQueryAfterRemoval returns the QueryAfterRemoval field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetQueryAfterRemoval() string {
	if o == nil || o.QueryAfterRemoval == nil {
		var ret string
		return ret
	}
	return *o.QueryAfterRemoval
}

// GetQueryAfterRemovalOk returns a tuple with the QueryAfterRemoval field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetQueryAfterRemovalOk() (*string, bool) {
	if o == nil || o.QueryAfterRemoval == nil {
		return nil, false
	}
	return o.QueryAfterRemoval, true
}

// HasQueryAfterRemoval returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasQueryAfterRemoval() bool {
	if o != nil && o.QueryAfterRemoval != nil {
		return true
	}

	return false
}

// SetQueryAfterRemoval gets a reference to the given string and assigns it to the QueryAfterRemoval field.
func (o *BaseSearchResponse) SetQueryAfterRemoval(v string) {
	o.QueryAfterRemoval = &v
}

// GetServerUsed returns the ServerUsed field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetServerUsed() string {
	if o == nil || o.ServerUsed == nil {
		var ret string
		return ret
	}
	return *o.ServerUsed
}

// GetServerUsedOk returns a tuple with the ServerUsed field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetServerUsedOk() (*string, bool) {
	if o == nil || o.ServerUsed == nil {
		return nil, false
	}
	return o.ServerUsed, true
}

// HasServerUsed returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasServerUsed() bool {
	if o != nil && o.ServerUsed != nil {
		return true
	}

	return false
}

// SetServerUsed gets a reference to the given string and assigns it to the ServerUsed field.
func (o *BaseSearchResponse) SetServerUsed(v string) {
	o.ServerUsed = &v
}

// GetUserData returns the UserData field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetUserData() map[string]interface{} {
	if o == nil || o.UserData == nil {
		var ret map[string]interface{}
		return ret
	}
	return o.UserData
}

// GetUserDataOk returns a tuple with the UserData field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetUserDataOk() (map[string]interface{}, bool) {
	if o == nil || o.UserData == nil {
		return nil, false
	}
	return o.UserData, true
}

// HasUserData returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasUserData() bool {
	if o != nil && o.UserData != nil {
		return true
	}

	return false
}

// SetUserData gets a reference to the given map[string]interface{} and assigns it to the UserData field.
func (o *BaseSearchResponse) SetUserData(v map[string]interface{}) {
	o.UserData = v
}

// GetRenderingContent returns the RenderingContent field value if set, zero value otherwise.
func (o *BaseSearchResponse) GetRenderingContent() RenderingContent {
	if o == nil || o.RenderingContent == nil {
		var ret RenderingContent
		return ret
	}
	return *o.RenderingContent
}

// GetRenderingContentOk returns a tuple with the RenderingContent field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BaseSearchResponse) GetRenderingContentOk() (*RenderingContent, bool) {
	if o == nil || o.RenderingContent == nil {
		return nil, false
	}
	return o.RenderingContent, true
}

// HasRenderingContent returns a boolean if a field has been set.
func (o *BaseSearchResponse) HasRenderingContent() bool {
	if o != nil && o.RenderingContent != nil {
		return true
	}

	return false
}

// SetRenderingContent gets a reference to the given RenderingContent and assigns it to the RenderingContent field.
func (o *BaseSearchResponse) SetRenderingContent(v RenderingContent) {
	o.RenderingContent = &v
}

func (o BaseSearchResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if o.AbTestID != nil {
		toSerialize["abTestID"] = o.AbTestID
	}
	if o.AbTestVariantID != nil {
		toSerialize["abTestVariantID"] = o.AbTestVariantID
	}
	if o.AroundLatLng != nil {
		toSerialize["aroundLatLng"] = o.AroundLatLng
	}
	if o.AutomaticRadius != nil {
		toSerialize["automaticRadius"] = o.AutomaticRadius
	}
	if o.ExhaustiveFacetsCount != nil {
		toSerialize["exhaustiveFacetsCount"] = o.ExhaustiveFacetsCount
	}
	if true {
		toSerialize["exhaustiveNbHits"] = o.ExhaustiveNbHits
	}
	if o.ExhaustiveTypo != nil {
		toSerialize["exhaustiveTypo"] = o.ExhaustiveTypo
	}
	if o.Facets != nil {
		toSerialize["facets"] = o.Facets
	}
	if o.FacetsStats != nil {
		toSerialize["facets_stats"] = o.FacetsStats
	}
	if true {
		toSerialize["hitsPerPage"] = o.HitsPerPage
	}
	if o.Index != nil {
		toSerialize["index"] = o.Index
	}
	if o.IndexUsed != nil {
		toSerialize["indexUsed"] = o.IndexUsed
	}
	if o.Message != nil {
		toSerialize["message"] = o.Message
	}
	if true {
		toSerialize["nbHits"] = o.NbHits
	}
	if true {
		toSerialize["nbPages"] = o.NbPages
	}
	if o.NbSortedHits != nil {
		toSerialize["nbSortedHits"] = o.NbSortedHits
	}
	if true {
		toSerialize["page"] = o.Page
	}
	if true {
		toSerialize["params"] = o.Params
	}
	if o.Redirect != nil {
		toSerialize["redirect"] = o.Redirect
	}
	if o.ParsedQuery != nil {
		toSerialize["parsedQuery"] = o.ParsedQuery
	}
	if true {
		toSerialize["processingTimeMS"] = o.ProcessingTimeMS
	}
	if true {
		toSerialize["query"] = o.Query
	}
	if o.QueryAfterRemoval != nil {
		toSerialize["queryAfterRemoval"] = o.QueryAfterRemoval
	}
	if o.ServerUsed != nil {
		toSerialize["serverUsed"] = o.ServerUsed
	}
	if o.UserData != nil {
		toSerialize["userData"] = o.UserData
	}
	if o.RenderingContent != nil {
		toSerialize["renderingContent"] = o.RenderingContent
	}
	return json.Marshal(toSerialize)
}

func (o BaseSearchResponse) String() string {
	out := ""
	out += fmt.Sprintf("  abTestID=%v\n", o.AbTestID)
	out += fmt.Sprintf("  abTestVariantID=%v\n", o.AbTestVariantID)
	out += fmt.Sprintf("  aroundLatLng=%v\n", o.AroundLatLng)
	out += fmt.Sprintf("  automaticRadius=%v\n", o.AutomaticRadius)
	out += fmt.Sprintf("  exhaustiveFacetsCount=%v\n", o.ExhaustiveFacetsCount)
	out += fmt.Sprintf("  exhaustiveNbHits=%v\n", o.ExhaustiveNbHits)
	out += fmt.Sprintf("  exhaustiveTypo=%v\n", o.ExhaustiveTypo)
	out += fmt.Sprintf("  facets=%v\n", o.Facets)
	out += fmt.Sprintf("  facets_stats=%v\n", o.FacetsStats)
	out += fmt.Sprintf("  hitsPerPage=%v\n", o.HitsPerPage)
	out += fmt.Sprintf("  index=%v\n", o.Index)
	out += fmt.Sprintf("  indexUsed=%v\n", o.IndexUsed)
	out += fmt.Sprintf("  message=%v\n", o.Message)
	out += fmt.Sprintf("  nbHits=%v\n", o.NbHits)
	out += fmt.Sprintf("  nbPages=%v\n", o.NbPages)
	out += fmt.Sprintf("  nbSortedHits=%v\n", o.NbSortedHits)
	out += fmt.Sprintf("  page=%v\n", o.Page)
	out += fmt.Sprintf("  params=%v\n", o.Params)
	out += fmt.Sprintf("  redirect=%v\n", o.Redirect)
	out += fmt.Sprintf("  parsedQuery=%v\n", o.ParsedQuery)
	out += fmt.Sprintf("  processingTimeMS=%v\n", o.ProcessingTimeMS)
	out += fmt.Sprintf("  query=%v\n", o.Query)
	out += fmt.Sprintf("  queryAfterRemoval=%v\n", o.QueryAfterRemoval)
	out += fmt.Sprintf("  serverUsed=%v\n", o.ServerUsed)
	out += fmt.Sprintf("  userData=%v\n", o.UserData)
	out += fmt.Sprintf("  renderingContent=%v\n", o.RenderingContent)
	return fmt.Sprintf("BaseSearchResponse {\n%s}", out)
}

type NullableBaseSearchResponse struct {
	value *BaseSearchResponse
	isSet bool
}

func (v NullableBaseSearchResponse) Get() *BaseSearchResponse {
	return v.value
}

func (v *NullableBaseSearchResponse) Set(val *BaseSearchResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableBaseSearchResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableBaseSearchResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBaseSearchResponse(val *BaseSearchResponse) *NullableBaseSearchResponse {
	return &NullableBaseSearchResponse{value: val, isSet: true}
}

func (v NullableBaseSearchResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBaseSearchResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
