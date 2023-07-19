import type config from '../config/clients.config.json';

/**
 * Config.
 */
export type ClientsConfig = Record<Language, LanguageConfig>;

export type LanguageConfig = {
  folder: string;
  gitRepoId: string;
  modelFolder: string;
  apiFolder: string;
  customGenerator: string;
  packageVersion?: string;
  tests: {
    extension: string;
    outputFolder: string;
  };
};

export type Generator = Record<string, any> & {
  language: Language;
  client: string;
  key: string;
  additionalProperties: AdditionalProperties;
};

export type AdditionalProperties = Partial<{
  packageName: string;
}> &
  Record<string, any>;

export type CheckForCacheOptions = {
  folder: string;
  generatedFiles: string[];
  filesToCache: string[];
  cacheFile: string;
};

export type CheckForCache = {
  cacheExists: boolean;
  hash: string;
};

export type RunOptions = {
  errorMessage?: string;
  cwd?: string;
};

export type Language = keyof typeof config;

export type Spec = {
  servers: Server[];
  tags: Tag[];
  paths: Path[];
};

/**
 * Server of a spec.
 */
type Server = {
  url: string;
  variables?: Record<
    string,
    {
      enum?: string[];
      default: string;
    }
  >;
};

/**
 * Global tag of a spec.
 */
type Tag = {
  name: string;
  description: string;
};

/**
 * Paths of a spec.
 */
type Path = Record<string, Record<string, any>>;
