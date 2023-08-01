// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_profile.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserProfile _$UserProfileFromJson(Map<String, dynamic> json) => $checkedCreate(
      'UserProfile',
      json,
      ($checkedConvert) {
        final val = UserProfile(
          user: $checkedConvert('user', (v) => v as String),
          predictions: $checkedConvert(
              'predictions',
              (v) => v == null
                  ? null
                  : Predictions.fromJson(v as Map<String, dynamic>)),
          properties: $checkedConvert(
              'properties',
              (v) => v == null
                  ? null
                  : Properties.fromJson(v as Map<String, dynamic>)),
          segments: $checkedConvert(
              'segments',
              (v) => v == null
                  ? null
                  : Segments.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$UserProfileToJson(UserProfile instance) {
  final val = <String, dynamic>{
    'user': instance.user,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('predictions', instance.predictions?.toJson());
  writeNotNull('properties', instance.properties?.toJson());
  writeNotNull('segments', instance.segments?.toJson());
  return val;
}
