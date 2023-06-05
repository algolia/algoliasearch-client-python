// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'insight_event.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InsightEvent _$InsightEventFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'InsightEvent',
      json,
      ($checkedConvert) {
        final val = InsightEvent(
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$EventTypeEnumMap, v)),
          eventName: $checkedConvert('eventName', (v) => v as String),
          index: $checkedConvert('index', (v) => v as String),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
          queryID: $checkedConvert('queryID', (v) => v as String?),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          filters: $checkedConvert('filters',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          positions: $checkedConvert('positions',
              (v) => (v as List<dynamic>?)?.map((e) => e as int).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$InsightEventToJson(InsightEvent instance) {
  final val = <String, dynamic>{
    'eventType': _$EventTypeEnumMap[instance.eventType]!,
    'eventName': instance.eventName,
    'index': instance.index,
    'userToken': instance.userToken,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('timestamp', instance.timestamp);
  writeNotNull('queryID', instance.queryID);
  writeNotNull('objectIDs', instance.objectIDs);
  writeNotNull('filters', instance.filters);
  writeNotNull('positions', instance.positions);
  return val;
}

const _$EventTypeEnumMap = {
  EventType.click: 'click',
  EventType.conversion: 'conversion',
  EventType.view: 'view',
};
