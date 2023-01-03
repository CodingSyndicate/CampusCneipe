import { sveltekit } from '@sveltejs/kit/vite';
import { imagetools } from 'vite-imagetools';
import path from 'path';

const supportedExtensions = ['png', 'jpg', 'jpeg'];

const config = {
  plugins: [
    imagetools({
      defaultDirectives: (url) => {
	const extension = url.pathname.substring(url.pathname.lastIndexOf('.') + 1);
	if (supportedExtensions.includes(extension)) {
	  return new URLSearchParams({
	    format: 'avif;webp;' + extension,
	    picture: true,
	    //source: true,
	    width: '200;320;480;720;1028;1400;1920'
	  });
	}
	return new URLSearchParams();
      }
    }),
    sveltekit()],

	css: {
		preprocessorOptions: {
			scss: {
				additionalData: '@use "src/variables.scss" as *;'
			}
		}
	},

	resolve: {
		alias: {
			$data: path.resolve('./data')
		}
	},

	server: {
		fs: {
			// Allow serving files from one level up to the project root
			allow: ['..']
		}
	}
};

export default config;
