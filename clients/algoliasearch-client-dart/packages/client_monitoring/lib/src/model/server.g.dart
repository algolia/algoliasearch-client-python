// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'server.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Server _$ServerFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Server',
      json,
      ($checkedConvert) {
        final val = Server(
          name: $checkedConvert('name', (v) => v as String?),
          region: $checkedConvert(
              'region', (v) => $enumDecodeNullable(_$RegionEnumMap, v)),
          isSlave: $checkedConvert('is_slave', (v) => v as bool?),
          isReplica: $checkedConvert('is_replica', (v) => v as bool?),
          cluster: $checkedConvert('cluster', (v) => v as String?),
          status: $checkedConvert(
              'status', (v) => $enumDecodeNullable(_$ServerStatusEnumMap, v)),
          type: $checkedConvert(
              'type', (v) => $enumDecodeNullable(_$TypeEnumMap, v)),
        );
        return val;
      },
      fieldKeyMap: const {'isSlave': 'is_slave', 'isReplica': 'is_replica'},
    );

Map<String, dynamic> _$ServerToJson(Server instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('name', instance.name);
  writeNotNull('region', instance.region?.toJson());
  writeNotNull('is_slave', instance.isSlave);
  writeNotNull('is_replica', instance.isReplica);
  writeNotNull('cluster', instance.cluster);
  writeNotNull('status', instance.status?.toJson());
  writeNotNull('type', instance.type?.toJson());
  return val;
}

const _$RegionEnumMap = {
  Region.au: 'au',
  Region.br: 'br',
  Region.ca: 'ca',
  Region.de: 'de',
  Region.eu: 'eu',
  Region.hk: 'hk',
  Region.in_: 'in',
  Region.jp: 'jp',
  Region.sg: 'sg',
  Region.uae: 'uae',
  Region.uk: 'uk',
  Region.usc: 'usc',
  Region.use: 'use',
  Region.usw: 'usw',
  Region.za: 'za',
};

const _$ServerStatusEnumMap = {
  ServerStatus.production: 'PRODUCTION',
};

const _$TypeEnumMap = {
  Type.cluster: 'cluster',
};
