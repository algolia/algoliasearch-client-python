// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element
import 'package:algolia_client_search/src/model/search_type_facet.dart';

import 'package:json_annotation/json_annotation.dart';

part 'search_for_facets_options.g.dart';

@JsonSerializable()
final class SearchForFacetsOptions {
  /// Returns a new [SearchForFacetsOptions] instance.
  const SearchForFacetsOptions({
    required this.facet,
    required this.indexName,
    this.facetQuery,
    this.maxFacetHits,
    required this.type,
  });

  /// Facet name.
  @JsonKey(name: r'facet')
  final String facet;

  /// Algolia index name.
  @JsonKey(name: r'indexName')
  final String indexName;

  /// Text to search inside the facet's values.
  @JsonKey(name: r'facetQuery')
  final String? facetQuery;

  /// Maximum number of facet hits to return when [searching for facet values](https://www.algolia.com/doc/guides/managing-results/refine-results/faceting/#search-for-facet-values).
  // maximum: 100
  @JsonKey(name: r'maxFacetHits')
  final int? maxFacetHits;

  @JsonKey(name: r'type')
  final SearchTypeFacet type;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is SearchForFacetsOptions &&
          other.facet == facet &&
          other.indexName == indexName &&
          other.facetQuery == facetQuery &&
          other.maxFacetHits == maxFacetHits &&
          other.type == type;

  @override
  int get hashCode =>
      facet.hashCode +
      indexName.hashCode +
      facetQuery.hashCode +
      maxFacetHits.hashCode +
      type.hashCode;

  factory SearchForFacetsOptions.fromJson(Map<String, dynamic> json) =>
      _$SearchForFacetsOptionsFromJson(json);

  Map<String, dynamic> toJson() => _$SearchForFacetsOptionsToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}
