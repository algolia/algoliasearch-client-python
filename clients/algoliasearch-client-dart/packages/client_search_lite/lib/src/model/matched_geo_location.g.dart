// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'matched_geo_location.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

MatchedGeoLocation _$MatchedGeoLocationFromJson(Map<String, dynamic> json) =>
    MatchedGeoLocation(
      lat: (json['lat'] as num?)?.toDouble(),
      lng: (json['lng'] as num?)?.toDouble(),
      distance: json['distance'] as int?,
    );

Map<String, dynamic> _$MatchedGeoLocationToJson(MatchedGeoLocation instance) =>
    <String, dynamic>{
      'lat': instance.lat,
      'lng': instance.lng,
      'distance': instance.distance,
    };
