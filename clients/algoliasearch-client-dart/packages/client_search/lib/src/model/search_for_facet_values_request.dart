// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element

import 'package:json_annotation/json_annotation.dart';

part 'search_for_facet_values_request.g.dart';

@JsonSerializable()
final class SearchForFacetValuesRequest {
  /// Returns a new [SearchForFacetValuesRequest] instance.
  const SearchForFacetValuesRequest({
    this.params,
    this.facetQuery,
    this.maxFacetHits,
  });

  /// Search parameters as URL-encoded query string.
  @JsonKey(name: r'params')
  final String? params;

  /// Text to search inside the facet's values.
  @JsonKey(name: r'facetQuery')
  final String? facetQuery;

  /// Maximum number of facet hits to return during a search for facet values. For performance reasons, the maximum allowed number of returned values is 100.
  // maximum: 100
  @JsonKey(name: r'maxFacetHits')
  final int? maxFacetHits;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is SearchForFacetValuesRequest &&
          other.params == params &&
          other.facetQuery == facetQuery &&
          other.maxFacetHits == maxFacetHits;

  @override
  int get hashCode =>
      params.hashCode + facetQuery.hashCode + maxFacetHits.hashCode;

  factory SearchForFacetValuesRequest.fromJson(Map<String, dynamic> json) =>
      _$SearchForFacetValuesRequestFromJson(json);

  Map<String, dynamic> toJson() => _$SearchForFacetValuesRequestToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}