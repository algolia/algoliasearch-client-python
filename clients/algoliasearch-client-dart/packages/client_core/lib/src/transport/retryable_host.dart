import 'package:algolia_client_core/src/config/host.dart';

/// This internal data class represents a host that supports retrying requests.
///
/// It wraps a Host object and provides additional information about the host's status, such as
/// whether it is up, when it was last updated, and how many times it has been retried.
final class RetryableHost {
  final Host host;

  bool get isUp => _isUp;
  bool _isUp;

  DateTime get lastUpdated => _lastUpdated;
  DateTime _lastUpdated;

  int get retryCount => _retryCount;
  int _retryCount;

  RetryableHost(this.host)
      : _isUp = true,
        _lastUpdated = DateTime.now(),
        _retryCount = 0;

  void reset() {
    _isUp = true;
    _lastUpdated = DateTime.now();
    _retryCount = 0;
  }

  void timedOut() {
    _isUp = true;
    _lastUpdated = DateTime.now();
    _retryCount += 1;
  }

  void failed() {
    _isUp = false;
    _lastUpdated = DateTime.now();
  }
}
