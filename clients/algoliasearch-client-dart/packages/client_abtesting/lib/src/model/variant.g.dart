// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'variant.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Variant _$VariantFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Variant',
      json,
      ($checkedConvert) {
        final val = Variant(
          averageClickPosition:
              $checkedConvert('averageClickPosition', (v) => v as int),
          clickCount: $checkedConvert('clickCount', (v) => v as int),
          clickThroughRate:
              $checkedConvert('clickThroughRate', (v) => (v as num).toDouble()),
          conversionCount: $checkedConvert('conversionCount', (v) => v as int),
          conversionRate:
              $checkedConvert('conversionRate', (v) => (v as num).toDouble()),
          description: $checkedConvert('description', (v) => v as String),
          index: $checkedConvert('index', (v) => v as String),
          noResultCount: $checkedConvert('noResultCount', (v) => v as int),
          outlierTrackedSearchesCount:
              $checkedConvert('outlierTrackedSearchesCount', (v) => v as int),
          outlierUsersCount:
              $checkedConvert('outlierUsersCount', (v) => v as int),
          searchCount: $checkedConvert('searchCount', (v) => v as int),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          trafficPercentage:
              $checkedConvert('trafficPercentage', (v) => v as int),
          userCount: $checkedConvert('userCount', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$VariantToJson(Variant instance) => <String, dynamic>{
      'averageClickPosition': instance.averageClickPosition,
      'clickCount': instance.clickCount,
      'clickThroughRate': instance.clickThroughRate,
      'conversionCount': instance.conversionCount,
      'conversionRate': instance.conversionRate,
      'description': instance.description,
      'index': instance.index,
      'noResultCount': instance.noResultCount,
      'outlierTrackedSearchesCount': instance.outlierTrackedSearchesCount,
      'outlierUsersCount': instance.outlierUsersCount,
      'searchCount': instance.searchCount,
      'trackedSearchCount': instance.trackedSearchCount,
      'trafficPercentage': instance.trafficPercentage,
      'userCount': instance.userCount,
    };
