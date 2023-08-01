// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_index_prefix.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationIndexPrefix _$DestinationIndexPrefixFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationIndexPrefix',
      json,
      ($checkedConvert) {
        final val = DestinationIndexPrefix(
          indexPrefix: $checkedConvert('indexPrefix', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationIndexPrefixToJson(
        DestinationIndexPrefix instance) =>
    <String, dynamic>{
      'indexPrefix': instance.indexPrefix,
    };
