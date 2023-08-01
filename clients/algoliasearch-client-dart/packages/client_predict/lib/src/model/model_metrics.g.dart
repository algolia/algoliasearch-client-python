// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model_metrics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelMetrics _$ModelMetricsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ModelMetrics',
      json,
      ($checkedConvert) {
        final val = ModelMetrics(
          precision:
              $checkedConvert('precision', (v) => (v as num?)?.toDouble()),
          recall: $checkedConvert('recall', (v) => (v as num?)?.toDouble()),
          mrr: $checkedConvert('mrr', (v) => (v as num?)?.toDouble()),
          coverage: $checkedConvert('coverage', (v) => (v as num?)?.toDouble()),
          f1Score: $checkedConvert('f1_score', (v) => (v as num?)?.toDouble()),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String?),
        );
        return val;
      },
      fieldKeyMap: const {'f1Score': 'f1_score'},
    );

Map<String, dynamic> _$ModelMetricsToJson(ModelMetrics instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('precision', instance.precision);
  writeNotNull('recall', instance.recall);
  writeNotNull('mrr', instance.mrr);
  writeNotNull('coverage', instance.coverage);
  writeNotNull('f1_score', instance.f1Score);
  writeNotNull('updatedAt', instance.updatedAt);
  return val;
}
