// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_indices_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListIndicesResponse _$ListIndicesResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ListIndicesResponse',
      json,
      ($checkedConvert) {
        final val = ListIndicesResponse(
          items: $checkedConvert(
              'items',
              (v) => (v as List<dynamic>)
                  .map((e) => FetchedIndex.fromJson(e as Map<String, dynamic>))
                  .toList()),
          nbPages: $checkedConvert('nbPages', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListIndicesResponseToJson(ListIndicesResponse instance) {
  final val = <String, dynamic>{
    'items': instance.items.map((e) => e.toJson()).toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('nbPages', instance.nbPages);
  return val;
}
