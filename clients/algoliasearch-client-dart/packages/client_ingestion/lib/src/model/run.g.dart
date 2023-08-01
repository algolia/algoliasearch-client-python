// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'run.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Run _$RunFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Run',
      json,
      ($checkedConvert) {
        final val = Run(
          runID: $checkedConvert('runID', (v) => v as String),
          appID: $checkedConvert('appID', (v) => v as String),
          taskID: $checkedConvert('taskID', (v) => v as String),
          status: $checkedConvert(
              'status', (v) => $enumDecode(_$RunStatusEnumMap, v)),
          progress: $checkedConvert(
              'progress',
              (v) => v == null
                  ? null
                  : RunProgress.fromJson(v as Map<String, dynamic>)),
          outcome: $checkedConvert(
              'outcome', (v) => $enumDecodeNullable(_$RunOutcomeEnumMap, v)),
          reason: $checkedConvert('reason', (v) => v as String?),
          reasonCode: $checkedConvert('reasonCode',
              (v) => $enumDecodeNullable(_$RunReasonCodeEnumMap, v)),
          type:
              $checkedConvert('type', (v) => $enumDecode(_$RunTypeEnumMap, v)),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          startedAt: $checkedConvert('startedAt', (v) => v as String?),
          finishedAt: $checkedConvert('finishedAt', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$RunToJson(Run instance) {
  final val = <String, dynamic>{
    'runID': instance.runID,
    'appID': instance.appID,
    'taskID': instance.taskID,
    'status': instance.status.toJson(),
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('progress', instance.progress?.toJson());
  writeNotNull('outcome', instance.outcome?.toJson());
  writeNotNull('reason', instance.reason);
  writeNotNull('reasonCode', instance.reasonCode?.toJson());
  val['type'] = instance.type.toJson();
  val['createdAt'] = instance.createdAt;
  writeNotNull('startedAt', instance.startedAt);
  writeNotNull('finishedAt', instance.finishedAt);
  return val;
}

const _$RunStatusEnumMap = {
  RunStatus.created: 'created',
  RunStatus.started: 'started',
  RunStatus.idled: 'idled',
  RunStatus.finished: 'finished',
  RunStatus.skipped: 'skipped',
};

const _$RunOutcomeEnumMap = {
  RunOutcome.success: 'success',
  RunOutcome.failure: 'failure',
  RunOutcome.processing: 'processing',
};

const _$RunReasonCodeEnumMap = {
  RunReasonCode.internal: 'internal',
  RunReasonCode.critical: 'critical',
  RunReasonCode.noEvents: 'no_events',
  RunReasonCode.tooManyErrors: 'too_many_errors',
  RunReasonCode.ok: 'ok',
  RunReasonCode.discarded: 'discarded',
  RunReasonCode.blocking: 'blocking',
};

const _$RunTypeEnumMap = {
  RunType.reindex: 'reindex',
  RunType.update: 'update',
};
