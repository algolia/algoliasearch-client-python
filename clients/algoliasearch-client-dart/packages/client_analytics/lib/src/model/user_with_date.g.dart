// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'user_with_date.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

UserWithDate _$UserWithDateFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'UserWithDate',
      json,
      ($checkedConvert) {
        final val = UserWithDate(
          date: $checkedConvert('date', (v) => v as String),
          count: $checkedConvert('count', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$UserWithDateToJson(UserWithDate instance) =>
    <String, dynamic>{
      'date': instance.date,
      'count': instance.count,
    };
