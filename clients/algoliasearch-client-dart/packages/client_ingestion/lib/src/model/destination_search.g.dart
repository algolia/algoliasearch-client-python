// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationSearch _$DestinationSearchFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationSearch',
      json,
      ($checkedConvert) {
        final val = DestinationSearch(
          destinationIDs: $checkedConvert('destinationIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationSearchToJson(DestinationSearch instance) =>
    <String, dynamic>{
      'destinationIDs': instance.destinationIDs,
    };
