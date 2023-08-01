// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'facet.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Facet _$FacetFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Facet',
      json,
      ($checkedConvert) {
        final val = Facet(
          attribute: $checkedConvert('attribute', (v) => v as String?),
          amount: $checkedConvert('amount', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$FacetToJson(Facet instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('attribute', instance.attribute);
  writeNotNull('amount', instance.amount);
  return val;
}
