// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_users_count_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetUsersCountResponse _$GetUsersCountResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetUsersCountResponse',
      json,
      ($checkedConvert) {
        final val = GetUsersCountResponse(
          count: $checkedConvert('count', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) => UserWithDate.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetUsersCountResponseToJson(
        GetUsersCountResponse instance) =>
    <String, dynamic>{
      'count': instance.count,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
