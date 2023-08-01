// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'segments.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Segments _$SegmentsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Segments',
      json,
      ($checkedConvert) {
        final val = Segments(
          computed: $checkedConvert('computed',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          custom: $checkedConvert('custom',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SegmentsToJson(Segments instance) => <String, dynamic>{
      'computed': instance.computed,
      'custom': instance.custom,
    };
