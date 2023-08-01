import 'package:algolia_client_analytics/src/model/average_click_event.dart';
import 'package:algolia_client_analytics/src/model/click_position.dart';
import 'package:algolia_client_analytics/src/model/click_through_rate_event.dart';
import 'package:algolia_client_analytics/src/model/conversion_rate_event.dart';
import 'package:algolia_client_analytics/src/model/direction.dart';
import 'package:algolia_client_analytics/src/model/error_base.dart';
import 'package:algolia_client_analytics/src/model/get_average_click_position_response.dart';
import 'package:algolia_client_analytics/src/model/get_click_positions_response.dart';
import 'package:algolia_client_analytics/src/model/get_click_through_rate_response.dart';
import 'package:algolia_client_analytics/src/model/get_conversation_rate_response.dart';
import 'package:algolia_client_analytics/src/model/get_no_click_rate_response.dart';
import 'package:algolia_client_analytics/src/model/get_no_results_rate_response.dart';
import 'package:algolia_client_analytics/src/model/get_searches_count_response.dart';
import 'package:algolia_client_analytics/src/model/get_searches_no_clicks_response.dart';
import 'package:algolia_client_analytics/src/model/get_searches_no_results_response.dart';
import 'package:algolia_client_analytics/src/model/get_status_response.dart';
import 'package:algolia_client_analytics/src/model/get_top_countries_response.dart';
import 'package:algolia_client_analytics/src/model/get_top_filter_attribute.dart';
import 'package:algolia_client_analytics/src/model/get_top_filter_attributes_response.dart';
import 'package:algolia_client_analytics/src/model/get_top_filter_for_attribute.dart';
import 'package:algolia_client_analytics/src/model/get_top_filter_for_attribute_response.dart';
import 'package:algolia_client_analytics/src/model/get_top_filters_no_results_response.dart';
import 'package:algolia_client_analytics/src/model/get_top_filters_no_results_value.dart';
import 'package:algolia_client_analytics/src/model/get_top_filters_no_results_values.dart';
import 'package:algolia_client_analytics/src/model/get_users_count_response.dart';
import 'package:algolia_client_analytics/src/model/no_click_rate_event.dart';
import 'package:algolia_client_analytics/src/model/no_results_rate_event.dart';
import 'package:algolia_client_analytics/src/model/order_by.dart';
import 'package:algolia_client_analytics/src/model/search_event.dart';
import 'package:algolia_client_analytics/src/model/search_no_click_event.dart';
import 'package:algolia_client_analytics/src/model/search_no_result_event.dart';
import 'package:algolia_client_analytics/src/model/top_country.dart';
import 'package:algolia_client_analytics/src/model/top_hit.dart';
import 'package:algolia_client_analytics/src/model/top_hit_with_analytics.dart';
import 'package:algolia_client_analytics/src/model/top_hits_response.dart';
import 'package:algolia_client_analytics/src/model/top_hits_response_with_analytics.dart';
import 'package:algolia_client_analytics/src/model/top_search.dart';
import 'package:algolia_client_analytics/src/model/top_search_with_analytics.dart';
import 'package:algolia_client_analytics/src/model/top_searches_response.dart';
import 'package:algolia_client_analytics/src/model/top_searches_response_with_analytics.dart';
import 'package:algolia_client_analytics/src/model/user_with_date.dart';

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
    case 'AverageClickEvent':
      return AverageClickEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ClickPosition':
      return ClickPosition.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ClickThroughRateEvent':
      return ClickThroughRateEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConversionRateEvent':
      return ConversionRateEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Direction':
      return Direction.fromJson(value) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetAverageClickPositionResponse':
      return GetAverageClickPositionResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetClickPositionsResponse':
      return GetClickPositionsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetClickThroughRateResponse':
      return GetClickThroughRateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetConversationRateResponse':
      return GetConversationRateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetNoClickRateResponse':
      return GetNoClickRateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetNoResultsRateResponse':
      return GetNoResultsRateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetSearchesCountResponse':
      return GetSearchesCountResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetSearchesNoClicksResponse':
      return GetSearchesNoClicksResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetSearchesNoResultsResponse':
      return GetSearchesNoResultsResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetStatusResponse':
      return GetStatusResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopCountriesResponse':
      return GetTopCountriesResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopFilterAttribute':
      return GetTopFilterAttribute.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopFilterAttributesResponse':
      return GetTopFilterAttributesResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetTopFilterForAttribute':
      return GetTopFilterForAttribute.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopFilterForAttributeResponse':
      return GetTopFilterForAttributeResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetTopFiltersNoResultsResponse':
      return GetTopFiltersNoResultsResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetTopFiltersNoResultsValue':
      return GetTopFiltersNoResultsValue.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetTopFiltersNoResultsValues':
      return GetTopFiltersNoResultsValues.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetUsersCountResponse':
      return GetUsersCountResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'NoClickRateEvent':
      return NoClickRateEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'NoResultsRateEvent':
      return NoResultsRateEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OrderBy':
      return OrderBy.fromJson(value) as ReturnType;
    case 'SearchEvent':
      return SearchEvent.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SearchNoClickEvent':
      return SearchNoClickEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SearchNoResultEvent':
      return SearchNoResultEvent.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TopCountry':
      return TopCountry.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TopHit':
      return TopHit.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TopHitWithAnalytics':
      return TopHitWithAnalytics.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TopHitsResponse':
      return TopHitsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TopHitsResponseWithAnalytics':
      return TopHitsResponseWithAnalytics.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'TopSearch':
      return TopSearch.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TopSearchWithAnalytics':
      return TopSearchWithAnalytics.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TopSearchesResponse':
      return TopSearchesResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TopSearchesResponseWithAnalytics':
      return TopSearchesResponseWithAnalytics.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'UserWithDate':
      return UserWithDate.fromJson(value as Map<String, dynamic>) as ReturnType;
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
