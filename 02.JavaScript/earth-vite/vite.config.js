// vite.config.js

export default {
  build: {
    emptyOutDir: false,
    chunkSizeWarningLimit: 5024,
    target: ["chrome90"],
  },
  resolve: {
    alias: {
      http: "http-browserify",
      https: "https-browserify",
      zlib: "zlib-browserify",
    },
  },
};
