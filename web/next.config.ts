import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  eslint: {
    ignoreDuringBuilds: true, // ✅ ESLint errors ignore kar dega
  },
  typescript: {
    ignoreBuildErrors: true, // ✅ TS errors ignore kar dega
  },
};

export default nextConfig;
