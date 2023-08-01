// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_csv.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceCSV _$SourceCSVFromJson(Map<String, dynamic> json) => $checkedCreate(
      'SourceCSV',
      json,
      ($checkedConvert) {
        final val = SourceCSV(
          url: $checkedConvert('url', (v) => v as String),
          uniqueIDColumn:
              $checkedConvert('uniqueIDColumn', (v) => v as String?),
          mapping: $checkedConvert(
              'mapping',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) =>
                        MapEntry(k, $enumDecode(_$MappingTypeCSVEnumMap, e)),
                  )),
          method: $checkedConvert(
              'method', (v) => $enumDecodeNullable(_$MethodTypeEnumMap, v)),
          delimiter: $checkedConvert('delimiter', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceCSVToJson(SourceCSV instance) {
  final val = <String, dynamic>{
    'url': instance.url,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('uniqueIDColumn', instance.uniqueIDColumn);
  writeNotNull(
      'mapping', instance.mapping?.map((k, e) => MapEntry(k, e.toJson())));
  writeNotNull('method', instance.method?.toJson());
  writeNotNull('delimiter', instance.delimiter);
  return val;
}

const _$MappingTypeCSVEnumMap = {
  MappingTypeCSV.string: 'string',
  MappingTypeCSV.integer: 'integer',
  MappingTypeCSV.float: 'float',
  MappingTypeCSV.boolean: 'boolean',
  MappingTypeCSV.json: 'json',
};

const _$MethodTypeEnumMap = {
  MethodType.get: 'GET',
  MethodType.post: 'POST',
};
