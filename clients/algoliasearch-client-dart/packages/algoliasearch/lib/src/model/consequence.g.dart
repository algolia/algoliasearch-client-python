// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'consequence.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Consequence _$ConsequenceFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Consequence',
      json,
      ($checkedConvert) {
        final val = Consequence(
          params: $checkedConvert(
              'params',
              (v) => v == null
                  ? null
                  : ConsequenceParams.fromJson(v as Map<String, dynamic>)),
          promote: $checkedConvert('promote', (v) => v as List<dynamic>?),
          filterPromotes: $checkedConvert('filterPromotes', (v) => v as bool?),
          hide_: $checkedConvert(
              'hide',
              (v) => (v as List<dynamic>?)
                  ?.map((e) =>
                      ConsequenceHide.fromJson(e as Map<String, dynamic>))
                  .toList()),
          userData: $checkedConvert('userData', (v) => v),
        );
        return val;
      },
      fieldKeyMap: const {'hide_': 'hide'},
    );

Map<String, dynamic> _$ConsequenceToJson(Consequence instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('params', instance.params?.toJson());
  writeNotNull('promote', instance.promote?.toList());
  writeNotNull('filterPromotes', instance.filterPromotes);
  writeNotNull('hide', instance.hide_?.map((e) => e.toJson()).toList());
  writeNotNull('userData', instance.userData);
  return val;
}
