// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_objects_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetObjectsResponse _$GetObjectsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetObjectsResponse',
      json,
      ($checkedConvert) {
        final val = GetObjectsResponse(
          results: $checkedConvert('results',
              (v) => (v as List<dynamic>).map((e) => e as Object).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetObjectsResponseToJson(GetObjectsResponse instance) =>
    <String, dynamic>{
      'results': instance.results,
    };
