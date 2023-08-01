// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'schedule_date_utils_input.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ScheduleDateUtilsInput _$ScheduleDateUtilsInputFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ScheduleDateUtilsInput',
      json,
      ($checkedConvert) {
        final val = ScheduleDateUtilsInput(
          timeframe: $checkedConvert('timeframe', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$ScheduleDateUtilsInputToJson(
        ScheduleDateUtilsInput instance) =>
    <String, dynamic>{
      'timeframe': instance.timeframe,
    };
