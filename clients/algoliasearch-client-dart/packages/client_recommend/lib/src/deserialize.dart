import 'package:algolia_client_recommend/src/model/advanced_syntax_features.dart';
import 'package:algolia_client_recommend/src/model/alternatives_as_exact.dart';
import 'package:algolia_client_recommend/src/model/anchoring.dart';
import 'package:algolia_client_recommend/src/model/around_precision_from_value_inner.dart';
import 'package:algolia_client_recommend/src/model/around_radius_all.dart';
import 'package:algolia_client_recommend/src/model/automatic_facet_filter.dart';
import 'package:algolia_client_recommend/src/model/base_recommend_request.dart';
import 'package:algolia_client_recommend/src/model/base_recommendations_query.dart';
import 'package:algolia_client_recommend/src/model/base_search_params.dart';
import 'package:algolia_client_recommend/src/model/base_search_params_without_query.dart';
import 'package:algolia_client_recommend/src/model/base_search_response.dart';
import 'package:algolia_client_recommend/src/model/base_trending_facets_query.dart';
import 'package:algolia_client_recommend/src/model/base_trending_items_query.dart';
import 'package:algolia_client_recommend/src/model/condition.dart';
import 'package:algolia_client_recommend/src/model/consequence.dart';
import 'package:algolia_client_recommend/src/model/consequence_hide.dart';
import 'package:algolia_client_recommend/src/model/consequence_params.dart';
import 'package:algolia_client_recommend/src/model/consequence_query_object.dart';
import 'package:algolia_client_recommend/src/model/deleted_at_response.dart';
import 'package:algolia_client_recommend/src/model/edit.dart';
import 'package:algolia_client_recommend/src/model/edit_type.dart';
import 'package:algolia_client_recommend/src/model/error_base.dart';
import 'package:algolia_client_recommend/src/model/exact_on_single_word_query.dart';
import 'package:algolia_client_recommend/src/model/exhaustive.dart';
import 'package:algolia_client_recommend/src/model/facet_ordering.dart';
import 'package:algolia_client_recommend/src/model/facets.dart';
import 'package:algolia_client_recommend/src/model/facets_stats.dart';
import 'package:algolia_client_recommend/src/model/get_recommend_task_response.dart';
import 'package:algolia_client_recommend/src/model/get_recommendations_params.dart';
import 'package:algolia_client_recommend/src/model/get_recommendations_response.dart';
import 'package:algolia_client_recommend/src/model/highlight_result_option.dart';
import 'package:algolia_client_recommend/src/model/index_settings_as_search_params.dart';
import 'package:algolia_client_recommend/src/model/match_level.dart';
import 'package:algolia_client_recommend/src/model/matched_geo_location.dart';
import 'package:algolia_client_recommend/src/model/mode.dart';
import 'package:algolia_client_recommend/src/model/params.dart';
import 'package:algolia_client_recommend/src/model/personalization.dart';
import 'package:algolia_client_recommend/src/model/promote_object_id.dart';
import 'package:algolia_client_recommend/src/model/promote_object_ids.dart';
import 'package:algolia_client_recommend/src/model/query_type.dart';
import 'package:algolia_client_recommend/src/model/ranking_info.dart';
import 'package:algolia_client_recommend/src/model/recommend_hit.dart';
import 'package:algolia_client_recommend/src/model/recommend_hits.dart';
import 'package:algolia_client_recommend/src/model/recommend_models.dart';
import 'package:algolia_client_recommend/src/model/recommendation_models.dart';
import 'package:algolia_client_recommend/src/model/recommendations_query.dart';
import 'package:algolia_client_recommend/src/model/recommendations_response.dart';
import 'package:algolia_client_recommend/src/model/redirect.dart';
import 'package:algolia_client_recommend/src/model/redirect_rule_index_metadata.dart';
import 'package:algolia_client_recommend/src/model/redirect_rule_index_metadata_data.dart';
import 'package:algolia_client_recommend/src/model/remove_words_if_no_results.dart';
import 'package:algolia_client_recommend/src/model/rendering_content.dart';
import 'package:algolia_client_recommend/src/model/rule_response.dart';
import 'package:algolia_client_recommend/src/model/rule_response_metadata.dart';
import 'package:algolia_client_recommend/src/model/search_params_object.dart';
import 'package:algolia_client_recommend/src/model/search_params_query.dart';
import 'package:algolia_client_recommend/src/model/search_recommend_rules_params.dart';
import 'package:algolia_client_recommend/src/model/search_recommend_rules_response.dart';
import 'package:algolia_client_recommend/src/model/semantic_search.dart';
import 'package:algolia_client_recommend/src/model/snippet_result_option.dart';
import 'package:algolia_client_recommend/src/model/sort_remaining_by.dart';
import 'package:algolia_client_recommend/src/model/task_status.dart';
import 'package:algolia_client_recommend/src/model/trending_facets_model.dart';
import 'package:algolia_client_recommend/src/model/trending_facets_query.dart';
import 'package:algolia_client_recommend/src/model/trending_items_model.dart';
import 'package:algolia_client_recommend/src/model/trending_items_query.dart';
import 'package:algolia_client_recommend/src/model/typo_tolerance_enum.dart';
import 'package:algolia_client_recommend/src/model/value.dart';

final _regList = RegExp(r'^List<(.*)>$');
final _regSet = RegExp(r'^Set<(.*)>$');
final _regMap = RegExp(r'^Map<String,(.*)>$');

