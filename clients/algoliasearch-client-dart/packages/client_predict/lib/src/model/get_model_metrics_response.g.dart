// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_model_metrics_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetModelMetricsResponse _$GetModelMetricsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetModelMetricsResponse',
      json,
      ($checkedConvert) {
        final val = GetModelMetricsResponse(
          modelID: $checkedConvert('modelID', (v) => v as String),
          metrics: $checkedConvert(
              'metrics',
              (v) => (v as List<dynamic>)
                  .map((e) => ModelMetrics.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetModelMetricsResponseToJson(
        GetModelMetricsResponse instance) =>
    <String, dynamic>{
      'modelID': instance.modelID,
      'metrics': instance.metrics.map((e) => e.toJson()).toList(),
    };
