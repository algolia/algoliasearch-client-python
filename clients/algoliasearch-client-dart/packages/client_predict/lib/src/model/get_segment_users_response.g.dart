// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_segment_users_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetSegmentUsersResponse _$GetSegmentUsersResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetSegmentUsersResponse',
      json,
      ($checkedConvert) {
        final val = GetSegmentUsersResponse(
          segmentID: $checkedConvert('segmentID', (v) => v as String),
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

Map<String, dynamic> _$GetSegmentUsersResponseToJson(
    GetSegmentUsersResponse instance) {
  final val = <String, dynamic>{
    'segmentID': instance.segmentID,
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
