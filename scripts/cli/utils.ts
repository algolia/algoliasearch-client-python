import inquirer from 'inquirer';

import { CLIENTS, GENERATORS, LANGUAGES } from '../common.js';
import type { Generator, Language } from '../types.js';

export const ALL = 'all';
export const PROMPT_LANGUAGES = [ALL, ...LANGUAGES];
export const PROMPT_CLIENTS = [ALL, ...CLIENTS];

export type AllLanguage = Language | typeof ALL;
export type LangArg = AllLanguage | undefined;

export type PromptDecision = {
  language: AllLanguage;
  client: string[];
  clientList: string[];
};

type Prompt = {
  langArg: LangArg;
  clientArg: string[];
  interactive: boolean;
};

export function getClientChoices(language?: LangArg, clientList = PROMPT_CLIENTS): string[] {
  const withoutAlgoliaSearch = clientList.filter((client) => client !== 'algoliasearch');

  return language === ALL || language === 'javascript' || language === 'dart'
    ? clientList
    : withoutAlgoliaSearch;
}

export function generatorList({
  language,
  client,
  clientList,
}: {
  language: AllLanguage;
  client: string[];
  clientList: string[];
}): Generator[] {
  const langsTodo = language === ALL ? LANGUAGES : [language];
  const clientsTodo = client[0] === ALL ? clientList : client;

  return langsTodo
    .flatMap((lang) => clientsTodo.map((cli) => GENERATORS[`${lang}-${cli}`]))
    .filter(Boolean);
}

export async function prompt({ langArg, clientArg, interactive }: Prompt): Promise<PromptDecision> {
  const decision: PromptDecision = {
    client: [ALL],
    language: ALL,
    clientList: [],
  };

  if (!langArg) {
    if (interactive) {
      const { language } = await inquirer.prompt<PromptDecision>([
        {
          type: 'list',
          name: 'language',
          message: 'Select a language',
          default: ALL,
          choices: LANGUAGES,
        },
      ]);

      decision.language = language;
    }
  } else {
    decision.language = langArg;
  }

  decision.clientList = getClientChoices(decision.language, CLIENTS);

  if (!clientArg?.length) {
    if (interactive) {
      const { client } = await inquirer.prompt<{ client: string }>([
        {
          type: 'list',
          name: 'client',
          message: 'Select a client',
          default: ALL,
          choices: getClientChoices(decision.language),
        },
      ]);

      decision.client = [client];
    }
  } else {
    clientArg.forEach((client) => {
      if (![ALL, ...decision.clientList].includes(client)) {
        throw new Error(
          `The '${clientArg}' client does not exist for ${
            decision.language
          }.\n\nAllowed choices are: ${decision.clientList.join(', ')}`
        );
      }
    });

    decision.client = clientArg;
  }

  return decision;
}
