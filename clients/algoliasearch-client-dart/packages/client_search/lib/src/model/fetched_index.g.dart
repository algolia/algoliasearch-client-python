// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'fetched_index.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FetchedIndex _$FetchedIndexFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'FetchedIndex',
      json,
      ($checkedConvert) {
        final val = FetchedIndex(
          name: $checkedConvert('name', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
          entries: $checkedConvert('entries', (v) => v as int),
          dataSize: $checkedConvert('dataSize', (v) => v as int),
          fileSize: $checkedConvert('fileSize', (v) => v as int),
          lastBuildTimeS: $checkedConvert('lastBuildTimeS', (v) => v as int),
          numberOfPendingTasks:
              $checkedConvert('numberOfPendingTasks', (v) => v as int),
          pendingTask: $checkedConvert('pendingTask', (v) => v as bool),
          primary: $checkedConvert('primary', (v) => v as String?),
          replicas: $checkedConvert('replicas',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$FetchedIndexToJson(FetchedIndex instance) {
  final val = <String, dynamic>{
    'name': instance.name,
    'createdAt': instance.createdAt,
    'updatedAt': instance.updatedAt,
    'entries': instance.entries,
    'dataSize': instance.dataSize,
    'fileSize': instance.fileSize,
    'lastBuildTimeS': instance.lastBuildTimeS,
    'numberOfPendingTasks': instance.numberOfPendingTasks,
    'pendingTask': instance.pendingTask,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('primary', instance.primary);
  writeNotNull('replicas', instance.replicas);
  return val;
}
