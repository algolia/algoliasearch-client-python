// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_conversation_rate_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetConversationRateResponse _$GetConversationRateResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetConversationRateResponse',
      json,
      ($checkedConvert) {
        final val = GetConversationRateResponse(
          rate: $checkedConvert('rate', (v) => (v as num).toDouble()),
          trackedSearchCount:
              $checkedConvert('trackedSearchCount', (v) => v as int),
          conversionCount: $checkedConvert('conversionCount', (v) => v as int),
          dates: $checkedConvert(
              'dates',
              (v) => (v as List<dynamic>)
                  .map((e) =>
                      ConversionRateEvent.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetConversationRateResponseToJson(
        GetConversationRateResponse instance) =>
    <String, dynamic>{
      'rate': instance.rate,
      'trackedSearchCount': instance.trackedSearchCount,
      'conversionCount': instance.conversionCount,
      'dates': instance.dates.map((e) => e.toJson()).toList(),
    };
