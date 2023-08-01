// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'error_base.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ErrorBase _$ErrorBaseFromJson(Map<String, dynamic> json) => $checkedCreate(
      'ErrorBase',
      json,
      ($checkedConvert) {
        final val = ErrorBase(
          message: $checkedConvert('message', (v) => v as String?),
        );
        return val;
      },
    );

const _$ErrorBaseFieldMap = <String, String>{
  'message': 'message',
};

Map<String, dynamic> _$ErrorBaseToJson(ErrorBase instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('message', instance.message);
  return val;
}
