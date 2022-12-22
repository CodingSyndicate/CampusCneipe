import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';
import { mdsvex } from 'mdsvex'

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    trailingSlash: 'always',
    paths: {
      base: process.env.BASE
    }
  },

  extensions: ['.svelte', '.md'],
  preprocess: [
    preprocess({
      scss: {
	prependData: '@use "src/variables.scss" as *;'
      }
    }),
    mdsvex({
      extensions: ['.md']
    })
  ],

  vitePlugin: {
    experimental: {
      useVitePreprocess: true
    }
  }
};

export default config;
