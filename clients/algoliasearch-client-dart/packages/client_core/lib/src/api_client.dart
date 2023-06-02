import 'package:algolia_client_core/src/config/client_options.dart';

/// An abstract class representing an API client with specific properties and options.
abstract interface class ApiClient {
  /// The unique identifier for the application using the API client.
  String get appId;

  /// The API key used for authentication.
  String get apiKey;

  /// A set of custom client options to configure the behavior of the API client.
  ClientOptions get options;

  /// Dispose of underlying resources.
  void dispose();
}
