// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_click_positions_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetClickPositionsResponse _$GetClickPositionsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetClickPositionsResponse',
      json,
      ($checkedConvert) {
        final val = GetClickPositionsResponse(
          positions: $checkedConvert(
              'positions',
              (v) => (v as List<dynamic>)
                  .map((e) => ClickPosition.fromJson(e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetClickPositionsResponseToJson(
        GetClickPositionsResponse instance) =>
    <String, dynamic>{
      'positions': instance.positions.map((e) => e.toJson()).toList(),
    };
