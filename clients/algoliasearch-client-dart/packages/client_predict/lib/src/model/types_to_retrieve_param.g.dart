// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'types_to_retrieve_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TypesToRetrieveParam _$TypesToRetrieveParamFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'TypesToRetrieveParam',
      json,
      ($checkedConvert) {
        final val = TypesToRetrieveParam(
          typesToRetrieve: $checkedConvert(
              'typesToRetrieve',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => $enumDecode(_$TypesToRetrieveEnumMap, e))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$TypesToRetrieveParamToJson(
    TypesToRetrieveParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('typesToRetrieve',
      instance.typesToRetrieve?.map((e) => e.toJson()).toList());
  return val;
}

const _$TypesToRetrieveEnumMap = {
  TypesToRetrieve.properties: 'properties',
  TypesToRetrieve.segments: 'segments',
};
