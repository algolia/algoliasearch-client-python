import fsp from 'fs/promises';
import path from 'path';

import { createClientName, toAbsolutePath } from '../common';
import { getLanguageApiFolder, getLanguageModelFolder } from '../config';
import type { Generator } from '../types';

/**
 * Remove `model` folder for the current language and client.
 */
export async function removeExistingCodegen({
  language,
  client,
  output,
}: Generator): Promise<void> {
  const baseModelFolder = getLanguageModelFolder(language);
  const baseApiFolder = getLanguageApiFolder(language);
  const clientName = createClientName(client, language);

  let clientModel = '';
  let clientApi = '';

  switch (language) {
    case 'java':
      clientModel = client.replace('-', '');
      clientApi = `${clientName}*.java`;
      break;
    case 'php':
      clientModel = clientName;
      clientApi = `${clientName}*.php`;
      break;
    case 'javascript':
      // We want to also delete the nested `lite` client or folders that only exists in JS
      if (clientName === 'algoliasearch') {
        await fsp.rm(toAbsolutePath(path.resolve('..', output, 'lite')), {
          force: true,
          recursive: true,
        });
      }

      // Delete `builds` folder
      await fsp.rm(toAbsolutePath(path.resolve('..', output, 'builds')), {
        force: true,
        recursive: true,
      });
      break;
    case 'dart':
      clientModel = clientName;
      clientApi = `${clientName}*.dart`;
      break;
    default:
      break;
  }

  // Delete client model folder/file
  await fsp.rm(
    toAbsolutePath(path.resolve('..', output, baseModelFolder, clientModel)),
    { force: true, recursive: true }
  );

  // Delete client api folder/file
  await fsp.rm(
    toAbsolutePath(path.resolve('..', output, baseApiFolder, clientApi)),
    { force: true, recursive: true }
  );
}
