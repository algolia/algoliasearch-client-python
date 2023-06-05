// Dart Algolia insights API client to interact with Algolia
library algolia_insights;

export 'package:algolia_client_core/algolia_client_core.dart'
    show AgentSegment, ApiClient, CallType, ClientOptions, Host, RequestOptions;
export 'package:algolia_insights/src/api/insights_client.dart';

export 'package:algolia_insights/src/model/error_base.dart';
export 'package:algolia_insights/src/model/event_type.dart';
export 'package:algolia_insights/src/model/insight_event.dart';
export 'package:algolia_insights/src/model/insight_events.dart';
export 'package:algolia_insights/src/model/push_events_response.dart';

export 'package:algolia_insights/src/extension.dart';
