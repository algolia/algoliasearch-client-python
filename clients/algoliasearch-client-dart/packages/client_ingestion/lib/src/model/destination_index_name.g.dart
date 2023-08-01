// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_index_name.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationIndexName _$DestinationIndexNameFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationIndexName',
      json,
      ($checkedConvert) {
        final val = DestinationIndexName(
          indexName: $checkedConvert('indexName', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationIndexNameToJson(
        DestinationIndexName instance) =>
    <String, dynamic>{
      'indexName': instance.indexName,
    };
