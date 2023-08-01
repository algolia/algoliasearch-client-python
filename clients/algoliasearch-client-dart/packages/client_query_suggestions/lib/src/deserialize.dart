import 'package:algolia_client_query_suggestions/src/model/base_response.dart';
import 'package:algolia_client_query_suggestions/src/model/error_base.dart';
import 'package:algolia_client_query_suggestions/src/model/facet.dart';
import 'package:algolia_client_query_suggestions/src/model/get_config_status200_response.dart';
import 'package:algolia_client_query_suggestions/src/model/get_log_file200_response.dart';
import 'package:algolia_client_query_suggestions/src/model/log_level.dart';
import 'package:algolia_client_query_suggestions/src/model/query_suggestions_configuration.dart';
import 'package:algolia_client_query_suggestions/src/model/query_suggestions_configuration_response.dart';
import 'package:algolia_client_query_suggestions/src/model/query_suggestions_configuration_response_all_of.dart';
import 'package:algolia_client_query_suggestions/src/model/query_suggestions_configuration_with_index.dart';
import 'package:algolia_client_query_suggestions/src/model/query_suggestions_configuration_with_index_all_of.dart';
import 'package:algolia_client_query_suggestions/src/model/source_index.dart';

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
    case 'BaseResponse':
      return BaseResponse.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Facet':
      return Facet.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetConfigStatus200Response':
      return GetConfigStatus200Response.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetLogFile200Response':
      return GetLogFile200Response.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'LogLevel':
      return LogLevel.fromJson(value) as ReturnType;
    case 'QuerySuggestionsConfiguration':
      return QuerySuggestionsConfiguration.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'QuerySuggestionsConfigurationResponse':
      return QuerySuggestionsConfigurationResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'QuerySuggestionsConfigurationResponseAllOf':
      return QuerySuggestionsConfigurationResponseAllOf.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'QuerySuggestionsConfigurationWithIndex':
      return QuerySuggestionsConfigurationWithIndex.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'QuerySuggestionsConfigurationWithIndexAllOf':
      return QuerySuggestionsConfigurationWithIndexAllOf.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'SourceIndex':
      return SourceIndex.fromJson(value as Map<String, dynamic>) as ReturnType;
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
