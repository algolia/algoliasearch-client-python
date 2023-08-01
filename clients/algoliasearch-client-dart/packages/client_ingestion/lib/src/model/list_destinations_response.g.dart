// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_destinations_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListDestinationsResponse _$ListDestinationsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ListDestinationsResponse',
      json,
      ($checkedConvert) {
        final val = ListDestinationsResponse(
          destinations: $checkedConvert(
              'destinations',
              (v) => (v as List<dynamic>)
                  .map((e) => Destination.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListDestinationsResponseToJson(
        ListDestinationsResponse instance) =>
    <String, dynamic>{
      'destinations': instance.destinations.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
