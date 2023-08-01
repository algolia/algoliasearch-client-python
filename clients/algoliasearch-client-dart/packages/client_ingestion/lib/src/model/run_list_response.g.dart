// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'run_list_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RunListResponse _$RunListResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'RunListResponse',
      json,
      ($checkedConvert) {
        final val = RunListResponse(
          runs: $checkedConvert(
              'runs',
              (v) => (v as List<dynamic>)
                  .map((e) => Run.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$RunListResponseToJson(RunListResponse instance) =>
    <String, dynamic>{
      'runs': instance.runs.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
