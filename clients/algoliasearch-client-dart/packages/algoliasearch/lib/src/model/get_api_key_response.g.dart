// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetApiKeyResponse _$GetApiKeyResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'GetApiKeyResponse',
      json,
      ($checkedConvert) {
        final val = GetApiKeyResponse(
          value: $checkedConvert('value', (v) => v as String?),
          createdAt: $checkedConvert('createdAt', (v) => v as int),
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

Map<String, dynamic> _$GetApiKeyResponseToJson(GetApiKeyResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('value', instance.value);
  val['createdAt'] = instance.createdAt;
  val['acl'] = instance.acl.map((e) => _$AclEnumMap[e]!).toList();
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
