// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'has_pending_mappings_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

HasPendingMappingsResponse _$HasPendingMappingsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'HasPendingMappingsResponse',
      json,
      ($checkedConvert) {
        final val = HasPendingMappingsResponse(
          pending: $checkedConvert('pending', (v) => v as bool),
          clusters: $checkedConvert(
              'clusters',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(k,
                        (e as List<dynamic>).map((e) => e as String).toList()),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$HasPendingMappingsResponseToJson(
    HasPendingMappingsResponse instance) {
  final val = <String, dynamic>{
    'pending': instance.pending,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('clusters', instance.clusters);
  return val;
}
