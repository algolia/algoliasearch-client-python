// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'updated_at_with_object_id_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UpdatedAtWithObjectIdResponse _$UpdatedAtWithObjectIdResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'UpdatedAtWithObjectIdResponse',
      json,
      ($checkedConvert) {
        final val = UpdatedAtWithObjectIdResponse(
          taskID: $checkedConvert('taskID', (v) => v as int?),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String?),
          objectID: $checkedConvert('objectID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$UpdatedAtWithObjectIdResponseToJson(
    UpdatedAtWithObjectIdResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('taskID', instance.taskID);
  writeNotNull('updatedAt', instance.updatedAt);
  writeNotNull('objectID', instance.objectID);
  return val;
}
