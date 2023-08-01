// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_hits_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopHitsResponse _$TopHitsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TopHitsResponse',
      json,
      ($checkedConvert) {
        final val = TopHitsResponse(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) => TopHit.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopHitsResponseToJson(TopHitsResponse instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
    };
