// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model_source.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ModelSource _$ModelSourceFromJson(Map<String, dynamic> json) => ModelSource(
      source_: json['source'] as String,
      description: json['description'] as String?,
    );

Map<String, dynamic> _$ModelSourceToJson(ModelSource instance) =>
    <String, dynamic>{
      'source': instance.source_,
      'description': instance.description,
    };
