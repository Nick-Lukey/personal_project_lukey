import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  // vite uses this as a prefix for href and src URLs
  base: '/static/',
  build: {
    // this is the folder where vite will generate its output. Make sure django can serve files from here!
    outDir: '../env/WasherToss/static',

    // delete the old build when creating the new build. 
    // this is the default behavior, unless outDir is outside of the current directory
    emptyOutDir: true,
	
	// vite will generate sourcemaps, which let you see logs and error messages with line numbers from our jsx files, not from the minified js
	sourcemap: true,

  },
  plugins: [react()]
})


