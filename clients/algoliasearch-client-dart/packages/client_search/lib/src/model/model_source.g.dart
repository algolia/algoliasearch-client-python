// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model_source.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelSource _$ModelSourceFromJson(Map<String, dynamic> json) => $checkedCreate(
      'ModelSource',
      json,
      ($checkedConvert) {
        final val = ModelSource(
          source_: $checkedConvert('source', (v) => v as String),
          description: $checkedConvert('description', (v) => v as String?),
        );
        return val;
      },
      fieldKeyMap: const {'source_': 'source'},
    );

Map<String, dynamic> _$ModelSourceToJson(ModelSource instance) {
  final val = <String, dynamic>{
    'source': instance.source_,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('description', instance.description);
  return val;
}
