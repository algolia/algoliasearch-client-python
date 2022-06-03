import { createClientName, run } from './common';
import type { Language } from './types';

export async function playground({
  language,
  client,
}: {
  language: Language | 'all';
  client: string;
}): Promise<void> {
  const verbose = true;
  switch (language) {
    case 'javascript':
      await run(`yarn workspace javascript-playground start:${client}`, {
        verbose,
      });
      break;
    case 'java':
      await run(
        `./gradle/gradlew -p playground/java -PmainClass=com.algolia.playground.${createClientName(
          client,
          'java'
        )} run`,
        {
          verbose,
        }
      );
      break;
    case 'php':
      await run(
        `cd clients/algoliasearch-client-php/ && \
       composer update && \
       composer dump-autoload && \
       cd ../../playground/php/src && \
       php8 ${client}.php`,
        { verbose }
      );
      break;
    default:
  }
}
