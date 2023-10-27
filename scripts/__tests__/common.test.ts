import { afterEach, describe, expect, it, vi } from "vitest";

import { getClientsConfigField } from '../config.js';

vi.mock('execa', () => {
  return {
    execaCommand: vi.fn(),
    execa: vi.fn(),
  };
});

const { capitalize, createClientName, gitCommit } = await import(
  '../common.js'
);
const { execa } = await import('execa');

describe('gitCommit', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('commits with message', () => {
    gitCommit({ message: 'chore: does something' });
    expect(execa).toHaveBeenCalledTimes(1);
    expect(execa).toHaveBeenCalledWith(
      'git', ["commit", "-m", "chore: does something"],
      { cwd: expect.any(String) }
    );
  });

  it('commits with co-author', () => {
    // This reflects how it can be retrieved from git commands.
    const author = `Co-authored-by: them <them@algolia.com>
     `.trim();
    const coAuthors = `

      Co-authored-by: me <me@algolia.com>


      Co-authored-by: you <you@algolia.com>
      
      `
      .split('\n')
      .map((coAuthor) => coAuthor.trim())
      .filter(Boolean);

    gitCommit({
      message: 'chore: does something',
      coAuthors: [author, ...coAuthors],
    });
    expect(execa).toHaveBeenCalledTimes(1);
    expect(execa).toHaveBeenCalledWith(
      'git', ["commit", "-m", "chore: does something\n\n\nCo-authored-by: them <them@algolia.com>\nCo-authored-by: me <me@algolia.com>\nCo-authored-by: you <you@algolia.com>"],
      { cwd: expect.any(String) }
    );
  });
});

describe('config', () => {
  describe('getClientsConfigField', () => {
    it('throws if the field is not found', () => {
      expect(() => {
        getClientsConfigField('javascript', 'foofoo');
      }).toThrowErrorMatchingInlineSnapshot(
        `"Unable to find 'foofoo' for 'javascript'"`
      );
    });

    it('find the field if it exists', () => {
      expect(getClientsConfigField('java', ['tests', 'extension'])).toEqual(
        '.test.java'
      );
    });
  });
});

describe('utils', () => {
  describe('capitalize', () => {
    it('should capitalize first letter', () => {
      expect(capitalize('hello')).toEqual('Hello');
      expect(capitalize('Hello')).toEqual('Hello');
    });

    it('should only capitalize first letter', () => {
      expect(capitalize('hello wolrd')).toEqual('Hello wolrd');
      expect(capitalize('Hello wolrd')).toEqual('Hello wolrd');
    });

    it('should not affect other character', () => {
      expect(capitalize('8Hello')).toEqual('8Hello');
      expect(capitalize('<hello>')).toEqual('<hello>');
    });
  });

  describe('createClientName', () => {
    it('does not capitalize every part for JavaScript', () => {
      expect(createClientName('search', 'javascript')).toEqual('search');
      expect(createClientName('search-client', 'javascript')).toEqual(
        'searchClient'
      );
      expect(createClientName('search-cli!nt-complex', 'javascript')).toEqual(
        'searchCli!ntComplex'
      );
    });

    it('capitalize every part for other languages', () => {
      expect(createClientName('search', 'java')).toEqual('Search');
      expect(createClientName('search-client', 'java')).toEqual('SearchClient');
      expect(createClientName('search-cli!nt-complex', 'java')).toEqual(
        'SearchCli!ntComplex'
      );
    });
  });
});
