// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'source_docker.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

SourceDocker _$SourceDockerFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'SourceDocker',
      json,
      ($checkedConvert) {
        final val = SourceDocker(
          registry: $checkedConvert(
              'registry', (v) => $enumDecode(_$DockerRegistryEnumMap, v)),
          image: $checkedConvert('image', (v) => v as String),
          version: $checkedConvert('version', (v) => v as String?),
          imageType: $checkedConvert(
              'imageType', (v) => $enumDecode(_$DockerImageTypeEnumMap, v)),
          outputFile: $checkedConvert('outputFile', (v) => v as String?),
          configuration: $checkedConvert('configuration', (v) => v as Object),
        );
        return val;
      },
    );

Map<String, dynamic> _$SourceDockerToJson(SourceDocker instance) {
  final val = <String, dynamic>{
    'registry': instance.registry.toJson(),
    'image': instance.image,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('version', instance.version);
  val['imageType'] = instance.imageType.toJson();
  writeNotNull('outputFile', instance.outputFile);
  val['configuration'] = instance.configuration;
  return val;
}

const _$DockerRegistryEnumMap = {
  DockerRegistry.dockerhub: 'dockerhub',
  DockerRegistry.ghcr: 'ghcr',
};

const _$DockerImageTypeEnumMap = {
  DockerImageType.singer: 'singer',
  DockerImageType.custom: 'custom',
  DockerImageType.airbyte: 'airbyte',
};
