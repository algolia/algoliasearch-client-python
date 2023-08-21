import type { ReleaseType } from 'semver';

import type { Language } from '../types.js';

export type Version = {
  current: string;
  releaseType: ReleaseType | null;
  next: string | null;
  skipRelease?: boolean;
  noCommit?: boolean;
};

export type Versions = Record<string, Version>;

export type VersionsBeforeBump = Record<string, Omit<Version, 'next' | 'releaseType'>>;

export type Scope = Language | 'clients' | 'specs';

export type PassedCommit = {
  hash: string;
  type: string;
  /**
   * A commit can be scoped to a language. When scoped to `clients` or `specs`, it impacts all clients.
   */
  scope: Scope;
  author: string;
  message: string;
  raw: string;
  prNumber: number;
};

export type Commit =
  | PassedCommit
  | { error: 'generation-commit' }
  | { error: 'missing-language-scope'; message: string }
  | { error: 'unknown-language-scope'; message: string };

export type VersionsToRelease = {
  [lang in Language]?: {
    current: string;
    next: string;
    releaseType: ReleaseType;
  };
};

export type Changelog = {
  [lang in Language]?: string;
};

export type BeforeClientCommitCommand = (params: { dir: string }) => Promise<void>;
