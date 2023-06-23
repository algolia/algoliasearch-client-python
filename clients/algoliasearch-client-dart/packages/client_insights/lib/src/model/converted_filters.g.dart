// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'converted_filters.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ConvertedFilters _$ConvertedFiltersFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ConvertedFilters',
      json,
      ($checkedConvert) {
        final val = ConvertedFilters(
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$ConversionEventEnumMap, v)),
          index: $checkedConvert('index', (v) => v as String),
          filters: $checkedConvert('filters',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ConvertedFiltersToJson(ConvertedFilters instance) {
  final val = <String, dynamic>{
    'eventName': instance.eventName,
    'eventType': instance.eventType.toJson(),
    'index': instance.index,
    'filters': instance.filters,
    'userToken': instance.userToken,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('timestamp', instance.timestamp);
  return val;
}

const _$ConversionEventEnumMap = {
  ConversionEvent.conversion: 'conversion',
};
