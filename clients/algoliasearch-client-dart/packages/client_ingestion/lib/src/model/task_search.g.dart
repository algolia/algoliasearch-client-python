// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TaskSearch _$TaskSearchFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TaskSearch',
      json,
      ($checkedConvert) {
        final val = TaskSearch(
          taskIDs: $checkedConvert('taskIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TaskSearchToJson(TaskSearch instance) =>
    <String, dynamic>{
      'taskIDs': instance.taskIDs,
    };
