// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_source_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteSourceResponse _$DeleteSourceResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteSourceResponse',
      json,
      ($checkedConvert) {
        final val = DeleteSourceResponse(
          deletedAt: $checkedConvert('deletedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteSourceResponseToJson(
        DeleteSourceResponse instance) =>
    <String, dynamic>{
      'deletedAt': instance.deletedAt,
    };
