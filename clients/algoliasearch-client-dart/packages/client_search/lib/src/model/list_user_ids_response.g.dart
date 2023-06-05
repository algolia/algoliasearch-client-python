// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_user_ids_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListUserIdsResponse _$ListUserIdsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListUserIdsResponse',
      json,
      ($checkedConvert) {
        final val = ListUserIdsResponse(
          userIDs: $checkedConvert(
              'userIDs',
              (v) => (v as List<dynamic>)
                  .map((e) => UserId.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListUserIdsResponseToJson(
        ListUserIdsResponse instance) =>
    <String, dynamic>{
      'userIDs': instance.userIDs.map((e) => e.toJson()).toList(),
    };
