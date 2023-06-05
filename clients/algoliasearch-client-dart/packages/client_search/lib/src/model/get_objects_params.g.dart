// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_objects_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetObjectsParams _$GetObjectsParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetObjectsParams',
      json,
      ($checkedConvert) {
        final val = GetObjectsParams(
          requests: $checkedConvert(
              'requests',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      GetObjectsRequest.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetObjectsParamsToJson(GetObjectsParams instance) =>
    <String, dynamic>{
      'requests': instance.requests.map((e) => e.toJson()).toList(),
    };
