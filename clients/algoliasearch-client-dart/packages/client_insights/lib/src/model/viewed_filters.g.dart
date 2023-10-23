// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'viewed_filters.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ViewedFilters _$ViewedFiltersFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ViewedFilters',
      json,
      ($checkedConvert) {
        final val = ViewedFilters(
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$ViewEventEnumMap, v)),
          index: $checkedConvert('index', (v) => v as String),
          filters: $checkedConvert('filters',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
          authenticatedUserToken:
              $checkedConvert('authenticatedUserToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ViewedFiltersToJson(ViewedFilters instance) {
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
  writeNotNull('authenticatedUserToken', instance.authenticatedUserToken);
  return val;
}

const _$ViewEventEnumMap = {
  ViewEvent.view: 'view',
};
