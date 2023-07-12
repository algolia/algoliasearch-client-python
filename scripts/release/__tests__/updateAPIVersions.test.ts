import { getNextVersion } from '../createReleasePR.js';
import { getVersionsToRelease } from '../updateAPIVersions.js';

describe('updateAPIversions', () => {
  it('gets versions to release', () => {
    const versions = getVersionsToRelease({
      javascript: {
        current: '1.0.0',
        releaseType: 'minor',
        next: getNextVersion('1.0.0', 'minor'),
      },
      php: {
        current: '2.0.0',
        releaseType: 'patch',
        next: getNextVersion('2.0.0', 'patch'),
      },
      java: {
        current: '3.0.0',
        releaseType: null,
        noCommit: true,
        skipRelease: true,
        next: null,
      },
    });

    expect(Object.keys(versions)).toEqual(['javascript', 'php']);
    expect(versions.java).toBeUndefined();
    expect(versions.javascript?.current).toEqual('1.0.0');
    expect(versions.javascript?.releaseType).toEqual('minor');
    expect(versions.php?.current).toEqual('2.0.0');
    expect(versions.php?.releaseType).toEqual('patch');
  });

  it('correctly reads clients version and their next release type', () => {
    const versions = getVersionsToRelease({
      javascript: {
        current: '0.0.1',
        releaseType: 'patch',
        next: getNextVersion('0.0.1', 'patch'),
      },
      php: {
        current: '0.0.1',
        releaseType: 'minor',
        next: getNextVersion('0.0.1', 'minor'),
      },
      java: {
        current: '0.0.1',
        releaseType: 'patch',
        skipRelease: true,
        next: null,
      },
    });
    expect(versions).toEqual({
      javascript: expect.objectContaining({
        current: '0.0.1',
        releaseType: 'patch',
      }),
      php: expect.objectContaining({
        current: '0.0.1',
        releaseType: 'minor',
      }),
    });
  });
});
