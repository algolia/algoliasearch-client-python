// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'created_at_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

CreatedAtResponse _$CreatedAtResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'CreatedAtResponse',
      json,
      ($checkedConvert) {
        final val = CreatedAtResponse(
          createdAt: $checkedConvert('createdAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$CreatedAtResponseToJson(CreatedAtResponse instance) =>
    <String, dynamic>{
      'createdAt': instance.createdAt,
    };
