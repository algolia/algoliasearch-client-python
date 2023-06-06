// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'fetched_index.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FetchedIndex _$FetchedIndexFromJson(Map<String, dynamic> json) => FetchedIndex(
      name: json['name'] as String,
      createdAt: json['createdAt'] as String,
      updatedAt: json['updatedAt'] as String,
      entries: json['entries'] as int,
      dataSize: json['dataSize'] as int,
      fileSize: json['fileSize'] as int,
      lastBuildTimeS: json['lastBuildTimeS'] as int,
      numberOfPendingTasks: json['numberOfPendingTasks'] as int,
      pendingTask: json['pendingTask'] as bool,
      primary: json['primary'] as String?,
      replicas: (json['replicas'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
    );

Map<String, dynamic> _$FetchedIndexToJson(FetchedIndex instance) =>
    <String, dynamic>{
      'name': instance.name,
      'createdAt': instance.createdAt,
      'updatedAt': instance.updatedAt,
      'entries': instance.entries,
      'dataSize': instance.dataSize,
      'fileSize': instance.fileSize,
      'lastBuildTimeS': instance.lastBuildTimeS,
      'numberOfPendingTasks': instance.numberOfPendingTasks,
      'pendingTask': instance.pendingTask,
      'primary': instance.primary,
      'replicas': instance.replicas,
    };
