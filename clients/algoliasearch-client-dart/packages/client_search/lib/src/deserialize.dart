import 'package:algolia_client_search/src/model/add_api_key_response.dart';
import 'package:algolia_client_search/src/model/api_key.dart';
import 'package:algolia_client_search/src/model/assign_user_id_params.dart';
import 'package:algolia_client_search/src/model/automatic_facet_filter.dart';
import 'package:algolia_client_search/src/model/base_get_api_key_response.dart';
import 'package:algolia_client_search/src/model/base_index_settings.dart';
import 'package:algolia_client_search/src/model/base_search_params.dart';
import 'package:algolia_client_search/src/model/base_search_params_without_query.dart';
import 'package:algolia_client_search/src/model/base_search_response.dart';
import 'package:algolia_client_search/src/model/base_search_response_redirect.dart';
import 'package:algolia_client_search/src/model/batch_assign_user_ids_params.dart';
import 'package:algolia_client_search/src/model/batch_dictionary_entries_params.dart';
import 'package:algolia_client_search/src/model/batch_dictionary_entries_request.dart';
import 'package:algolia_client_search/src/model/batch_params.dart';
import 'package:algolia_client_search/src/model/batch_request.dart';
import 'package:algolia_client_search/src/model/batch_response.dart';
import 'package:algolia_client_search/src/model/batch_write_params.dart';
import 'package:algolia_client_search/src/model/browse_params_object.dart';
import 'package:algolia_client_search/src/model/browse_response.dart';
import 'package:algolia_client_search/src/model/built_in_operation.dart';
import 'package:algolia_client_search/src/model/condition.dart';
import 'package:algolia_client_search/src/model/consequence.dart';
import 'package:algolia_client_search/src/model/consequence_hide.dart';
import 'package:algolia_client_search/src/model/consequence_params.dart';
import 'package:algolia_client_search/src/model/consequence_query_object.dart';
import 'package:algolia_client_search/src/model/created_at_response.dart';
import 'package:algolia_client_search/src/model/cursor.dart';
import 'package:algolia_client_search/src/model/delete_api_key_response.dart';
import 'package:algolia_client_search/src/model/delete_by_params.dart';
import 'package:algolia_client_search/src/model/delete_source_response.dart';
import 'package:algolia_client_search/src/model/deleted_at_response.dart';
import 'package:algolia_client_search/src/model/dictionary_entry.dart';
import 'package:algolia_client_search/src/model/dictionary_language.dart';
import 'package:algolia_client_search/src/model/dictionary_settings_params.dart';
import 'package:algolia_client_search/src/model/edit.dart';
import 'package:algolia_client_search/src/model/error_base.dart';
import 'package:algolia_client_search/src/model/facet_hits.dart';
import 'package:algolia_client_search/src/model/facet_ordering.dart';
import 'package:algolia_client_search/src/model/facets.dart';
import 'package:algolia_client_search/src/model/facets_stats.dart';
import 'package:algolia_client_search/src/model/fetched_index.dart';
import 'package:algolia_client_search/src/model/get_api_key_response.dart';
import 'package:algolia_client_search/src/model/get_dictionary_settings_response.dart';
import 'package:algolia_client_search/src/model/get_logs_response.dart';
import 'package:algolia_client_search/src/model/get_objects_params.dart';
import 'package:algolia_client_search/src/model/get_objects_request.dart';
import 'package:algolia_client_search/src/model/get_objects_response.dart';
import 'package:algolia_client_search/src/model/get_task_response.dart';
import 'package:algolia_client_search/src/model/get_top_user_ids_response.dart';
import 'package:algolia_client_search/src/model/has_pending_mappings_response.dart';
import 'package:algolia_client_search/src/model/highlight_result_option.dart';
import 'package:algolia_client_search/src/model/hit.dart';
import 'package:algolia_client_search/src/model/index_settings.dart';
import 'package:algolia_client_search/src/model/index_settings_as_search_params.dart';
import 'package:algolia_client_search/src/model/index_settings_as_search_params_semantic_search.dart';
import 'package:algolia_client_search/src/model/languages.dart';
import 'package:algolia_client_search/src/model/list_api_keys_response.dart';
import 'package:algolia_client_search/src/model/list_clusters_response.dart';
import 'package:algolia_client_search/src/model/list_indices_response.dart';
import 'package:algolia_client_search/src/model/list_user_ids_response.dart';
import 'package:algolia_client_search/src/model/log.dart';
import 'package:algolia_client_search/src/model/log_query.dart';
import 'package:algolia_client_search/src/model/matched_geo_location.dart';
import 'package:algolia_client_search/src/model/model_source.dart';
import 'package:algolia_client_search/src/model/multiple_batch_request.dart';
import 'package:algolia_client_search/src/model/multiple_batch_response.dart';
import 'package:algolia_client_search/src/model/operation_index_params.dart';
import 'package:algolia_client_search/src/model/params.dart';
import 'package:algolia_client_search/src/model/personalization.dart';
import 'package:algolia_client_search/src/model/promote_object_id.dart';
import 'package:algolia_client_search/src/model/promote_object_ids.dart';
import 'package:algolia_client_search/src/model/ranking_info.dart';
import 'package:algolia_client_search/src/model/redirect_rule_index_metadata.dart';
import 'package:algolia_client_search/src/model/redirect_rule_index_metadata_data.dart';
import 'package:algolia_client_search/src/model/remove_user_id_response.dart';
import 'package:algolia_client_search/src/model/rendering_content.dart';
import 'package:algolia_client_search/src/model/replace_source_response.dart';
import 'package:algolia_client_search/src/model/rule.dart';
import 'package:algolia_client_search/src/model/save_object_response.dart';
import 'package:algolia_client_search/src/model/save_synonym_response.dart';
import 'package:algolia_client_search/src/model/search_dictionary_entries_params.dart';
import 'package:algolia_client_search/src/model/search_for_facet_values_request.dart';
import 'package:algolia_client_search/src/model/search_for_facet_values_response.dart';
import 'package:algolia_client_search/src/model/search_for_facets.dart';
import 'package:algolia_client_search/src/model/search_for_facets_options.dart';
import 'package:algolia_client_search/src/model/search_for_hits.dart';
import 'package:algolia_client_search/src/model/search_for_hits_options.dart';
import 'package:algolia_client_search/src/model/search_hits.dart';
import 'package:algolia_client_search/src/model/search_method_params.dart';
import 'package:algolia_client_search/src/model/search_params_object.dart';
import 'package:algolia_client_search/src/model/search_params_query.dart';
import 'package:algolia_client_search/src/model/search_params_string.dart';
import 'package:algolia_client_search/src/model/search_response.dart';
import 'package:algolia_client_search/src/model/search_responses.dart';
import 'package:algolia_client_search/src/model/search_rules_params.dart';
import 'package:algolia_client_search/src/model/search_rules_response.dart';
import 'package:algolia_client_search/src/model/search_synonyms_params.dart';
import 'package:algolia_client_search/src/model/search_synonyms_response.dart';
import 'package:algolia_client_search/src/model/search_user_ids_params.dart';
import 'package:algolia_client_search/src/model/search_user_ids_response.dart';
import 'package:algolia_client_search/src/model/snippet_result_option.dart';
import 'package:algolia_client_search/src/model/standard_entries.dart';
import 'package:algolia_client_search/src/model/synonym_hit.dart';
import 'package:algolia_client_search/src/model/time_range.dart';
import 'package:algolia_client_search/src/model/update_api_key_response.dart';
import 'package:algolia_client_search/src/model/updated_at_response.dart';
import 'package:algolia_client_search/src/model/updated_at_with_object_id_response.dart';
import 'package:algolia_client_search/src/model/updated_rule_response.dart';
import 'package:algolia_client_search/src/model/user_highlight_result.dart';
import 'package:algolia_client_search/src/model/user_hit.dart';
import 'package:algolia_client_search/src/model/user_id.dart';
import 'package:algolia_client_search/src/model/value.dart';

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
    case 'Acl':
    case 'Action':
    case 'AddApiKeyResponse':
      return AddApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AdvancedSyntaxFeatures':
    case 'AlternativesAsExact':
    case 'Anchoring':
    case 'ApiKey':
      return ApiKey.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AroundRadiusAll':
    case 'AssignUserIdParams':
      return AssignUserIdParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AutomaticFacetFilter':
      return AutomaticFacetFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseGetApiKeyResponse':
      return BaseGetApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BaseIndexSettings':
      return BaseIndexSettings.fromJson(value as Map<String, dynamic>)
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
    case 'BaseSearchResponseRedirect':
      return BaseSearchResponseRedirect.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BatchAssignUserIdsParams':
      return BatchAssignUserIdsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BatchDictionaryEntriesParams':
      return BatchDictionaryEntriesParams.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'BatchDictionaryEntriesRequest':
      return BatchDictionaryEntriesRequest.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'BatchParams':
      return BatchParams.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'BatchRequest':
      return BatchRequest.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'BatchResponse':
      return BatchResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BatchWriteParams':
      return BatchWriteParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BrowseParamsObject':
      return BrowseParamsObject.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BrowseResponse':
      return BrowseResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BuiltInOperation':
      return BuiltInOperation.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BuiltInOperationType':
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
    case 'CreatedAtResponse':
      return CreatedAtResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Cursor':
      return Cursor.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'DeleteApiKeyResponse':
      return DeleteApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeleteByParams':
      return DeleteByParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeleteSourceResponse':
      return DeleteSourceResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeletedAtResponse':
      return DeletedAtResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionaryAction':
    case 'DictionaryEntry':
      return DictionaryEntry.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionaryEntryState':
    case 'DictionaryLanguage':
      return DictionaryLanguage.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionarySettingsParams':
      return DictionarySettingsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionaryType':
    case 'Edit':
      return Edit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EditType':
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ExactOnSingleWordQuery':
    case 'FacetHits':
      return FacetHits.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FacetOrdering':
      return FacetOrdering.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Facets':
      return Facets.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FacetsStats':
      return FacetsStats.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FetchedIndex':
      return FetchedIndex.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetApiKeyResponse':
      return GetApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetDictionarySettingsResponse':
      return GetDictionarySettingsResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetLogsResponse':
      return GetLogsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetObjectsParams':
      return GetObjectsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetObjectsRequest':
      return GetObjectsRequest.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetObjectsResponse':
      return GetObjectsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTaskResponse':
      return GetTaskResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopUserIdsResponse':
      return GetTopUserIdsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'HasPendingMappingsResponse':
      return HasPendingMappingsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'HighlightResultOption':
      return HighlightResultOption.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Hit':
      return Hit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'IndexSettings':
      return IndexSettings.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IndexSettingsAsSearchParams':
      return IndexSettingsAsSearchParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IndexSettingsAsSearchParamsSemanticSearch':
      return IndexSettingsAsSearchParamsSemanticSearch.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'Languages':
      return Languages.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ListApiKeysResponse':
      return ListApiKeysResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListClustersResponse':
      return ListClustersResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListIndicesResponse':
      return ListIndicesResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListUserIdsResponse':
      return ListUserIdsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Log':
      return Log.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'LogQuery':
      return LogQuery.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'LogType':
    case 'MatchLevel':
    case 'MatchedGeoLocation':
      return MatchedGeoLocation.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Mode':
    case 'ModelSource':
      return ModelSource.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'MultipleBatchRequest':
      return MultipleBatchRequest.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'MultipleBatchResponse':
      return MultipleBatchResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OperationIndexParams':
      return OperationIndexParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OperationType':
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
    case 'RankingInfo':
      return RankingInfo.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RedirectRuleIndexMetadata':
      return RedirectRuleIndexMetadata.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RedirectRuleIndexMetadataData':
      return RedirectRuleIndexMetadataData.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'RemoveUserIdResponse':
      return RemoveUserIdResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RemoveWordsIfNoResults':
    case 'RenderingContent':
      return RenderingContent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ReplaceSourceResponse':
      return ReplaceSourceResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Rule':
      return Rule.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SaveObjectResponse':
      return SaveObjectResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SaveSynonymResponse':
      return SaveSynonymResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ScopeType':
    case 'SearchDictionaryEntriesParams':
      return SearchDictionaryEntriesParams.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'SearchForFacetValuesRequest':
      return SearchForFacetValuesRequest.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchForFacetValuesResponse':
      return SearchForFacetValuesResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'SearchForFacets':
      return SearchForFacets.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchForFacetsOptions':
      return SearchForFacetsOptions.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchForHits':
      return SearchForHits.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchForHitsOptions':
      return SearchForHitsOptions.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchHits':
      return SearchHits.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SearchMethodParams':
      return SearchMethodParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchParamsObject':
      return SearchParamsObject.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchParamsQuery':
      return SearchParamsQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchParamsString':
      return SearchParamsString.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchResponse':
      return SearchResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchResponses':
      return SearchResponses.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchRulesParams':
      return SearchRulesParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchRulesResponse':
      return SearchRulesResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchStrategy':
    case 'SearchSynonymsParams':
      return SearchSynonymsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchSynonymsResponse':
      return SearchSynonymsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchTypeDefault':
    case 'SearchTypeFacet':
    case 'SearchUserIdsParams':
      return SearchUserIdsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchUserIdsResponse':
      return SearchUserIdsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SnippetResultOption':
      return SnippetResultOption.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SortRemainingBy':
    case 'StandardEntries':
      return StandardEntries.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SynonymHit':
      return SynonymHit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SynonymType':
    case 'TaskStatus':
    case 'TimeRange':
      return TimeRange.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TypoToleranceEnum':
    case 'UpdateApiKeyResponse':
      return UpdateApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UpdatedAtResponse':
      return UpdatedAtResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UpdatedAtWithObjectIdResponse':
      return UpdatedAtWithObjectIdResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'UpdatedRuleResponse':
      return UpdatedRuleResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UserHighlightResult':
      return UserHighlightResult.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UserHit':
      return UserHit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'UserId':
      return UserId.fromJson(value as Map<String, dynamic>) as ReturnType;
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
      break;
  }
  throw Exception('Cannot deserialize');
}
