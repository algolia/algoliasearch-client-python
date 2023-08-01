// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'delete_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DeleteResponse _$DeleteResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DeleteResponse',
      json,
      ($checkedConvert) {
        final val = DeleteResponse(
          deletedAt: $checkedConvert('deletedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DeleteResponseToJson(DeleteResponse instance) =>
    <String, dynamic>{
      'deletedAt': instance.deletedAt,
    };
