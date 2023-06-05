// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_clusters_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListClustersResponse _$ListClustersResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ListClustersResponse',
      json,
      ($checkedConvert) {
        final val = ListClustersResponse(
          topUsers: $checkedConvert('topUsers',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListClustersResponseToJson(
        ListClustersResponse instance) =>
    <String, dynamic>{
      'topUsers': instance.topUsers,
    };
