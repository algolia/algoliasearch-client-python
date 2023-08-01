import 'package:algolia_client_abtesting/src/model/ab_test.dart';
import 'package:algolia_client_abtesting/src/model/ab_test_response.dart';
import 'package:algolia_client_abtesting/src/model/ab_tests_variant.dart';
import 'package:algolia_client_abtesting/src/model/ab_tests_variant_search_params.dart';
import 'package:algolia_client_abtesting/src/model/add_ab_tests_request.dart';
import 'package:algolia_client_abtesting/src/model/custom_search_params.dart';
import 'package:algolia_client_abtesting/src/model/error_base.dart';
import 'package:algolia_client_abtesting/src/model/list_ab_tests_response.dart';
import 'package:algolia_client_abtesting/src/model/variant.dart';

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
    case 'ABTest':
      return ABTest.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ABTestResponse':
      return ABTestResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AbTestsVariant':
      return AbTestsVariant.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AbTestsVariantSearchParams':
      return AbTestsVariantSearchParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AddABTestsRequest':
      return AddABTestsRequest.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'CustomSearchParams':
      return CustomSearchParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ListABTestsResponse':
      return ListABTestsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Variant':
      return Variant.fromJson(value as Map<String, dynamic>) as ReturnType;
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
