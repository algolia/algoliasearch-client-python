// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_big_query.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceBigQuery _$SourceBigQueryFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceBigQuery',
      json,
      ($checkedConvert) {
        final val = SourceBigQuery(
          projectID: $checkedConvert('projectID', (v) => v as String),
          datasetID: $checkedConvert('datasetID', (v) => v as String),
          dataType: $checkedConvert('dataType',
              (v) => $enumDecodeNullable(_$BigQueryDataTypeEnumMap, v)),
          table: $checkedConvert('table', (v) => v as String?),
          tablePrefix: $checkedConvert('tablePrefix', (v) => v as String?),
          customSQLRequest:
              $checkedConvert('customSQLRequest', (v) => v as String?),
          uniqueIDColumn:
              $checkedConvert('uniqueIDColumn', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceBigQueryToJson(SourceBigQuery instance) {
  final val = <String, dynamic>{
    'projectID': instance.projectID,
    'datasetID': instance.datasetID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('dataType', instance.dataType?.toJson());
  writeNotNull('table', instance.table);
  writeNotNull('tablePrefix', instance.tablePrefix);
  writeNotNull('customSQLRequest', instance.customSQLRequest);
  writeNotNull('uniqueIDColumn', instance.uniqueIDColumn);
  return val;
}

const _$BigQueryDataTypeEnumMap = {
  BigQueryDataType.ga4: 'ga4',
  BigQueryDataType.ga360: 'ga360',
};
