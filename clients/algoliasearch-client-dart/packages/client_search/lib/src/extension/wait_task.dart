import 'package:algolia_client_core/algolia_client_core.dart';
import 'package:algolia_client_search/src/api/search_client.dart';
import 'package:algolia_client_search/src/model/api_key.dart';
import 'package:algolia_client_search/src/model/get_api_key_response.dart';
import 'package:algolia_client_search/src/model/task_status.dart';
import 'package:collection/collection.dart';

extension WaitTask on SearchClient {
  /// Wait for a [taskID] to complete before executing the next line of code, to synchronize index
  /// updates. All write operations in Algolia are asynchronous by design. It means that when you add
  /// or update an object to your index, our servers will reply to your request with a [taskID] as soon
  /// as they understood the write operation. The actual insert and indexing will be done after
  /// replying to your code. You can wait for a task to complete by using the [taskID] and this method.
  Future<void> waitTask({
    required String indexName,
    required int taskID,
    WaitParams params = const WaitParams(),
    RequestOptions? requestOptions,
  }) async {
    await _waitUntil(
      params: params,
      retry: () => getTask(
        indexName: indexName,
        taskID: taskID,
        requestOptions: requestOptions,
      ),
      until: (response) => response.status == TaskStatus.published,
    );
  }

  ///  Wait on an API key creation operation.
  Future<void> waitKeyCreation({
    required String key,
    int maxRetries = 50,
    WaitParams params = const WaitParams(),
    RequestOptions? requestOptions,
  }) async {
    await _waitUntil(
      retry: () async {
        try {
          return await getApiKey(key: key, requestOptions: requestOptions);
        } on AlgoliaApiException catch (_) {
          return null;
        }
      },
      until: (result) => result != null,
      params: params,
    );
  }

  /// Wait on a delete API ket operation.
  Future<void> waitKeyDeletion({
    required String key,
    WaitParams params = const WaitParams(),
    RequestOptions? requestOptions,
  }) async {
    await _waitUntil(
      params: params,
      retry: () async {
        try {
          return await getApiKey(key: key, requestOptions: requestOptions);
        } on AlgoliaApiException catch (e) {
          return e;
        }
      },
      until: (result) =>
      result is AlgoliaApiException ? result.statusCode == 404 : false,
    );
  }

  /// Wait on an API key update operation.
  Future<void> waitKeyUpdate({
    required String key,
    required ApiKey apiKey,
    WaitParams params = const WaitParams(),
    RequestOptions? requestOptions,
  }) async {
    await _waitUntil(
      params: params,
      retry: () async =>
          await getApiKey(key: key, requestOptions: requestOptions),
      until: (response) => _isExpectedApiKey(apiKey, response),
    );
  }
}

/// Wait operation parameters.
class WaitParams {
  final int maxRetries;
  final Duration? timeout;
  final Duration initialDelay;
  final Duration maxDelay;

  const WaitParams({
    this.maxRetries = 50,
    this.timeout,
    this.initialDelay = const Duration(milliseconds: 200),
    this.maxDelay = const Duration(seconds: 5),
  });
}

/// Checks if [response] contains the expected updates in [apiKey].
bool _isExpectedApiKey(ApiKey apiKey, GetApiKeyResponse response) {
  return const DeepCollectionEquality.unordered()
            .equals(apiKey.acl, response.acl) &&
        (apiKey.description == null ||
            (apiKey.description != null &&
                apiKey.description == response.description)) &&
        (apiKey.indexes == null ||
            (apiKey.indexes != null &&
                const DeepCollectionEquality.unordered()
                    .equals(apiKey.indexes, response.indexes))) &&
        (apiKey.maxHitsPerQuery == null ||
            (apiKey.maxHitsPerQuery != null &&
                apiKey.maxHitsPerQuery == response.maxHitsPerQuery)) &&
        (apiKey.maxQueriesPerIPPerHour == null ||
            (apiKey.maxQueriesPerIPPerHour != null &&
                apiKey.maxQueriesPerIPPerHour ==
                    response.maxQueriesPerIPPerHour)) &&
        (apiKey.queryParameters == null ||
            (apiKey.queryParameters != null &&
                apiKey.queryParameters == response.queryParameters)) &&
        (apiKey.referers == null ||
            (apiKey.referers != null &&
                const DeepCollectionEquality.unordered()
                    .equals(apiKey.referers, response.referers))) &&
        (apiKey.validity == null ||
            (apiKey.validity != null &&
                apiKey.validity == response.validity));
}

/// Retries the given [retry] function until the [until] condition is satisfied or the maximum number
/// of [maxRetries] or [timeout] is reached.
Future<T> _waitUntil<T>({
  required Future<T> Function() retry,
  required bool Function(T) until,
  required WaitParams params,
}) async {
  Future<T> wait() async {
    var currentDelay = params.initialDelay;
    for (var i = 0; i < params.maxRetries; i++) {
      var result = await retry();
      if (until(result)) return result;
      await Future.delayed(currentDelay);
      var newDelay = currentDelay * 2;
      currentDelay = newDelay < params.maxDelay ? newDelay : params.maxDelay;
    }
    throw AlgoliaWaitException(
        "The maximum number of retries ($params.maxRetries) exceeded");
  }

  final timeout = params.timeout;
  return timeout == null
      ? wait()
      : wait().timeout(
          timeout,
          onTimeout: () => throw Exception("Timeout of $timeout ms exceeded"),
        );
}
