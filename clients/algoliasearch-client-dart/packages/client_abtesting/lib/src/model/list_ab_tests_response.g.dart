// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_ab_tests_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListABTestsResponse _$ListABTestsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListABTestsResponse',
      json,
      ($checkedConvert) {
        final val = ListABTestsResponse(
          abtests: $checkedConvert(
              'abtests',
              (v) => (v as List<dynamic>)
                  .map((e) => ABTest.fromJson(e as Map<String, dynamic>))
                  .toList()),
          count: $checkedConvert('count', (v) => v as int),
          total: $checkedConvert('total', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListABTestsResponseToJson(
        ListABTestsResponse instance) =>
    <String, dynamic>{
      'abtests': instance.abtests.map((e) => e.toJson()).toList(),
      'count': instance.count,
      'total': instance.total,
    };
