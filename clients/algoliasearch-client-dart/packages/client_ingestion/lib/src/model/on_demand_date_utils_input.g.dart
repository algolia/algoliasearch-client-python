// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'on_demand_date_utils_input.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

OnDemandDateUtilsInput _$OnDemandDateUtilsInputFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'OnDemandDateUtilsInput',
      json,
      ($checkedConvert) {
        final val = OnDemandDateUtilsInput(
          startDate: $checkedConvert('startDate', (v) => v as String),
          endDate: $checkedConvert('endDate', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$OnDemandDateUtilsInputToJson(
        OnDemandDateUtilsInput instance) =>
    <String, dynamic>{
      'startDate': instance.startDate,
      'endDate': instance.endDate,
    };
