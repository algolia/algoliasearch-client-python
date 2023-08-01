// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'top_country.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TopCountry _$TopCountryFromJson(Map<String, dynamic> json) => $checkedCreate(
      'TopCountry',
      json,
      ($checkedConvert) {
        final val = TopCountry(
          country: $checkedConvert('country', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$TopCountryToJson(TopCountry instance) =>
    <String, dynamic>{
      'country': instance.country,
      'count': instance.count,
    };
