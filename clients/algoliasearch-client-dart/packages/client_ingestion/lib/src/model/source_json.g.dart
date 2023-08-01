// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_json.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceJSON _$SourceJSONFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SourceJSON',
      json,
      ($checkedConvert) {
        final val = SourceJSON(
          url: $checkedConvert('url', (v) => v as String),
          uniqueIDColumn:
              $checkedConvert('uniqueIDColumn', (v) => v as String?),
          method: $checkedConvert(
              'method', (v) => $enumDecodeNullable(_$MethodTypeEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceJSONToJson(SourceJSON instance) {
  final val = <String, dynamic>{
    'url': instance.url,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('uniqueIDColumn', instance.uniqueIDColumn);
  writeNotNull('method', instance.method?.toJson());
  return val;
}

const _$MethodTypeEnumMap = {
  MethodType.get: 'GET',
  MethodType.post: 'POST',
};
