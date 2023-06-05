// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_objects_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetObjectsRequest _$GetObjectsRequestFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetObjectsRequest',
      json,
      ($checkedConvert) {
        final val = GetObjectsRequest(
          attributesToRetrieve: $checkedConvert('attributesToRetrieve',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          objectID: $checkedConvert('objectID', (v) => v as String),
          indexName: $checkedConvert('indexName', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetObjectsRequestToJson(GetObjectsRequest instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('attributesToRetrieve', instance.attributesToRetrieve);
  val['objectID'] = instance.objectID;
  val['indexName'] = instance.indexName;
  return val;
}
