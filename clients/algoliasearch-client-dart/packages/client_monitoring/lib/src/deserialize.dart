import 'package:algolia_client_monitoring/src/model/error_base.dart';
import 'package:algolia_client_monitoring/src/model/get_inventory403_response.dart';
import 'package:algolia_client_monitoring/src/model/incident.dart';
import 'package:algolia_client_monitoring/src/model/incidents_inner.dart';
import 'package:algolia_client_monitoring/src/model/incidents_response.dart';
import 'package:algolia_client_monitoring/src/model/indexing_time_response.dart';
import 'package:algolia_client_monitoring/src/model/indexing_time_response_metrics.dart';
import 'package:algolia_client_monitoring/src/model/infrastructure_response.dart';
import 'package:algolia_client_monitoring/src/model/infrastructure_response_metrics.dart';
import 'package:algolia_client_monitoring/src/model/inventory_response.dart';
import 'package:algolia_client_monitoring/src/model/latency_response.dart';
import 'package:algolia_client_monitoring/src/model/latency_response_metrics.dart';
import 'package:algolia_client_monitoring/src/model/metric.dart';
import 'package:algolia_client_monitoring/src/model/period.dart';
import 'package:algolia_client_monitoring/src/model/probes_metric.dart';
import 'package:algolia_client_monitoring/src/model/region.dart';
import 'package:algolia_client_monitoring/src/model/server.dart';
import 'package:algolia_client_monitoring/src/model/server_status.dart';
import 'package:algolia_client_monitoring/src/model/status.dart';
import 'package:algolia_client_monitoring/src/model/status_response.dart';
import 'package:algolia_client_monitoring/src/model/time_inner.dart';
import 'package:algolia_client_monitoring/src/model/type.dart';

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
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetInventory403Response':
      return GetInventory403Response.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Incident':
      return Incident.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'IncidentsInner':
      return IncidentsInner.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IncidentsResponse':
      return IncidentsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IndexingTimeResponse':
      return IndexingTimeResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'IndexingTimeResponseMetrics':
      return IndexingTimeResponseMetrics.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'InfrastructureResponse':
      return InfrastructureResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'InfrastructureResponseMetrics':
      return InfrastructureResponseMetrics.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'InventoryResponse':
      return InventoryResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'LatencyResponse':
      return LatencyResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'LatencyResponseMetrics':
      return LatencyResponseMetrics.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Metric':
      return Metric.fromJson(value) as ReturnType;
    case 'Period':
      return Period.fromJson(value) as ReturnType;
    case 'ProbesMetric':
      return ProbesMetric.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Region':
      return Region.fromJson(value) as ReturnType;
    case 'Server':
      return Server.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ServerStatus':
      return ServerStatus.fromJson(value) as ReturnType;
    case 'Status':
      return Status.fromJson(value) as ReturnType;
    case 'StatusResponse':
      return StatusResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TimeInner':
      return TimeInner.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Type':
      return Type.fromJson(value) as ReturnType;
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
