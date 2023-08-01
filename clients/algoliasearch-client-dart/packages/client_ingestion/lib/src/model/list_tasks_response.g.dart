// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_tasks_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListTasksResponse _$ListTasksResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListTasksResponse',
      json,
      ($checkedConvert) {
        final val = ListTasksResponse(
          tasks: $checkedConvert(
              'tasks',
              (v) => (v as List<dynamic>)
                  .map((e) => Task.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListTasksResponseToJson(ListTasksResponse instance) =>
    <String, dynamic>{
      'tasks': instance.tasks.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
