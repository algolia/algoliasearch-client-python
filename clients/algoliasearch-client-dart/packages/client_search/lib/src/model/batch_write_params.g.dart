// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_write_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchWriteParams _$BatchWriteParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BatchWriteParams',
      json,
      ($checkedConvert) {
        final val = BatchWriteParams(
          requests: $checkedConvert(
              'requests',
              (v) => (v as List<dynamic>)
                  .map((e) => BatchRequest.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchWriteParamsToJson(BatchWriteParams instance) =>
    <String, dynamic>{
      'requests': instance.requests.map((e) => e.toJson()).toList(),
    };
