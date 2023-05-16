// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
package ingestion

import (
	"encoding/json"
	"fmt"
)

// SourceBigQuery struct for SourceBigQuery
type SourceBigQuery struct {
	// Project ID of the BigQuery Source.
	ProjectID string `json:"projectID" validate:"required"`
	// Dataset ID of the BigQuery Source.
	DatasetID string            `json:"datasetID" validate:"required"`
	DataType  *BigQueryDataType `json:"dataType,omitempty"`
	// Table name (for default BQ).
	Table *string `json:"table,omitempty"`
	// Table prefix (for Google Analytics).
	TablePrefix *string `json:"tablePrefix,omitempty"`
	// Custom SQL request to extract data from the BigQuery table.
	CustomSQLRequest *string `json:"customSQLRequest,omitempty"`
}

type SourceBigQueryOption func(f *SourceBigQuery)

func WithSourceBigQueryDataType(val BigQueryDataType) SourceBigQueryOption {
	return func(f *SourceBigQuery) {
		f.DataType = &val
	}
}

func WithSourceBigQueryTable(val string) SourceBigQueryOption {
	return func(f *SourceBigQuery) {
		f.Table = &val
	}
}

func WithSourceBigQueryTablePrefix(val string) SourceBigQueryOption {
	return func(f *SourceBigQuery) {
		f.TablePrefix = &val
	}
}

func WithSourceBigQueryCustomSQLRequest(val string) SourceBigQueryOption {
	return func(f *SourceBigQuery) {
		f.CustomSQLRequest = &val
	}
}

// NewSourceBigQuery instantiates a new SourceBigQuery object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSourceBigQuery(projectID string, datasetID string, opts ...SourceBigQueryOption) *SourceBigQuery {
	this := &SourceBigQuery{}
	this.ProjectID = projectID
	this.DatasetID = datasetID
	for _, opt := range opts {
		opt(this)
	}
	return this
}

// NewSourceBigQueryWithDefaults instantiates a new SourceBigQuery object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSourceBigQueryWithDefaults() *SourceBigQuery {
	this := &SourceBigQuery{}
	return this
}

// GetProjectID returns the ProjectID field value
func (o *SourceBigQuery) GetProjectID() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.ProjectID
}

// GetProjectIDOk returns a tuple with the ProjectID field value
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetProjectIDOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.ProjectID, true
}

// SetProjectID sets field value
func (o *SourceBigQuery) SetProjectID(v string) {
	o.ProjectID = v
}

// GetDatasetID returns the DatasetID field value
func (o *SourceBigQuery) GetDatasetID() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.DatasetID
}

// GetDatasetIDOk returns a tuple with the DatasetID field value
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetDatasetIDOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.DatasetID, true
}

// SetDatasetID sets field value
func (o *SourceBigQuery) SetDatasetID(v string) {
	o.DatasetID = v
}

// GetDataType returns the DataType field value if set, zero value otherwise.
func (o *SourceBigQuery) GetDataType() BigQueryDataType {
	if o == nil || o.DataType == nil {
		var ret BigQueryDataType
		return ret
	}
	return *o.DataType
}

// GetDataTypeOk returns a tuple with the DataType field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetDataTypeOk() (*BigQueryDataType, bool) {
	if o == nil || o.DataType == nil {
		return nil, false
	}
	return o.DataType, true
}

// HasDataType returns a boolean if a field has been set.
func (o *SourceBigQuery) HasDataType() bool {
	if o != nil && o.DataType != nil {
		return true
	}

	return false
}

// SetDataType gets a reference to the given BigQueryDataType and assigns it to the DataType field.
func (o *SourceBigQuery) SetDataType(v BigQueryDataType) {
	o.DataType = &v
}

// GetTable returns the Table field value if set, zero value otherwise.
func (o *SourceBigQuery) GetTable() string {
	if o == nil || o.Table == nil {
		var ret string
		return ret
	}
	return *o.Table
}

// GetTableOk returns a tuple with the Table field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetTableOk() (*string, bool) {
	if o == nil || o.Table == nil {
		return nil, false
	}
	return o.Table, true
}

