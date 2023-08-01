// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_hit.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopHit _$TopHitFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TopHit',
      json,
      ($checkedConvert) {
        final val = TopHit(
          hit: $checkedConvert('hit', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopHitToJson(TopHit instance) => <String, dynamic>{
      'hit': instance.hit,
      'count': instance.count,
    };
