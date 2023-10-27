import type { Rule } from 'eslint';

import { isPairWithKey } from '../utils';

export function createOutOfLineRule({
  property,
  description = `${property} must be out of line, not nested inside properties`,
  messageId = `${property}NotOutOfLine`,
  message = `${property} must be out of line`,
}: {
  property: string;
  description?: string;
  messageId?: string;
  message?: string;
}): Rule.RuleModule {
  const rule: Rule.RuleModule = {
    meta: {
      docs: {
        description,
      },
      messages: {
        [messageId]: message,
      },
    },
    create(context) {
      if (!context.sourceCode.parserServices.isYAML) {
        return {};
      }

      return {
        YAMLPair(node): void {
          if (!isPairWithKey(node, property)) {
            return;
          }
          // parent is mapping, and parent is real parent that must be to the far left
          if (node.parent.parent.loc.start.column === 0) {
            return;
          }
          // accept anything in servers
          if (
            isPairWithKey(
              node.parent.parent.parent.parent?.parent?.parent?.parent ?? null,
              'servers'
            )
          ) {
            return;
          }
          context.report({
            node: node.parent.parent as any,
            messageId,
          });
        },
      };
    },
  };
  return rule;
}
