// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_hit_with_analytics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopHitWithAnalytics _$TopHitWithAnalyticsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'TopHitWithAnalytics',
      json,
      ($checkedConvert) {
        final val = TopHitWithAnalytics(
          hit: $checkedConvert('hit', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
          clickThroughRate:
              $checkedConvert('clickThroughRate', (v) => (v as num).toDouble()),
          conversionRate:
              $checkedConvert('conversionRate', (v) => (v as num).toDouble()),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          conversionCount: $checkedConvert('conversionCount', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopHitWithAnalyticsToJson(
        TopHitWithAnalytics instance) =>
    <String, dynamic>{
      'hit': instance.hit,
      'count': instance.count,
      'clickThroughRate': instance.clickThroughRate,
      'conversionRate': instance.conversionRate,
      'trackedSearchCount': instance.trackedSearchCount,
      'clickCount': instance.clickCount,
      'conversionCount': instance.conversionCount,
    };
