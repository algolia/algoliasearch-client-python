module.exports = {
  ignorePatterns: [
    "*.test.ts"
  ],

  parser: '@typescript-eslint/parser',
  
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    tsconfigRootDir: __dirname,
    project: "tsconfig.json",
  },

  settings: {
    'import/extensions': ['.js', '.ts', '.mjs'],
    'import/parsers': {
      '@typescript-eslint/parser': ['.ts', '.js', '.mjs'],
    },
    'import/ignore': ['node_modules'],
    'import/resolver': {
      typescript: {},
    },
  },

  rules: {
    "import/extensions": [2, "ignorePackages", {
      "js": "never",
      "ts": "never",
      "mjs": "never",
    }],
    '@typescript-eslint/sort-type-union-intersection-members': 0
  },
};
