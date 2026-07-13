import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  const backendProxyTarget = env.VITE_BACKEND_PROXY_TARGET;

  return {
    plugins: [react()],
    server: backendProxyTarget
      ? {
          proxy: {
            '/api': backendProxyTarget,
            '/health': backendProxyTarget,
            '/version': backendProxyTarget,
          },
        }
      : undefined,
  };
});
