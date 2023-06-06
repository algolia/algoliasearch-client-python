// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'value.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Value _$ValueFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Value',
      json,
      ($checkedConvert) {
        final val = Value(
          order: $checkedConvert('order',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          sortRemainingBy: $checkedConvert('sortRemainingBy',
              (v) => $enumDecodeNullable(_$SortRemainingByEnumMap, v)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ValueToJson(Value instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('order', instance.order);
  writeNotNull(
      'sortRemainingBy', _$SortRemainingByEnumMap[instance.sortRemainingBy]);
  return val;
}

const _$SortRemainingByEnumMap = {
  SortRemainingBy.count: 'count',
  SortRemainingBy.alpha: 'alpha',
  SortRemainingBy.hidden: 'hidden',
};
