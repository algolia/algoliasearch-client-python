// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predictions_affinities_success.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PredictionsAffinitiesSuccess _$PredictionsAffinitiesSuccessFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PredictionsAffinitiesSuccess',
      json,
      ($checkedConvert) {
        final val = PredictionsAffinitiesSuccess(
          value: $checkedConvert(
              'value',
              (v) => (v as List<dynamic>)
                  .map((e) => Affinity.fromJson(e as Map<String, dynamic>))
                  .toList()),
          lastUpdatedAt: $checkedConvert('lastUpdatedAt', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$PredictionsAffinitiesSuccessToJson(
        PredictionsAffinitiesSuccess instance) =>
    <String, dynamic>{
      'value': instance.value.map((e) => e.toJson()).toList(),
      'lastUpdatedAt': instance.lastUpdatedAt,
    };
