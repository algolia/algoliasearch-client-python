import Spinnies from 'spinnies';

import { CI, isVerbose } from './common.js';

class SpinnerStatic {
  private maybeText(text?: string): void {
    if (text !== undefined) {
      // eslint-disable-next-line no-console
      console.log(text);
    }
  }

  constructor(text: string) {
    this.maybeText(text);
  }

  succeed(text?: string): void {
    this.maybeText(text);
  }

  fail(text?: string): void {
    this.maybeText(text);
  }

  warn(text?: string): void {
    this.maybeText(text);
  }

  set text(t: string) {
    this.maybeText(t);
  }

  get text(): string {
    return '';
  }
}

const spinnies = new Spinnies();

class SpinnerWrapper {
  private name: string;

  constructor(name: string, text: string) {
    this.name = name;
    spinnies.add(name, { text });
  }

  succeed(text?: string): void {
    spinnies.succeed(this.name, { text });
  }

  fail(text?: string): void {
    spinnies.fail(this.name, { text });
  }

  warn(text?: string): void {
    spinnies.fail(this.name, { text, failColor: 'yellow' });
  }

  set text(t: string) {
    spinnies.update(this.name, { text: t });
  }

  get text(): string {
    return '';
  }
}

export function createSpinner(text: string): SpinnerStatic | SpinnerWrapper {
  return CI || isVerbose() ? new SpinnerStatic(text) : new SpinnerWrapper(text, text);
}
