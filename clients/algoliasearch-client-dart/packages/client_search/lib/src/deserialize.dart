import 'package:algolia_client_search/src/model/acl.dart';
import 'package:algolia_client_search/src/model/action.dart';
import 'package:algolia_client_search/src/model/add_api_key_response.dart';
import 'package:algolia_client_search/src/model/advanced_syntax_features.dart';
import 'package:algolia_client_search/src/model/alternatives_as_exact.dart';
import 'package:algolia_client_search/src/model/anchoring.dart';
import 'package:algolia_client_search/src/model/api_key.dart';
import 'package:algolia_client_search/src/model/around_precision_from_value_inner.dart';
import 'package:algolia_client_search/src/model/around_radius_all.dart';
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
import 'package:algolia_client_search/src/model/built_in_operation_type.dart';
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
import 'package:algolia_client_search/src/model/dictionary_action.dart';
import 'package:algolia_client_search/src/model/dictionary_entry.dart';
import 'package:algolia_client_search/src/model/dictionary_entry_state.dart';
import 'package:algolia_client_search/src/model/dictionary_language.dart';
import 'package:algolia_client_search/src/model/dictionary_settings_params.dart';
import 'package:algolia_client_search/src/model/dictionary_type.dart';
import 'package:algolia_client_search/src/model/edit.dart';
import 'package:algolia_client_search/src/model/edit_type.dart';
import 'package:algolia_client_search/src/model/error_base.dart';
import 'package:algolia_client_search/src/model/exact_on_single_word_query.dart';
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
import 'package:algolia_client_search/src/model/languages.dart';
import 'package:algolia_client_search/src/model/list_api_keys_response.dart';
import 'package:algolia_client_search/src/model/list_clusters_response.dart';
import 'package:algolia_client_search/src/model/list_indices_response.dart';
import 'package:algolia_client_search/src/model/list_user_ids_response.dart';
import 'package:algolia_client_search/src/model/log.dart';
import 'package:algolia_client_search/src/model/log_query.dart';
import 'package:algolia_client_search/src/model/log_type.dart';
import 'package:algolia_client_search/src/model/match_level.dart';
import 'package:algolia_client_search/src/model/matched_geo_location.dart';
import 'package:algolia_client_search/src/model/mode.dart';
import 'package:algolia_client_search/src/model/multiple_batch_request.dart';
import 'package:algolia_client_search/src/model/multiple_batch_response.dart';
import 'package:algolia_client_search/src/model/operation_index_params.dart';
import 'package:algolia_client_search/src/model/operation_type.dart';
import 'package:algolia_client_search/src/model/params.dart';
import 'package:algolia_client_search/src/model/personalization.dart';
import 'package:algolia_client_search/src/model/promote_object_id.dart';
import 'package:algolia_client_search/src/model/promote_object_ids.dart';
import 'package:algolia_client_search/src/model/query_type.dart';
import 'package:algolia_client_search/src/model/ranking_info.dart';
import 'package:algolia_client_search/src/model/redirect_rule_index_metadata.dart';
import 'package:algolia_client_search/src/model/redirect_rule_index_metadata_data.dart';
import 'package:algolia_client_search/src/model/remove_user_id_response.dart';
import 'package:algolia_client_search/src/model/remove_words_if_no_results.dart';
import 'package:algolia_client_search/src/model/rendering_content.dart';
import 'package:algolia_client_search/src/model/replace_source_response.dart';
import 'package:algolia_client_search/src/model/rule.dart';
import 'package:algolia_client_search/src/model/save_object_response.dart';
import 'package:algolia_client_search/src/model/save_synonym_response.dart';
import 'package:algolia_client_search/src/model/scope_type.dart';
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
import 'package:algolia_client_search/src/model/search_strategy.dart';
import 'package:algolia_client_search/src/model/search_synonyms_params.dart';
import 'package:algolia_client_search/src/model/search_synonyms_response.dart';
import 'package:algolia_client_search/src/model/search_type_default.dart';
import 'package:algolia_client_search/src/model/search_type_facet.dart';
import 'package:algolia_client_search/src/model/search_user_ids_params.dart';
import 'package:algolia_client_search/src/model/search_user_ids_response.dart';
import 'package:algolia_client_search/src/model/semantic_search.dart';
import 'package:algolia_client_search/src/model/snippet_result_option.dart';
import 'package:algolia_client_search/src/model/sort_remaining_by.dart';
import 'package:algolia_client_search/src/model/source.dart';
import 'package:algolia_client_search/src/model/standard_entries.dart';
import 'package:algolia_client_search/src/model/synonym_hit.dart';
import 'package:algolia_client_search/src/model/synonym_type.dart';
import 'package:algolia_client_search/src/model/task_status.dart';
import 'package:algolia_client_search/src/model/time_range.dart';
import 'package:algolia_client_search/src/model/typo_tolerance_enum.dart';
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
      return Acl.fromJson(value) as ReturnType;
    case 'Action':
      return Action.fromJson(value) as ReturnType;
    case 'AddApiKeyResponse':
      return AddApiKeyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AdvancedSyntaxFeatures':
      return AdvancedSyntaxFeatures.fromJson(value) as ReturnType;
    case 'AlternativesAsExact':
      return AlternativesAsExact.fromJson(value) as ReturnType;
    case 'Anchoring':
      return Anchoring.fromJson(value) as ReturnType;
    case 'ApiKey':
      return ApiKey.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AroundPrecisionFromValueInner':
      return AroundPrecisionFromValueInner.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'AroundRadiusAll':
      return AroundRadiusAll.fromJson(value) as ReturnType;
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
      return BuiltInOperationType.fromJson(value) as ReturnType;
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
      return DictionaryAction.fromJson(value) as ReturnType;
    case 'DictionaryEntry':
      return DictionaryEntry.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionaryEntryState':
      return DictionaryEntryState.fromJson(value) as ReturnType;
    case 'DictionaryLanguage':
      return DictionaryLanguage.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionarySettingsParams':
      return DictionarySettingsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DictionaryType':
      return DictionaryType.fromJson(value) as ReturnType;
    case 'Edit':
      return Edit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EditType':
      return EditType.fromJson(value) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ExactOnSingleWordQuery':
      return ExactOnSingleWordQuery.fromJson(value) as ReturnType;
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
      return LogType.fromJson(value) as ReturnType;
    case 'MatchLevel':
      return MatchLevel.fromJson(value) as ReturnType;
    case 'MatchedGeoLocation':
      return MatchedGeoLocation.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Mode':
      return Mode.fromJson(value) as ReturnType;
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
      return OperationType.fromJson(value) as ReturnType;
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
      return RemoveWordsIfNoResults.fromJson(value) as ReturnType;
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
      return ScopeType.fromJson(value) as ReturnType;
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
      return SearchStrategy.fromJson(value) as ReturnType;
    case 'SearchSynonymsParams':
      return SearchSynonymsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchSynonymsResponse':
      return SearchSynonymsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchTypeDefault':
      return SearchTypeDefault.fromJson(value) as ReturnType;
    case 'SearchTypeFacet':
      return SearchTypeFacet.fromJson(value) as ReturnType;
    case 'SearchUserIdsParams':
      return SearchUserIdsParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchUserIdsResponse':
      return SearchUserIdsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SemanticSearch':
      return SemanticSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SnippetResultOption':
      return SnippetResultOption.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SortRemainingBy':
      return SortRemainingBy.fromJson(value) as ReturnType;
    case 'Source':
      return Source.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'StandardEntries':
      return StandardEntries.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SynonymHit':
      return SynonymHit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SynonymType':
      return SynonymType.fromJson(value) as ReturnType;
    case 'TaskStatus':
      return TaskStatus.fromJson(value) as ReturnType;
    case 'TimeRange':
      return TimeRange.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TypoToleranceEnum':
      return TypoToleranceEnum.fromJson(value) as ReturnType;
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
      if (targetType == 'Object') {
        return value;
      }
      break;
  }
  throw Exception('Cannot deserialize');
}
