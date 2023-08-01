// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'click_position.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ClickPosition _$ClickPositionFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ClickPosition',
      json,
      ($checkedConvert) {
        final val = ClickPosition(
          position: $checkedConvert('position',
              (v) => (v as List<dynamic>).map((e) => e as int).toList()),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$ClickPositionToJson(ClickPosition instance) =>
    <String, dynamic>{
      'position': instance.position,
      'clickCount': instance.clickCount,
    };
