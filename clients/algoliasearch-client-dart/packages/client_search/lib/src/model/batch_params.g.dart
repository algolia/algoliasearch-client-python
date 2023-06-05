// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchParams _$BatchParamsFromJson(Map<String, dynamic> json) => $checkedCreate(
      'BatchParams',
      json,
      ($checkedConvert) {
        final val = BatchParams(
          requests: $checkedConvert(
              'requests',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      MultipleBatchRequest.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchParamsToJson(BatchParams instance) =>
    <String, dynamic>{
      'requests': instance.requests.map((e) => e.toJson()).toList(),
    };
