// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'api_key.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ApiKey _$ApiKeyFromJson(Map<String, dynamic> json) => $checkedCreate(
      'ApiKey',
      json,
      ($checkedConvert) {
        final val = ApiKey(
          acl: $checkedConvert(
              'acl',
              (v) => (v as List<dynamic>)
                  .map((e) => $enumDecode(_$AclEnumMap, e))
                  .toList()),
          description: $checkedConvert('description', (v) => v as String?),
          indexes: $checkedConvert('indexes',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          maxHitsPerQuery: $checkedConvert('maxHitsPerQuery', (v) => v as int?),
          maxQueriesPerIPPerHour:
              $checkedConvert('maxQueriesPerIPPerHour', (v) => v as int?),
          queryParameters:
              $checkedConvert('queryParameters', (v) => v as String?),
          referers: $checkedConvert('referers',
              (v) => (v as List<dynamic>?)?.map((e) => e as String).toList()),
          validity: $checkedConvert('validity', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ApiKeyToJson(ApiKey instance) {
  final val = <String, dynamic>{
    'acl': instance.acl.map((e) => e.toJson()).toList(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('description', instance.description);
  writeNotNull('indexes', instance.indexes);
  writeNotNull('maxHitsPerQuery', instance.maxHitsPerQuery);
  writeNotNull('maxQueriesPerIPPerHour', instance.maxQueriesPerIPPerHour);
  writeNotNull('queryParameters', instance.queryParameters);
  writeNotNull('referers', instance.referers);
  writeNotNull('validity', instance.validity);
  return val;
}

const _$AclEnumMap = {
  Acl.addObject: 'addObject',
  Acl.analytics: 'analytics',
  Acl.browse: 'browse',
  Acl.deleteObject: 'deleteObject',
  Acl.deleteIndex: 'deleteIndex',
  Acl.editSettings: 'editSettings',
  Acl.listIndexes: 'listIndexes',
  Acl.logs: 'logs',
  Acl.personalization: 'personalization',
  Acl.recommendation: 'recommendation',
  Acl.search: 'search',
  Acl.seeUnretrievableAttributes: 'seeUnretrievableAttributes',
  Acl.settings: 'settings',
  Acl.usage: 'usage',
};
