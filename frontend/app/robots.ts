import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
  };
}
