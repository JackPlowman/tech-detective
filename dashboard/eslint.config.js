import eslintPluginAstro from 'eslint-plugin-astro';
export default [
  ...eslintPluginAstro.configs.recommended,
  {
    plugins: {
      'jsx-a11y': jsxA11y,
    },
    rules: {
    }
  }
];
