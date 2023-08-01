import 'package:algolia_client_ingestion/src/model/action_type.dart';
import 'package:algolia_client_ingestion/src/model/auth_api_key.dart';
import 'package:algolia_client_ingestion/src/model/auth_api_key_partial.dart';
import 'package:algolia_client_ingestion/src/model/auth_algolia.dart';
import 'package:algolia_client_ingestion/src/model/auth_algolia_partial.dart';
import 'package:algolia_client_ingestion/src/model/auth_basic.dart';
import 'package:algolia_client_ingestion/src/model/auth_basic_partial.dart';
import 'package:algolia_client_ingestion/src/model/auth_google_service_account.dart';
import 'package:algolia_client_ingestion/src/model/auth_google_service_account_partial.dart';
import 'package:algolia_client_ingestion/src/model/auth_o_auth.dart';
import 'package:algolia_client_ingestion/src/model/auth_o_auth_partial.dart';
import 'package:algolia_client_ingestion/src/model/authentication.dart';
import 'package:algolia_client_ingestion/src/model/authentication_create.dart';
import 'package:algolia_client_ingestion/src/model/authentication_create_response.dart';
import 'package:algolia_client_ingestion/src/model/authentication_search.dart';
import 'package:algolia_client_ingestion/src/model/authentication_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/authentication_type.dart';
import 'package:algolia_client_ingestion/src/model/authentication_update.dart';
import 'package:algolia_client_ingestion/src/model/authentication_update_response.dart';
import 'package:algolia_client_ingestion/src/model/big_commerce_channel.dart';
import 'package:algolia_client_ingestion/src/model/big_query_data_type.dart';
import 'package:algolia_client_ingestion/src/model/delete_response.dart';
import 'package:algolia_client_ingestion/src/model/destination.dart';
import 'package:algolia_client_ingestion/src/model/destination_create.dart';
import 'package:algolia_client_ingestion/src/model/destination_create_response.dart';
import 'package:algolia_client_ingestion/src/model/destination_index_name.dart';
import 'package:algolia_client_ingestion/src/model/destination_index_prefix.dart';
import 'package:algolia_client_ingestion/src/model/destination_search.dart';
import 'package:algolia_client_ingestion/src/model/destination_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/destination_type.dart';
import 'package:algolia_client_ingestion/src/model/destination_update.dart';
import 'package:algolia_client_ingestion/src/model/destination_update_response.dart';
import 'package:algolia_client_ingestion/src/model/docker_image_type.dart';
import 'package:algolia_client_ingestion/src/model/docker_registry.dart';
import 'package:algolia_client_ingestion/src/model/error_base.dart';
import 'package:algolia_client_ingestion/src/model/event.dart';
import 'package:algolia_client_ingestion/src/model/event_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/event_status.dart';
import 'package:algolia_client_ingestion/src/model/event_type.dart';
import 'package:algolia_client_ingestion/src/model/list_authentications_response.dart';
import 'package:algolia_client_ingestion/src/model/list_destinations_response.dart';
import 'package:algolia_client_ingestion/src/model/list_events_response.dart';
import 'package:algolia_client_ingestion/src/model/list_sources_response.dart';
import 'package:algolia_client_ingestion/src/model/list_tasks_response.dart';
import 'package:algolia_client_ingestion/src/model/mapping_type_csv.dart';
import 'package:algolia_client_ingestion/src/model/method_type.dart';
import 'package:algolia_client_ingestion/src/model/on_demand_date_utils_input.dart';
import 'package:algolia_client_ingestion/src/model/on_demand_trigger.dart';
import 'package:algolia_client_ingestion/src/model/on_demand_trigger_input.dart';
import 'package:algolia_client_ingestion/src/model/on_demand_trigger_type.dart';
import 'package:algolia_client_ingestion/src/model/order_keys.dart';
import 'package:algolia_client_ingestion/src/model/pagination.dart';
import 'package:algolia_client_ingestion/src/model/platform.dart';
import 'package:algolia_client_ingestion/src/model/platform_none.dart';
import 'package:algolia_client_ingestion/src/model/run.dart';
import 'package:algolia_client_ingestion/src/model/run_list_response.dart';
import 'package:algolia_client_ingestion/src/model/run_outcome.dart';
import 'package:algolia_client_ingestion/src/model/run_progress.dart';
import 'package:algolia_client_ingestion/src/model/run_reason_code.dart';
import 'package:algolia_client_ingestion/src/model/run_response.dart';
import 'package:algolia_client_ingestion/src/model/run_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/run_status.dart';
import 'package:algolia_client_ingestion/src/model/run_type.dart';
import 'package:algolia_client_ingestion/src/model/schedule_date_utils_input.dart';
import 'package:algolia_client_ingestion/src/model/schedule_trigger.dart';
import 'package:algolia_client_ingestion/src/model/schedule_trigger_input.dart';
import 'package:algolia_client_ingestion/src/model/schedule_trigger_type.dart';
import 'package:algolia_client_ingestion/src/model/source.dart';
import 'package:algolia_client_ingestion/src/model/source_big_commerce.dart';
import 'package:algolia_client_ingestion/src/model/source_big_query.dart';
import 'package:algolia_client_ingestion/src/model/source_csv.dart';
import 'package:algolia_client_ingestion/src/model/source_commercetools.dart';
import 'package:algolia_client_ingestion/src/model/source_create.dart';
import 'package:algolia_client_ingestion/src/model/source_create_response.dart';
import 'package:algolia_client_ingestion/src/model/source_docker.dart';
import 'package:algolia_client_ingestion/src/model/source_json.dart';
import 'package:algolia_client_ingestion/src/model/source_search.dart';
import 'package:algolia_client_ingestion/src/model/source_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/source_type.dart';
import 'package:algolia_client_ingestion/src/model/source_update.dart';
import 'package:algolia_client_ingestion/src/model/source_update_commercetools.dart';
import 'package:algolia_client_ingestion/src/model/source_update_response.dart';
import 'package:algolia_client_ingestion/src/model/subscription_trigger.dart';
import 'package:algolia_client_ingestion/src/model/subscription_trigger_type.dart';
import 'package:algolia_client_ingestion/src/model/task.dart';
import 'package:algolia_client_ingestion/src/model/task_create.dart';
import 'package:algolia_client_ingestion/src/model/task_create_response.dart';
import 'package:algolia_client_ingestion/src/model/task_search.dart';
import 'package:algolia_client_ingestion/src/model/task_sort_keys.dart';
import 'package:algolia_client_ingestion/src/model/task_update.dart';
import 'package:algolia_client_ingestion/src/model/task_update_response.dart';
import 'package:algolia_client_ingestion/src/model/trigger_input.dart';
import 'package:algolia_client_ingestion/src/model/trigger_type.dart';

