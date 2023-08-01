import 'package:algolia_client_personalization/src/model/delete_user_profile_response.dart';
import 'package:algolia_client_personalization/src/model/error_base.dart';
import 'package:algolia_client_personalization/src/model/event_scoring.dart';
import 'package:algolia_client_personalization/src/model/facet_scoring.dart';
import 'package:algolia_client_personalization/src/model/get_user_token_response.dart';
import 'package:algolia_client_personalization/src/model/personalization_strategy_params.dart';
import 'package:algolia_client_personalization/src/model/set_personalization_strategy_response.dart';

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
    case 'DeleteUserProfileResponse':
      return DeleteUserProfileResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EventScoring':
      return EventScoring.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FacetScoring':
      return FacetScoring.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetUserTokenResponse':
      return GetUserTokenResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'PersonalizationStrategyParams':
      return PersonalizationStrategyParams.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'SetPersonalizationStrategyResponse':
      return SetPersonalizationStrategyResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
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