ReturnType deserialize<ReturnType, BaseType>(dynamic value, String targetType,
    {bool growable = true}) {
  switch (targetType) {
    case 'String':
      return '$value' as ReturnType;
    case 'int':
      return (value is int ? value : int.parse('$value')) as ReturnType;
    case 'bool':
      if (value is bool) {
        return value as ReturnType;
      }
      final valueString = '$value'.toLowerCase();
      return (valueString == 'true' || valueString == '1') as ReturnType;
    case 'double':
      return (value is double ? value : double.parse('$value')) as ReturnType;
    case 'AdvancedSyntaxFeatures':
      return AdvancedSyntaxFeatures.fromJson(value) as ReturnType;
    case 'AlternativesAsExact':
      return AlternativesAsExact.fromJson(value) as ReturnType;
    case 'Anchoring':
      return Anchoring.fromJson(value) as ReturnType;
    case 'AroundPrecisionFromValueInner':
      return AroundPrecisionFromValueInner.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'AroundRadiusAll':
      return AroundRadiusAll.fromJson(value) as ReturnType;
    case 'AutomaticFacetFilter':
      return AutomaticFacetFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseRecommendRequest':
      return BaseRecommendRequest.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseRecommendationsQuery':
      return BaseRecommendationsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseSearchParams':
      return BaseSearchParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseSearchParamsWithoutQuery':
      return BaseSearchParamsWithoutQuery.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'BaseSearchResponse':
      return BaseSearchResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseTrendingFacetsQuery':
      return BaseTrendingFacetsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseTrendingItemsQuery':
      return BaseTrendingItemsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Condition':
      return Condition.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Consequence':
      return Consequence.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ConsequenceHide':
      return ConsequenceHide.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConsequenceParams':
      return ConsequenceParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConsequenceQueryObject':
      return ConsequenceQueryObject.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeletedAtResponse':
      return DeletedAtResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Edit':
      return Edit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EditType':
      return EditType.fromJson(value) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ExactOnSingleWordQuery':
      return ExactOnSingleWordQuery.fromJson(value) as ReturnType;
    case 'Exhaustive':
      return Exhaustive.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FacetOrdering':
      return FacetOrdering.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Facets':
      return Facets.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FacetsStats':
      return FacetsStats.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetRecommendTaskResponse':
      return GetRecommendTaskResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetRecommendationsParams':
      return GetRecommendationsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetRecommendationsResponse':
      return GetRecommendationsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'HighlightResultOption':
      return HighlightResultOption.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IndexSettingsAsSearchParams':
      return IndexSettingsAsSearchParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'MatchLevel':
      return MatchLevel.fromJson(value) as ReturnType;
    case 'MatchedGeoLocation':
      return MatchedGeoLocation.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Mode':
      return Mode.fromJson(value) as ReturnType;
    case 'Params':
      return Params.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Personalization':
      return Personalization.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'PromoteObjectID':
      return PromoteObjectID.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'PromoteObjectIDs':
      return PromoteObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'QueryType':
      return QueryType.fromJson(value) as ReturnType;
    case 'RankingInfo':
      return RankingInfo.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RecommendHit':
      return RecommendHit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RecommendHits':
      return RecommendHits.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RecommendModels':
      return RecommendModels.fromJson(value) as ReturnType;
    case 'RecommendationModels':
      return RecommendationModels.fromJson(value) as ReturnType;
    case 'RecommendationsQuery':
      return RecommendationsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RecommendationsResponse':
      return RecommendationsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Redirect':
      return Redirect.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RedirectRuleIndexMetadata':
      return RedirectRuleIndexMetadata.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RedirectRuleIndexMetadataData':
      return RedirectRuleIndexMetadataData.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'RemoveWordsIfNoResults':
      return RemoveWordsIfNoResults.fromJson(value) as ReturnType;
    case 'RenderingContent':
      return RenderingContent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RuleResponse':
      return RuleResponse.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RuleResponseMetadata':
      return RuleResponseMetadata.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchParamsObject':
      return SearchParamsObject.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchParamsQuery':
      return SearchParamsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchRecommendRulesParams':
      return SearchRecommendRulesParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchRecommendRulesResponse':
      return SearchRecommendRulesResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'SemanticSearch':
      return SemanticSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SnippetResultOption':
      return SnippetResultOption.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SortRemainingBy':
      return SortRemainingBy.fromJson(value) as ReturnType;
    case 'TaskStatus':
      return TaskStatus.fromJson(value) as ReturnType;
    case 'TrendingFacetsModel':
      return TrendingFacetsModel.fromJson(value) as ReturnType;
    case 'TrendingFacetsQuery':
      return TrendingFacetsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TrendingItemsModel':
      return TrendingItemsModel.fromJson(value) as ReturnType;
    case 'TrendingItemsQuery':
      return TrendingItemsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TypoToleranceEnum':
      return TypoToleranceEnum.fromJson(value) as ReturnType;
    case 'Value':
      return Value.fromJson(value as Map<String, dynamic>) as ReturnType;
    default:
      RegExpMatch? match;

      if (value is List && (match = _regList.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toList(growable: growable) as ReturnType;
      }
      if (value is Set && (match = _regSet.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toSet() as ReturnType;
      }
      if (value is Map && (match = _regMap.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return Map<dynamic, BaseType>.fromIterables(
          value.keys,
          value.values.map((dynamic v) => deserialize<BaseType, BaseType>(
              v, targetType,
              growable: growable)),
        ) as ReturnType;
      }
      if (targetType == 'Object') {
        return value;
      }
      break;
  }
  throw Exception('Cannot deserialize');
}
