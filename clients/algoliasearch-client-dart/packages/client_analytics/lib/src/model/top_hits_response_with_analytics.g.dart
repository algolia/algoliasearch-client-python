// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_hits_response_with_analytics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopHitsResponseWithAnalytics _$TopHitsResponseWithAnalyticsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'TopHitsResponseWithAnalytics',
      json,
      ($checkedConvert) {
        final val = TopHitsResponseWithAnalytics(
          hits: $checkedConvert(
              'hits',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      TopHitWithAnalytics.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopHitsResponseWithAnalyticsToJson(
        TopHitsResponseWithAnalytics instance) =>
    <String, dynamic>{
      'hits': instance.hits.map((e) => e.toJson()).toList(),
    };
