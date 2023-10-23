// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'purchased_object_ids_after_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PurchasedObjectIDsAfterSearch _$PurchasedObjectIDsAfterSearchFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PurchasedObjectIDsAfterSearch',
      json,
      ($checkedConvert) {
        final val = PurchasedObjectIDsAfterSearch(
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$ConversionEventEnumMap, v)),
          eventSubtype: $checkedConvert(
              'eventSubtype', (v) => $enumDecode(_$PurchaseEventEnumMap, v)),
          index: $checkedConvert('index', (v) => v as String),
          queryID: $checkedConvert('queryID', (v) => v as String),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          objectData: $checkedConvert(
              'objectData',
              (v) => (v as List<dynamic>?)
                  ?.map((e) =>
                      ObjectDataAfterSearch.fromJson(e as Map<String, dynamic>))
                  .toList()),
          currency: $checkedConvert('currency', (v) => v as String?),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
          authenticatedUserToken:
              $checkedConvert('authenticatedUserToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$PurchasedObjectIDsAfterSearchToJson(
    PurchasedObjectIDsAfterSearch instance) {
  final val = <String, dynamic>{
    'eventName': instance.eventName,
    'eventType': instance.eventType.toJson(),
    'eventSubtype': instance.eventSubtype.toJson(),
    'index': instance.index,
    'queryID': instance.queryID,
    'objectIDs': instance.objectIDs,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'objectData', instance.objectData?.map((e) => e.toJson()).toList());
  writeNotNull('currency', instance.currency);
  val['userToken'] = instance.userToken;
  writeNotNull('timestamp', instance.timestamp);
  writeNotNull('authenticatedUserToken', instance.authenticatedUserToken);
  return val;
}

const _$ConversionEventEnumMap = {
  ConversionEvent.conversion: 'conversion',
};

const _$PurchaseEventEnumMap = {
  PurchaseEvent.purchase: 'purchase',
};
