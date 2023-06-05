// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_top_user_ids_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetTopUserIdsResponse _$GetTopUserIdsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetTopUserIdsResponse',
      json,
      ($checkedConvert) {
        final val = GetTopUserIdsResponse(
          topUsers: $checkedConvert(
              'topUsers',
              (v) => (v as List<dynamic>)
                  .map((e) => (e as Map<String, dynamic>).map(
                        (k, e) => MapEntry(
                            k,
                            (e as List<dynamic>)
                                .map((e) =>
                                    UserId.fromJson(e as Map<String, dynamic>))
                                .toList()),
                      ))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetTopUserIdsResponseToJson(
        GetTopUserIdsResponse instance) =>
    <String, dynamic>{
      'topUsers': instance.topUsers
          .map((e) =>
              e.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())))
          .toList(),
    };
