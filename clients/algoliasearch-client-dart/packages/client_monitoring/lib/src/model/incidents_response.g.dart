// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'incidents_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

IncidentsResponse _$IncidentsResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'IncidentsResponse',
      json,
      ($checkedConvert) {
        final val = IncidentsResponse(
          incidents: $checkedConvert(
              'incidents',
              (v) => (v as Map<String, dynamic>?)?.map(
                    (k, e) => MapEntry(
                        k,
                        (e as List<dynamic>)
                            .map((e) => IncidentsInner.fromJson(
                                e as Map<String, dynamic>))
                            .toList()),
                  )),
        );
        return val;
      },
    );

Map<String, dynamic> _$IncidentsResponseToJson(IncidentsResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'incidents',
      instance.incidents
          ?.map((k, e) => MapEntry(k, e.map((e) => e.toJson()).toList())));
  return val;
}
