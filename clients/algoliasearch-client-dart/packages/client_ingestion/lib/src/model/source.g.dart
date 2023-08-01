// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Source _$SourceFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Source',
      json,
      ($checkedConvert) {
        final val = Source(
          sourceID: $checkedConvert('sourceID', (v) => v as String),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$SourceTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String),
          input: $checkedConvert('input', (v) => v),
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String?),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceToJson(Source instance) {
  final val = <String, dynamic>{
    'sourceID': instance.sourceID,
    'type': instance.type.toJson(),
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('input', instance.input);
  writeNotNull('authenticationID', instance.authenticationID);
  val['createdAt'] = instance.createdAt;
  writeNotNull('updatedAt', instance.updatedAt);
  return val;
}

const _$SourceTypeEnumMap = {
  SourceType.bigcommerce: 'bigcommerce',
  SourceType.commercetools: 'commercetools',
  SourceType.json: 'json',
  SourceType.csv: 'csv',
  SourceType.bigquery: 'bigquery',
  SourceType.docker: 'docker',
};
