import 'package:algolia_client_insights/src/model/add_to_cart_event.dart';
import 'package:algolia_client_insights/src/model/added_to_cart_object_ids.dart';
import 'package:algolia_client_insights/src/model/added_to_cart_object_ids_after_search.dart';
import 'package:algolia_client_insights/src/model/click_event.dart';
import 'package:algolia_client_insights/src/model/clicked_filters.dart';
import 'package:algolia_client_insights/src/model/clicked_object_ids.dart';
import 'package:algolia_client_insights/src/model/clicked_object_ids_after_search.dart';
import 'package:algolia_client_insights/src/model/conversion_event.dart';
import 'package:algolia_client_insights/src/model/converted_filters.dart';
import 'package:algolia_client_insights/src/model/converted_object_ids.dart';
import 'package:algolia_client_insights/src/model/converted_object_ids_after_search.dart';
import 'package:algolia_client_insights/src/model/error_base.dart';
import 'package:algolia_client_insights/src/model/events_response.dart';
import 'package:algolia_client_insights/src/model/insights_events.dart';
import 'package:algolia_client_insights/src/model/object_data.dart';
import 'package:algolia_client_insights/src/model/object_data_after_search.dart';
import 'package:algolia_client_insights/src/model/purchase_event.dart';
import 'package:algolia_client_insights/src/model/purchased_object_ids.dart';
import 'package:algolia_client_insights/src/model/purchased_object_ids_after_search.dart';
import 'package:algolia_client_insights/src/model/view_event.dart';
import 'package:algolia_client_insights/src/model/viewed_filters.dart';
import 'package:algolia_client_insights/src/model/viewed_object_ids.dart';

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
    case 'AddToCartEvent':
      return AddToCartEvent.fromJson(value) as ReturnType;
    case 'AddedToCartObjectIDs':
      return AddedToCartObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AddedToCartObjectIDsAfterSearch':
      return AddedToCartObjectIDsAfterSearch.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'ClickEvent':
      return ClickEvent.fromJson(value) as ReturnType;
    case 'ClickedFilters':
      return ClickedFilters.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ClickedObjectIDs':
      return ClickedObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ClickedObjectIDsAfterSearch':
      return ClickedObjectIDsAfterSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConversionEvent':
      return ConversionEvent.fromJson(value) as ReturnType;
    case 'ConvertedFilters':
      return ConvertedFilters.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConvertedObjectIDs':
      return ConvertedObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ConvertedObjectIDsAfterSearch':
      return ConvertedObjectIDsAfterSearch.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EventsResponse':
      return EventsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'InsightsEvents':
      return InsightsEvents.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ObjectData':
      return ObjectData.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ObjectDataAfterSearch':
      return ObjectDataAfterSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'PurchaseEvent':
      return PurchaseEvent.fromJson(value) as ReturnType;
    case 'PurchasedObjectIDs':
      return PurchasedObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'PurchasedObjectIDsAfterSearch':
      return PurchasedObjectIDsAfterSearch.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'ViewEvent':
      return ViewEvent.fromJson(value) as ReturnType;
    case 'ViewedFilters':
      return ViewedFilters.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ViewedObjectIDs':
      return ViewedObjectIDs.fromJson(value as Map<String, dynamic>)
          as ReturnType;
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
