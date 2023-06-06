// Algolia Algolia insights API client to interact with Algolia
library algolia_client_insights;

export 'package:algolia_client_core/algolia_client_core.dart'
    show AgentSegment, ApiClient, CallType, ClientOptions, Host, RequestOptions;
export 'src/api/insights_client.dart';

export 'src/model/error_base.dart';
export 'src/model/event_type.dart';
export 'src/model/insight_event.dart';
export 'src/model/insight_events.dart';
export 'src/model/push_events_response.dart';

export 'src/extension.dart';
