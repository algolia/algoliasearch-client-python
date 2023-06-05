// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'save_object_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SaveObjectResponse _$SaveObjectResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SaveObjectResponse',
      json,
      ($checkedConvert) {
        final val = SaveObjectResponse(
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          taskID: $checkedConvert('taskID', (v) => v as int),
          objectID: $checkedConvert('objectID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$SaveObjectResponseToJson(SaveObjectResponse instance) {
  final val = <String, dynamic>{
    'createdAt': instance.createdAt,
    'taskID': instance.taskID,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('objectID', instance.objectID);
  return val;
}
