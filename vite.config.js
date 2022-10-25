import { sveltekit } from '@sveltejs/kit/vite';
import path from 'path';

const config = {
	plugins: [sveltekit()],

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
