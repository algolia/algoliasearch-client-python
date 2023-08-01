// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_recommendations_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetRecommendationsResponse _$GetRecommendationsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetRecommendationsResponse',
      json,
      ($checkedConvert) {
        final val = GetRecommendationsResponse(
          results: $checkedConvert(
              'results',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => RecommendationsResponse.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetRecommendationsResponseToJson(
    GetRecommendationsResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('results', instance.results?.map((e) => e.toJson()).toList());
  return val;
}
