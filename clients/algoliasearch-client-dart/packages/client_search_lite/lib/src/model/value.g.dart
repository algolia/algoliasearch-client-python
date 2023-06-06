// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'value.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Value _$ValueFromJson(Map<String, dynamic> json) => Value(
      order:
          (json['order'] as List<dynamic>?)?.map((e) => e as String).toList(),
      sortRemainingBy: $enumDecodeNullable(
          _$SortRemainingByEnumMap, json['sortRemainingBy']),
    );

Map<String, dynamic> _$ValueToJson(Value instance) => <String, dynamic>{
      'order': instance.order,
      'sortRemainingBy': _$SortRemainingByEnumMap[instance.sortRemainingBy],
    };

const _$SortRemainingByEnumMap = {
  SortRemainingBy.count: 'count',
  SortRemainingBy.alpha: 'alpha',
  SortRemainingBy.hidden: 'hidden',
};
