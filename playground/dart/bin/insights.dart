import 'package:algoliasearch/algoliasearch.dart';
import 'package:dotenv/dotenv.dart';

void main() async {
  final dotenv = DotEnv()..load(['../.env']);

  // Creating an instance of the Insights client with the provided App ID and API key.
  final insights = InsightsClient(
    appId: dotenv['ALGOLIA_APPLICATION_ID']!,
    apiKey: dotenv['ALGOLIA_SEARCH_KEY']!,
    options: ClientOptions(logger: print),
  );

  // Creating an InsightEvents object with a list of InsightEvent objects.
  // Each InsightEvent represents an event such as a user viewing a specific item.
  final events = InsightEvents(
    events: [
      InsightEvent(
        eventType: EventType.view,
        eventName: 'View event',
        index: 'instant_search',
        userToken: 'anonymous',
        queryID: '43b15df305339e827f0ac0bdc5ebcaa7',
        objectIDs: ['5477500'],
      )
    ],
  );
  await insights.pushEvents(insightEvents: events);

  // Close the client and dispose of all underlying resources.
  insights.dispose();
}
