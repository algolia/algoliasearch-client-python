// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_searches_response_with_analytics.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopSearchesResponseWithAnalytics _$TopSearchesResponseWithAnalyticsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'TopSearchesResponseWithAnalytics',
      json,
      ($checkedConvert) {
        final val = TopSearchesResponseWithAnalytics(
          searches: $checkedConvert(
              'searches',
              (v) => (v as List<dynamic>)
                  .map((e) => TopSearchWithAnalytics.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopSearchesResponseWithAnalyticsToJson(
        TopSearchesResponseWithAnalytics instance) =>
    <String, dynamic>{
      'searches': instance.searches.map((e) => e.toJson()).toList(),
    };
