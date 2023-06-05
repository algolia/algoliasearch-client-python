// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'matched_geo_location.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

MatchedGeoLocation _$MatchedGeoLocationFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'MatchedGeoLocation',
      json,
      ($checkedConvert) {
        final val = MatchedGeoLocation(
          lat: $checkedConvert('lat', (v) => (v as num?)?.toDouble()),
          lng: $checkedConvert('lng', (v) => (v as num?)?.toDouble()),
          distance: $checkedConvert('distance', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$MatchedGeoLocationToJson(MatchedGeoLocation instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('lat', instance.lat);
  writeNotNull('lng', instance.lng);
  writeNotNull('distance', instance.distance);
  return val;
}