final _regList = RegExp(r'^List<(.*)>$');
final _regSet = RegExp(r'^Set<(.*)>$');
final _regMap = RegExp(r'^Map<String,(.*)>$');

ReturnType deserialize<ReturnType, BaseType>(dynamic value, String targetType,
    {bool growable = true}) {
  switch (targetType) {
    case 'String':
      return '$value' as ReturnType;
    case 'int':
      return (value is int ? value : int.parse('$value')) as ReturnType;
    case 'bool':
      if (value is bool) {
        return value as ReturnType;
      }
      final valueString = '$value'.toLowerCase();
      return (valueString == 'true' || valueString == '1') as ReturnType;
    case 'double':
      return (value is double ? value : double.parse('$value')) as ReturnType;
    case 'ActionType':
      return ActionType.fromJson(value) as ReturnType;
    case 'AuthAPIKey':
      return AuthAPIKey.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AuthAPIKeyPartial':
      return AuthAPIKeyPartial.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthAlgolia':
      return AuthAlgolia.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AuthAlgoliaPartial':
      return AuthAlgoliaPartial.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthBasic':
      return AuthBasic.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AuthBasicPartial':
      return AuthBasicPartial.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthGoogleServiceAccount':
      return AuthGoogleServiceAccount.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthGoogleServiceAccountPartial':
      return AuthGoogleServiceAccountPartial.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'AuthOAuth':
      return AuthOAuth.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AuthOAuthPartial':
      return AuthOAuthPartial.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Authentication':
      return Authentication.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthenticationCreate':
      return AuthenticationCreate.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthenticationCreateResponse':
      return AuthenticationCreateResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'AuthenticationSearch':
      return AuthenticationSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthenticationSortKeys':
      return AuthenticationSortKeys.fromJson(value) as ReturnType;
    case 'AuthenticationType':
      return AuthenticationType.fromJson(value) as ReturnType;
    case 'AuthenticationUpdate':
      return AuthenticationUpdate.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'AuthenticationUpdateResponse':
      return AuthenticationUpdateResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'BigCommerceChannel':
      return BigCommerceChannel.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'BigQueryDataType':
      return BigQueryDataType.fromJson(value) as ReturnType;
    case 'DeleteResponse':
      return DeleteResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Destination':
      return Destination.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'DestinationCreate':
      return DestinationCreate.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationCreateResponse':
      return DestinationCreateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationIndexName':
      return DestinationIndexName.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationIndexPrefix':
      return DestinationIndexPrefix.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationSearch':
      return DestinationSearch.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationSortKeys':
      return DestinationSortKeys.fromJson(value) as ReturnType;
    case 'DestinationType':
      return DestinationType.fromJson(value) as ReturnType;
    case 'DestinationUpdate':
      return DestinationUpdate.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DestinationUpdateResponse':
      return DestinationUpdateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DockerImageType':
      return DockerImageType.fromJson(value) as ReturnType;
    case 'DockerRegistry':
      return DockerRegistry.fromJson(value) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Event':
      return Event.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'EventSortKeys':
      return EventSortKeys.fromJson(value) as ReturnType;
    case 'EventStatus':
      return EventStatus.fromJson(value) as ReturnType;
    case 'EventType':
      return EventType.fromJson(value) as ReturnType;
    case 'ListAuthenticationsResponse':
      return ListAuthenticationsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListDestinationsResponse':
      return ListDestinationsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListEventsResponse':
      return ListEventsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListSourcesResponse':
      return ListSourcesResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ListTasksResponse':
      return ListTasksResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'MappingTypeCSV':
      return MappingTypeCSV.fromJson(value) as ReturnType;
    case 'MethodType':
      return MethodType.fromJson(value) as ReturnType;
    case 'OnDemandDateUtilsInput':
      return OnDemandDateUtilsInput.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OnDemandTrigger':
      return OnDemandTrigger.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OnDemandTriggerInput':
      return OnDemandTriggerInput.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'OnDemandTriggerType':
      return OnDemandTriggerType.fromJson(value) as ReturnType;
    case 'OrderKeys':
      return OrderKeys.fromJson(value) as ReturnType;
    case 'Pagination':
      return Pagination.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Platform':
      return Platform.fromJson(value) as ReturnType;
    case 'PlatformNone':
      return PlatformNone.fromJson(value) as ReturnType;
    case 'Run':
      return Run.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RunListResponse':
      return RunListResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'RunOutcome':
      return RunOutcome.fromJson(value) as ReturnType;
    case 'RunProgress':
      return RunProgress.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RunReasonCode':
      return RunReasonCode.fromJson(value) as ReturnType;
    case 'RunResponse':
      return RunResponse.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'RunSortKeys':
      return RunSortKeys.fromJson(value) as ReturnType;
    case 'RunStatus':
      return RunStatus.fromJson(value) as ReturnType;
    case 'RunType':
      return RunType.fromJson(value) as ReturnType;
    case 'ScheduleDateUtilsInput':
      return ScheduleDateUtilsInput.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ScheduleTrigger':
      return ScheduleTrigger.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ScheduleTriggerInput':
      return ScheduleTriggerInput.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ScheduleTriggerType':
      return ScheduleTriggerType.fromJson(value) as ReturnType;
    case 'Source':
      return Source.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceBigCommerce':
      return SourceBigCommerce.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SourceBigQuery':
      return SourceBigQuery.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SourceCSV':
      return SourceCSV.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceCommercetools':
      return SourceCommercetools.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SourceCreate':
      return SourceCreate.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceCreateResponse':
      return SourceCreateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SourceDocker':
      return SourceDocker.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceJSON':
      return SourceJSON.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceSearch':
      return SourceSearch.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceSortKeys':
      return SourceSortKeys.fromJson(value) as ReturnType;
    case 'SourceType':
      return SourceType.fromJson(value) as ReturnType;
    case 'SourceUpdate':
      return SourceUpdate.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SourceUpdateCommercetools':
      return SourceUpdateCommercetools.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SourceUpdateResponse':
      return SourceUpdateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SubscriptionTrigger':
      return SubscriptionTrigger.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SubscriptionTriggerType':
      return SubscriptionTriggerType.fromJson(value) as ReturnType;
    case 'Task':
      return Task.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TaskCreate':
      return TaskCreate.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TaskCreateResponse':
      return TaskCreateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TaskSearch':
      return TaskSearch.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TaskSortKeys':
      return TaskSortKeys.fromJson(value) as ReturnType;
    case 'TaskUpdate':
      return TaskUpdate.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TaskUpdateResponse':
      return TaskUpdateResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'TriggerInput':
      return TriggerInput.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TriggerType':
      return TriggerType.fromJson(value) as ReturnType;
    default:
      RegExpMatch? match;

      if (value is List && (match = _regList.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toList(growable: growable) as ReturnType;
      }
      if (value is Set && (match = _regSet.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toSet() as ReturnType;
      }
      if (value is Map && (match = _regMap.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return Map<dynamic, BaseType>.fromIterables(
          value.keys,
          value.values.map((dynamic v) => deserialize<BaseType, BaseType>(
              v, targetType,
              growable: growable)),
        ) as ReturnType;
      }
      if (targetType == 'Object') {
        return value;
      }
      break;
  }
  throw Exception('Cannot deserialize');
}
