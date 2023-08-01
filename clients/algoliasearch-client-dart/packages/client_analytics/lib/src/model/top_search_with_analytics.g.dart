// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_search_with_analytics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopSearchWithAnalytics _$TopSearchWithAnalyticsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'TopSearchWithAnalytics',
      json,
      ($checkedConvert) {
        final val = TopSearchWithAnalytics(
          search: $checkedConvert('search', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
          clickThroughRate:
              $checkedConvert('clickThroughRate', (v) => (v as num).toDouble()),
          averageClickPosition:
              $checkedConvert('averageClickPosition', (v) => v as int),
          conversionRate:
              $checkedConvert('conversionRate', (v) => (v as num).toDouble()),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          conversionCount: $checkedConvert('conversionCount', (v) => v as int),
          nbHits: $checkedConvert('nbHits', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopSearchWithAnalyticsToJson(
        TopSearchWithAnalytics instance) =>
    <String, dynamic>{
      'search': instance.search,
      'count': instance.count,
      'clickThroughRate': instance.clickThroughRate,
      'averageClickPosition': instance.averageClickPosition,
      'conversionRate': instance.conversionRate,
      'trackedSearchCount': instance.trackedSearchCount,
      'clickCount': instance.clickCount,
      'conversionCount': instance.conversionCount,
      'nbHits': instance.nbHits,
    };
