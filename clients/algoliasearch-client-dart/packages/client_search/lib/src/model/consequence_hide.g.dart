// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'consequence_hide.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ConsequenceHide _$ConsequenceHideFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ConsequenceHide',
      json,
      ($checkedConvert) {
        final val = ConsequenceHide(
          objectID: $checkedConvert('objectID', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ConsequenceHideToJson(ConsequenceHide instance) =>
    <String, dynamic>{
      'objectID': instance.objectID,
    };
