import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: "https://localhost:3000",
      lastModified: new Date(),
    },
  ];
}
