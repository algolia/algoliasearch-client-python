// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'limit_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

LimitParam _$LimitParamFromJson(Map<String, dynamic> json) => $checkedCreate(
      'LimitParam',
      json,
      ($checkedConvert) {
        final val = LimitParam(
          limit: $checkedConvert('limit', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$LimitParamToJson(LimitParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('limit', instance.limit);
  return val;
}
