import { DOCKER, run, runComposerUpdate } from './common';
import { createSpinner } from './spinners';

export async function formatter(
  language: string,
  folder: string
): Promise<void> {
  const spinner = createSpinner(`formatting '${language}'`);
  let cmd = '';
  switch (language) {
    case 'javascript':
      cmd = `yarn eslint --ext=ts,json ${folder} --fix --no-error-on-unmatched-pattern`;
      break;
    case 'java':
      cmd = `find ${folder} -type f -name "*.java" | xargs java --add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED \
        --add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED \
        --add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED \
        --add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED \
        --add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED \
        -jar /tmp/java-formatter.jar -r \
        && yarn prettier --write ${folder}`;
      break;
    case 'php':
      await runComposerUpdate();
      cmd = `yarn run prettier ${folder} --write \
            && PHP_CS_FIXER_IGNORE_ENV=1 php clients/algoliasearch-client-php/vendor/bin/php-cs-fixer fix ${folder} --using-cache=no --allow-risky=yes`;
      break;
    case 'go':
      cmd = `cd ${folder} && go fmt ./...`;
      if (DOCKER) {
        cmd = `cd ${folder} && /usr/local/go/bin/go fmt ./...`;
      }
      break;
    case 'kotlin':
      cmd = `${folder}/gradlew -p ${folder} spotlessApply`;
      break;
    case 'dart':
      if (folder.includes('tests')) {
        cmd = `(cd ${folder} && dart fix --apply && dart format .)`;
      } else {
        cmd = `(cd ${folder} && melos bs && melos build --no-select && melos lint)`;
      }
      break;
    default:
      return;
  }
  await run(cmd);
  spinner.succeed();
}