// HasTable returns a boolean if a field has been set.
func (o *SourceBigQuery) HasTable() bool {
	if o != nil && o.Table != nil {
		return true
	}

	return false
}

// SetTable gets a reference to the given string and assigns it to the Table field.
func (o *SourceBigQuery) SetTable(v string) {
	o.Table = &v
}

// GetTablePrefix returns the TablePrefix field value if set, zero value otherwise.
func (o *SourceBigQuery) GetTablePrefix() string {
	if o == nil || o.TablePrefix == nil {
		var ret string
		return ret
	}
	return *o.TablePrefix
}

// GetTablePrefixOk returns a tuple with the TablePrefix field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetTablePrefixOk() (*string, bool) {
	if o == nil || o.TablePrefix == nil {
		return nil, false
	}
	return o.TablePrefix, true
}

// HasTablePrefix returns a boolean if a field has been set.
func (o *SourceBigQuery) HasTablePrefix() bool {
	if o != nil && o.TablePrefix != nil {
		return true
	}

	return false
}

// SetTablePrefix gets a reference to the given string and assigns it to the TablePrefix field.
func (o *SourceBigQuery) SetTablePrefix(v string) {
	o.TablePrefix = &v
}

// GetCustomSQLRequest returns the CustomSQLRequest field value if set, zero value otherwise.
func (o *SourceBigQuery) GetCustomSQLRequest() string {
	if o == nil || o.CustomSQLRequest == nil {
		var ret string
		return ret
	}
	return *o.CustomSQLRequest
}

// GetCustomSQLRequestOk returns a tuple with the CustomSQLRequest field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SourceBigQuery) GetCustomSQLRequestOk() (*string, bool) {
	if o == nil || o.CustomSQLRequest == nil {
		return nil, false
	}
	return o.CustomSQLRequest, true
}

// HasCustomSQLRequest returns a boolean if a field has been set.
func (o *SourceBigQuery) HasCustomSQLRequest() bool {
	if o != nil && o.CustomSQLRequest != nil {
		return true
	}

	return false
}

// SetCustomSQLRequest gets a reference to the given string and assigns it to the CustomSQLRequest field.
func (o *SourceBigQuery) SetCustomSQLRequest(v string) {
	o.CustomSQLRequest = &v
}

func (o SourceBigQuery) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]any{}
	if true {
		toSerialize["projectID"] = o.ProjectID
	}
	if true {
		toSerialize["datasetID"] = o.DatasetID
	}
	if o.DataType != nil {
		toSerialize["dataType"] = o.DataType
	}
	if o.Table != nil {
		toSerialize["table"] = o.Table
	}
	if o.TablePrefix != nil {
		toSerialize["tablePrefix"] = o.TablePrefix
	}
	if o.CustomSQLRequest != nil {
		toSerialize["customSQLRequest"] = o.CustomSQLRequest
	}
	return json.Marshal(toSerialize)
}

func (o SourceBigQuery) String() string {
	out := ""
	out += fmt.Sprintf("  projectID=%v\n", o.ProjectID)
	out += fmt.Sprintf("  datasetID=%v\n", o.DatasetID)
	out += fmt.Sprintf("  dataType=%v\n", o.DataType)
	out += fmt.Sprintf("  table=%v\n", o.Table)
	out += fmt.Sprintf("  tablePrefix=%v\n", o.TablePrefix)
	out += fmt.Sprintf("  customSQLRequest=%v\n", o.CustomSQLRequest)
	return fmt.Sprintf("SourceBigQuery {\n%s}", out)
}

type NullableSourceBigQuery struct {
	value *SourceBigQuery
	isSet bool
}

func (v NullableSourceBigQuery) Get() *SourceBigQuery {
	return v.value
}

func (v *NullableSourceBigQuery) Set(val *SourceBigQuery) {
	v.value = val
	v.isSet = true
}

func (v NullableSourceBigQuery) IsSet() bool {
	return v.isSet
}

func (v *NullableSourceBigQuery) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSourceBigQuery(val *SourceBigQuery) *NullableSourceBigQuery {
	return &NullableSourceBigQuery{value: val, isSet: true}
}

func (v NullableSourceBigQuery) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSourceBigQuery) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
