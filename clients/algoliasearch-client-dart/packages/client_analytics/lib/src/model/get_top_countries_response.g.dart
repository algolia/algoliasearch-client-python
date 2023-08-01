// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_countries_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopCountriesResponse _$GetTopCountriesResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopCountriesResponse',
      json,
      ($checkedConvert) {
        final val = GetTopCountriesResponse(
          countries: $checkedConvert(
              'countries',
              (v) => (v as List<dynamic>)
                  .map((e) => TopCountry.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopCountriesResponseToJson(
        GetTopCountriesResponse instance) =>
    <String, dynamic>{
      'countries': instance.countries.map((e) => e.toJson()).toList(),
    };
