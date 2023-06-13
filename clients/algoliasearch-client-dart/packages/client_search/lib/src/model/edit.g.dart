// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'edit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Edit _$EditFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Edit',
      json,
      ($checkedConvert) {
        final val = Edit(
          type: $checkedConvert(
              'type', (v) => $enumDecodeNullable(_$EditTypeEnumMap, v)),
          delete: $checkedConvert('delete', (v) => v as String?),
          insert: $checkedConvert('insert', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$EditToJson(Edit instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('type', instance.type?.toJson());
  writeNotNull('delete', instance.delete);
  writeNotNull('insert', instance.insert);
  return val;
}

const _$EditTypeEnumMap = {
  EditType.remove: 'remove',
  EditType.replace: 'replace',
};
