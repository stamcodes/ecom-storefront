import Link from "next/link";
import { getProducts } from "@/lib/api/products";
import { getCategories } from "@/lib/api/categories";
import { ProductCard } from "@/components/features/product/productCard";

interface Product {
  id: string | number;
  name: string;
  slug?: string;
  price: number;
  image_url?: string;
  category_name?: string;
}

interface Category {
  id: string | number;
  name: string;
  slug?: string;
}

export default async function HomePage() {
  let products: Product[] = [];
  let categories: Category[] = [];

  try {
    const [productsRes, categoriesRes] = await Promise.all([
      getProducts({ limit: 12 }),
      getCategories(),
    ]);
    products = productsRes?.items || productsRes || [];
    categories = categoriesRes || [];
  } catch (error) {
    console.error("Failed to load homepage data:", error);
  }

  const featuredProducts = products.slice(0, 3);
  const recentProducts = products.slice(3, 11);

  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-8 md:p-12 shadow-xl">
        <div className="max-w-3xl space-y-4">
          <span className="text-xs font-semibold tracking-wider text-indigo-400 uppercase">
            Featured Collection
          </span>
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight">
            Discover Premium Products for Your Modern Lifestyle
          </h1>
          <p className="text-slate-300 text-lg">
            Explore our curated catalog of high-quality goods, exclusive deals, and fast delivery
            directly to your doorstep.
          </p>
          <div className="pt-2">
            <Link
              href="/products"
              className="inline-block bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-6 py-3 rounded-lg transition-colors shadow-md"
            >
              Shop All Products
            </Link>
          </div>
        </div>
      </section>

      {/* Featured Items Grid */}
      {featuredProducts.length > 0 && (
        <section className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-bold tracking-tight text-slate-900">Featured Items</h2>
            <Link
              href="/products"
              className="text-sm font-medium text-indigo-600 hover:text-indigo-500"
            >
              View all &rarr;
            </Link>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            {featuredProducts.map((product: Product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        </section>
      )}

      {/* Category Section */}
      {categories.length > 0 && (
        <section className="space-y-4">
          <h2 className="text-2xl font-bold tracking-tight text-slate-900">Shop by Category</h2>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4">
            {categories.map((category: Category) => (
              <Link
                key={category.id}
                href={`/category/${category.slug || category.id}`}
                className="p-4 rounded-xl border border-slate-200 bg-white hover:border-indigo-500 hover:shadow-sm text-center transition-all group"
              >
                <span className="block font-medium text-slate-800 group-hover:text-indigo-600 truncate">
                  {category.name}
                </span>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Latest Catalog Grid */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-2xl font-bold tracking-tight text-slate-900">Latest Arrivals</h2>
          <Link
            href="/products"
            className="text-sm font-medium text-indigo-600 hover:text-indigo-500"
          >
            Explore catalog &rarr;
          </Link>
        </div>
        {recentProducts.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
            {recentProducts.map((product: Product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        ) : (
          <div className="p-12 text-center border border-dashed border-slate-200 rounded-xl bg-white">
            <p className="text-slate-500">No products found at the moment.</p>
          </div>
        )}
      </section>
    </div>
  );
}
