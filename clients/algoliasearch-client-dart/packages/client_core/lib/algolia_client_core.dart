/// Core functionality for interacting with the Algolia API.
///
/// This library provides the essential logic for configuring and executing
/// HTTP requests to the Algolia API. It includes support for retry strategies
/// and comprehensive exception handling.
library algolia_client_core;

export 'src/algolia_exception.dart';
export 'src/api_client.dart';
export 'src/config/agent_segment.dart';
export 'src/config/client_options.dart';
export 'src/config/host.dart';
export 'src/transport/api_request.dart';
export 'src/transport/request_options.dart';
export 'src/transport/requester.dart';
export 'src/transport/retry_strategy.dart';
