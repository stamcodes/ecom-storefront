import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [],
  },
  typescript: {
    // Keeps ignoring type errors from empty files during this test phase
    ignoreBuildErrors: true,
  },
};

export default nextConfig;
