import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';



export default defineConfig({
    plugins: [
        laravel({
            input: [
                'resources/ts/app.ts',
            ],
            refresh: true,
        }),

    ],
    resolve: {
        alias: {
            vue: 'vue/dist/vue.esm-bundler.js',
        },
    },
});
