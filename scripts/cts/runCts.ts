import { run, runComposerUpdate } from '../common';
import { createSpinner } from '../spinners';

async function runCtsOne(language: string): Promise<void> {
  const spinner = createSpinner(`running cts for '${language}'`);
  switch (language) {
    case 'javascript':
      await run(
        'YARN_ENABLE_IMMUTABLE_INSTALLS=false yarn install && yarn test',
        {
          cwd: 'tests/output/javascript',
        }
      );
      break;
    case 'java':
      await run('./gradle/gradlew --no-daemon -p tests/output/java test');
      break;
    case 'php': {
      await runComposerUpdate();
      await run(
        `php ./clients/algoliasearch-client-php/vendor/bin/phpunit tests/output/php`
      );
      break;
    }
    case 'kotlin':
      await run('./gradle/gradlew --no-daemon -p tests/output/kotlin allTests');
      break;
    default:
      spinner.warn(`skipping unknown language '${language}' to run the CTS`);
      return;
  }
  spinner.succeed();
}

export async function runCts(languages: string[]): Promise<void> {
  for (const lang of languages) {
    await runCtsOne(lang);
  }
}
