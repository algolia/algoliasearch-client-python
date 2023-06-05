// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'replace_source_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ReplaceSourceResponse _$ReplaceSourceResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ReplaceSourceResponse',
      json,
      ($checkedConvert) {
        final val = ReplaceSourceResponse(
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$ReplaceSourceResponseToJson(
        ReplaceSourceResponse instance) =>
    <String, dynamic>{
      'updatedAt': instance.updatedAt,
    };
