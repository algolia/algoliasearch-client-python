// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ab_test.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ABTest _$ABTestFromJson(Map<String, dynamic> json) => $checkedCreate(
      'ABTest',
      json,
      ($checkedConvert) {
        final val = ABTest(
          abTestID: $checkedConvert('abTestID', (v) => v as int),
          clickSignificance: $checkedConvert(
              'clickSignificance', (v) => (v as num).toDouble()),
          conversionSignificance:
              $checkedConvert('conversionSignificance', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          name: $checkedConvert('name', (v) => v as String),
          status: $checkedConvert('status', (v) => v as String),
          variants: $checkedConvert(
              'variants',
              (v) => (v as List<dynamic>)
                  .map((e) => Variant.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ABTestToJson(ABTest instance) => <String, dynamic>{
      'abTestID': instance.abTestID,
      'clickSignificance': instance.clickSignificance,
      'conversionSignificance': instance.conversionSignificance,
      'updatedAt': instance.updatedAt,
      'createdAt': instance.createdAt,
      'name': instance.name,
      'status': instance.status,
      'variants': instance.variants.map((e) => e.toJson()).toList(),
    };
