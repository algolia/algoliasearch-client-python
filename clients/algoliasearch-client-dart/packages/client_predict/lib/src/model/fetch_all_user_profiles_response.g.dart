// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'fetch_all_user_profiles_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FetchAllUserProfilesResponse _$FetchAllUserProfilesResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'FetchAllUserProfilesResponse',
      json,
      ($checkedConvert) {
        final val = FetchAllUserProfilesResponse(
          users: $checkedConvert(
              'users',
              (v) => (v as List<dynamic>)
                  .map((e) => UserProfile.fromJson(e as Map<String, dynamic>))
                  .toList()),
          previousPageToken:
              $checkedConvert('previousPageToken', (v) => v as String?),
          nextPageToken: $checkedConvert('nextPageToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$FetchAllUserProfilesResponseToJson(
    FetchAllUserProfilesResponse instance) {
  final val = <String, dynamic>{
    'users': instance.users.map((e) => e.toJson()).toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('previousPageToken', instance.previousPageToken);
  writeNotNull('nextPageToken', instance.nextPageToken);
  return val;
}
