import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { mdsvex } from 'mdsvex'


/** @type {import('@sveltejs/kit').Config} */
const md_layout = "./src/MarkdownLayout.svelte";

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
      layout: md_layout,
      extensions: ['.md']
    }),
    vitePreprocess()
  ],
};

export default config;
