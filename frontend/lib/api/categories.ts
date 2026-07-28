export interface Category {
  id: string | number;
  name: string;
  slug?: string;
  description?: string;
  image_url?: string;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

/**
 * Fetch all categories from the backend API.
 */
export async function getCategories(): Promise<Category[]> {
  try {
    const res = await fetch(`${API_BASE_URL}/categories`, {
      cache: "no-store",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!res.ok) {
      throw new Error(`Failed to fetch categories: ${res.statusText}`);
    }

    const data = await res.json();
    return data.items || data || [];
  } catch (error) {
    console.error("Error fetching categories:", error);
    return [];
  }
}

/**
 * Fetch a single category by ID or slug.
 */
export async function getCategoryByIdOrSlug(idOrSlug: string | number): Promise<Category | null> {
  try {
    const res = await fetch(`${API_BASE_URL}/categories/${idOrSlug}`, {
      cache: "no-store",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!res.ok) {
      if (res.status === 404) return null;
      throw new Error(`Failed to fetch category: ${res.statusText}`);
    }

    return await res.json();
  } catch (error) {
    console.error(`Error fetching category (${idOrSlug}):`, error);
    return null;
  }
}
