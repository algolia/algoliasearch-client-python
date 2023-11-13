/* eslint-disable @typescript-eslint/no-var-requires */
/* eslint-disable import/no-commonjs */

const fs = require('fs');
const path = require('path');

function getSpecFiles() {
  const bundledSpecsPath = path.resolve(process.cwd(), '../specs/bundled');
  const specs = [];

  fs.readdirSync(bundledSpecsPath).forEach((file) => {
    if (file.endsWith('.doc.yml')) {
      const fileName = file.replace('.doc.yml', '');

      specs.push({
        fileName,
        path: `${bundledSpecsPath}/${file}`,
        route: `/specs/${fileName}`,
      });
    }
  });

  if (specs.length === 0) {
    throw new Error('Unable to find spec files');
  }

  return specs;
}

function getSpecsForPlugin() {
  return getSpecFiles().map((specFile) => {
    return {
      id: specFile.fileName,
      spec: specFile.path,
      route: specFile.route,
    };
  });
}

function getSpecsForNavBar() {
  return getSpecFiles().map((specFile) => {
    /** @type {import('@docusaurus/theme-common').NavbarItem} */
    return {
      label: specFile.fileName,
      href: specFile.route,
      className: 'header-restapi',
    };
  });
}

/** @type {import('@docusaurus/types').Config} */
(
  module.exports = {
    title: 'Algolia API',
    tagline: 'Documentation for the Algolia API and Clients.',
    url: 'https://api-clients-automation.netlify.app/',
    baseUrl: '/',
    favicon: 'img/logo-small.png',
    organizationName: 'Algolia',
    projectName: 'Algolia API and Clients',
    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'throw',

    presets: [
      [
        '@docusaurus/preset-classic',
        /** @type {import('@docusaurus/preset-classic').Options} */
        ({
          docs: {
            path: 'docs',
            sidebarPath: 'sidebars.js',
            editUrl:
              'https://github.com/algolia/api-clients-automation/edit/main/website/',
            showLastUpdateAuthor: true,
            showLastUpdateTime: true,
          },
          blog: false,
          theme: {
            customCss: require.resolve('./src/css/custom.css'),
          },
        }),
      ],
      [
        'redocusaurus',
        {
          specs: getSpecsForPlugin(),
          theme: {
            options: { disableSearch: true },
            primaryColor: '#5468ff',
            theme: {
              typography: { fontSize: '14px', lineHeight: '1.2em' },
              spacing: {
                unit: 5,
                sectionHorizontal: 30,
              },
            },
          },
        },
      ],
    ],

    themeConfig:
      /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
      ({
        prism: {
          // scala is required to make java work
          additionalLanguages: ['php', 'java', 'scala', 'dart', 'go']
        },
        navbar: {
          title: 'Algolia API',
          logo: {
            alt: 'Algolia',
            src: 'img/logo-small.png',
            srcDark: 'img/logo-small.png',
          },
          items: [
            // left
            {
              label: 'Clients',
              to: 'docs/clients/introduction',
              position: 'left',
            },
            {
              label: 'HTTP API',
              position: 'left',
              type: 'dropdown',
              items: getSpecsForNavBar(),
            },
            // right
            {
              label: 'Contributing',
              to: 'docs/contributing/introduction',
              position: 'right',
            },
            {
              label: 'Algolia documentation',
              href: 'https://www.algolia.com/doc/',
              position: 'right',
            },
            {
              href: 'https://github.com/algolia/api-clients-automation',
              position: 'right',
              className: 'header-github-link',
            },
          ],
        },
        algolia: {
          appId: 'QPBQ67WNIG',
          apiKey: 'b590ae1153bf574215ca1605c19eb1fe',
          indexName: 'api-clients-automation',
        },
        colorMode: {
          defaultMode: 'light',
          disableSwitch: false,
          respectPrefersColorScheme: true,
        },
        footer: {
          style: 'dark',
          links: [
            {
              label: 'GitHub',
              to: 'https://github.com/algolia/api-clients-automation',
            },
            {
              label: 'Twitter',
              to: 'https://twitter.com/algolia',
            },
            {
              label: 'Algolia Website',
              to: 'https://algolia.com/',
            },
            {
              label: 'Algolia Blog',
              to: 'https://algolia.com/blog',
            },
          ],
          copyright: `Copyright © ${new Date().getFullYear()} Algolia | Built with Docusaurus.`,
        },
      }),
  }
);
