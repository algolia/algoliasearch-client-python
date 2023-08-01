// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_update.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceUpdate _$SourceUpdateFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceUpdate',
      json,
      ($checkedConvert) {
        final val = SourceUpdate(
          name: $checkedConvert('name', (v) => v as String?),
          input: $checkedConvert('input', (v) => v),
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceUpdateToJson(SourceUpdate instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('name', instance.name);
  writeNotNull('input', instance.input);
  writeNotNull('authenticationID', instance.authenticationID);
  return val;
}
