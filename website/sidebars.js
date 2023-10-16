// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // Everything related to the API Clients Automation
  automation: [
    'contributing/introduction',
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      items: [
        'contributing/setup-repository',
        {
          type: 'category',
          label: 'CLI',
          collapsed: false,
          items: [
            'contributing/CLI/specs-commands',
            'contributing/CLI/clients-commands',
            'contributing/CLI/cts-commands',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Contributing',
      collapsed: false,
      items: [
        'contributing/add-new-api-client',
        'contributing/add-new-language',
        {
          type: 'category',
          label: 'Testing',
          collapsed: false,
          items: [
            'contributing/testing/common-test-suite',
            'contributing/testing/playground',
          ],
        },
        'contributing/commit-and-pull-request',
        'contributing/release-process',
      ],
    },
  ],
  // Everything related to the generated clients usage
  clients: [
    'clients/introduction',
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      items: [
        'clients/installation',
        {
          type: 'category',
          label: 'Migration guide',
          collapsed: false,
          link: {
            type: 'doc',
            id: 'clients/migration-guides/index',
          },
          items: [
            'clients/migration-guides/javascript',
            'clients/migration-guides/java',
            'clients/migration-guides/php',
            'clients/migration-guides/kotlin',
            'clients/migration-guides/go',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Guides',
      collapsed: false,
      items: [
        'clients/guides/send-data-to-algolia',
        'clients/guides/filtering-your-search',
        'clients/guides/retrieving-facets',
        'clients/guides/customized-client-usage',
        'clients/guides/wait-for-a-task-to-finish',
        'clients/guides/wait-for-api-key-to-be-valid',
        'clients/guides/copy-or-move-index-rules-settings-synonyms',
        'clients/guides/copy-index-to-another-application',
        'clients/guides/manage-dictionary-entries',
        'clients/guides/delete-objects',
        'clients/guides/replace-all-rules-synonyms',
      ],
    },
  ],
};

// eslint-disable-next-line import/no-commonjs
module.exports = sidebars;
