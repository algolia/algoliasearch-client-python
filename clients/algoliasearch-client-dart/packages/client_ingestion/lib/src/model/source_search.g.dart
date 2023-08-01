// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_search.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceSearch _$SourceSearchFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceSearch',
      json,
      ($checkedConvert) {
        final val = SourceSearch(
          sourceIDs: $checkedConvert('sourceIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceSearchToJson(SourceSearch instance) =>
    <String, dynamic>{
      'sourceIDs': instance.sourceIDs,
    };
