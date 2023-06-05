// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facet_hits.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FacetHits _$FacetHitsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'FacetHits',
      json,
      ($checkedConvert) {
        final val = FacetHits(
          value: $checkedConvert('value', (v) => v as String),
          highlighted: $checkedConvert('highlighted', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$FacetHitsToJson(FacetHits instance) => <String, dynamic>{
      'value': instance.value,
      'highlighted': instance.highlighted,
      'count': instance.count,
    };
