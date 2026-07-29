"use client";

import { useState, useMemo, useRef, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { ProductCard } from "@/components/features/product/productCard";

interface MockProduct {
  id: number;
  name: string;
  slug: string;
  price: number;
  image_url: string;
  category_name: string;
  rating: number;
  reviewCount: number;
}

const PRODUCTS: MockProduct[] = [
  {
    id: 1,
    name: "Aria Wireless Headphones",
    slug: "aria-wireless-headphones",
    price: 89.99,
    image_url: "https://picsum.photos/seed/prod1/600/600",
    category_name: "Electronics",
    rating: 4.5,
    reviewCount: 214,
  },
  {
    id: 2,
    name: "Nordic Ceramic Mug Set",
    slug: "nordic-ceramic-mug-set",
    price: 34.5,
    image_url: "https://picsum.photos/seed/prod2/600/600",
    category_name: "Home",
    rating: 4.8,
    reviewCount: 96,
  },
  {
    id: 3,
    name: "Trailblaze Running Shoes",
    slug: "trailblaze-running-shoes",
    price: 64.0,
    image_url: "https://picsum.photos/seed/prod3/600/600",
    category_name: "Footwear",
    rating: 4.2,
    reviewCount: 358,
  },
  {
    id: 4,
    name: "Lumen Desk Lamp",
    slug: "lumen-desk-lamp",
    price: 42.99,
    image_url: "https://picsum.photos/seed/prod4/600/600",
    category_name: "Home",
    rating: 4.6,
    reviewCount: 71,
  },
  {
    id: 5,
    name: "Voyager Backpack 28L",
    slug: "voyager-backpack-28l",
    price: 76.0,
    image_url: "https://picsum.photos/seed/prod5/600/600",
    category_name: "Bags",
    rating: 4.7,
    reviewCount: 132,
  },
  {
    id: 6,
    name: "Pulse Fitness Tracker",
    slug: "pulse-fitness-tracker",
    price: 129.99,
    image_url: "https://picsum.photos/seed/prod6/600/600",
    category_name: "Electronics",
    rating: 4.3,
    reviewCount: 480,
  },
  {
    id: 7,
    name: "Meadow Cotton Throw Blanket",
    slug: "meadow-cotton-throw-blanket",
    price: 28.75,
    image_url: "https://picsum.photos/seed/prod7/600/600",
    category_name: "Home",
    rating: 4.9,
    reviewCount: 58,
  },
  {
    id: 8,
    name: "Orbit Bluetooth Speaker",
    slug: "orbit-bluetooth-speaker",
    price: 54.0,
    image_url: "https://picsum.photos/seed/prod8/600/600",
    category_name: "Electronics",
    rating: 4.1,
    reviewCount: 267,
  },
  {
    id: 9,
    name: "Cascade Rain Jacket",
    slug: "cascade-rain-jacket",
    price: 98.5,
    image_url: "https://picsum.photos/seed/prod9/600/600",
    category_name: "Apparel",
    rating: 4.4,
    reviewCount: 145,
  },
  {
    id: 10,
    name: "Basecamp Enamel Cookware Set",
    slug: "basecamp-enamel-cookware-set",
    price: 112.0,
    image_url: "https://picsum.photos/seed/prod10/600/600",
    category_name: "Kitchen",
    rating: 4.6,
    reviewCount: 89,
  },
];

function rotate(arr: MockProduct[], by: number): MockProduct[] {
  return [...arr.slice(by), ...arr.slice(0, by)];
}

const CATEGORY_ROWS: {
  title: string;
  href: string;
  products: MockProduct[];
  featured?: boolean;
}[] = [
  { title: "Featured picks", href: "/products", products: rotate(PRODUCTS, 0), featured: true },
  { title: "Electronics", href: "/category/electronics", products: rotate(PRODUCTS, 3) },
  { title: "Home essentials", href: "/category/home", products: rotate(PRODUCTS, 6) },
  { title: "Apparel and footwear", href: "/category/apparel", products: rotate(PRODUCTS, 2) },
  { title: "New arrivals", href: "/products", products: rotate(PRODUCTS, 5) },
];

const NAV_LINKS = [
  { label: "Shop", href: "/products" },
  { label: "Categories", href: "/categories" },
  { label: "Deals", href: "/products" },
  { label: "About", href: "/about" },
  { label: "Contact", href: "/contact" },
];

/* ---------- Navigation loader ---------- */
function useNavLoader() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const navigate = (href: string) => {
    setLoading(true);
    router.push(href);
  };

  useEffect(() => {
    if (!loading) return;
    const timeout = setTimeout(() => setLoading(false), 5000);
    return () => clearTimeout(timeout);
  }, [loading]);

  return { loading, navigate };
}

function TopLoader({ active }: { active: boolean }) {
  if (!active) return null;
  return (
    <div className="fixed top-0 left-0 right-0 z-[100] h-[3px] bg-transparent overflow-hidden">
      <div className="h-full w-1/3 bg-[#1F6F63] animate-[loaderSlide_0.9s_ease-in-out_infinite] rounded-full" />
      <style jsx>{`
        @keyframes loaderSlide {
          0% {
            transform: translateX(-100%);
          }
          50% {
            transform: translateX(150%);
          }
          100% {
            transform: translateX(300%);
          }
        }
      `}</style>
    </div>
  );
}

/* ---------- Search with autosuggest ---------- */
function SearchBar({ className }: { className?: string }) {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const wrapperRef = useRef<HTMLDivElement>(null);

  const matches = useMemo(() => {
    if (!query.trim()) return [];
    const q = query.trim().toLowerCase();
    return PRODUCTS.filter((p) => p.name.toLowerCase().includes(q)).slice(0, 6);
  }, [query]);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div ref={wrapperRef} className={`relative ${className ?? ""}`}>
      <form action="/search" className="flex items-stretch w-full">
        <input
          type="text"
          name="q"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setOpen(true);
          }}
          onFocus={() => query && setOpen(true)}
          placeholder="Search products, brands, categories"
          autoComplete="off"
          className="flex-1 bg-white border border-[#10151F]/15 rounded-l-lg px-4 py-3 text-sm placeholder:text-[#10151F]/40 focus:outline-none focus:ring-2 focus:ring-[#E8A23D]"
        />
        <button
          type="submit"
          className="bg-[#10151F] text-white text-sm font-semibold px-6 rounded-r-lg hover:bg-[#1F6F63] transition-colors"
        >
          Search
        </button>
      </form>

      {open && query.trim() && (
        <div className="absolute left-0 right-0 top-full mt-2 bg-white border border-[#10151F]/10 rounded-lg shadow-lg overflow-hidden z-50 text-left animate-in fade-in slide-in-from-top-1 duration-150">
          {matches.length > 0 ? (
            matches.map((product) => (
              <Link
                key={product.id}
                href={`/products/${product.slug}`}
                onClick={() => setOpen(false)}
                className="flex items-center gap-3 px-4 py-2.5 hover:bg-[#F6F5F1] transition-colors"
              >
                <img
                  src={product.image_url}
                  alt={product.name}
                  className="w-8 h-8 rounded object-cover shrink-0"
                />
                <div className="min-w-0">
                  <p className="text-sm font-medium text-[#10151F] truncate">{product.name}</p>
                  <p className="text-xs text-[#10151F]/50">{product.category_name}</p>
                </div>
                <span className="ml-auto text-sm font-semibold text-[#10151F] shrink-0">
                  ${product.price.toFixed(2)}
                </span>
              </Link>
            ))
          ) : (
            <div className="px-4 py-3 text-sm text-[#10151F]/50">No products found</div>
          )}
        </div>
      )}
    </div>
  );
}

function Navbar({ onNavigate }: { onNavigate: (href: string) => void }) {
  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-[#10151F]/10">
      <div className="max-w-7xl mx-auto px-6 md:px-10 h-16 flex items-center justify-between gap-6">
        <Link href="/" className="text-lg font-bold tracking-tight text-[#10151F] shrink-0">
          Marketplace<span className="text-[#1F6F63]">.</span>
        </Link>

        <nav className="hidden md:flex items-center gap-6">
          {NAV_LINKS.map((link) => (
            <Link
              key={link.label}
              href={link.href}
              className="text-sm font-medium text-[#10151F]/70 hover:text-[#1F6F63] transition-colors"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="hidden lg:flex flex-1 max-w-md">
          <SearchBar className="w-full" />
        </div>

        <div className="flex items-center gap-3 shrink-0">
          <button
            onClick={() => onNavigate("/login")}
            className="hidden sm:inline text-sm font-medium text-[#10151F]/70 hover:text-[#1F6F63] transition-colors"
          >
            Sign in
          </button>
          <Link href="/cart" className="relative">
            <svg
              width="22"
              height="22"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.6"
            >
              <circle cx="9" cy="21" r="1" />
              <circle cx="20" cy="21" r="1" />
              <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
            </svg>
            <span className="absolute -top-2 -right-2 bg-[#1F6F63] text-white text-[10px] font-semibold rounded-full w-4 h-4 flex items-center justify-center">
              3
            </span>
          </Link>
          <Button
            onClick={() => onNavigate("/register")}
            className="bg-[#10151F] hover:bg-[#1F6F63] text-white text-sm font-semibold rounded-full px-5 transition-transform hover:scale-105 active:scale-95"
          >
            Sign up
          </Button>
        </div>
      </div>
    </header>
  );
}

function CategoryRow({
  title,
  href,
  products,
  featured,
}: {
  title: string;
  href: string;
  products: MockProduct[];
  featured?: boolean;
}) {
  const [expanded, setExpanded] = useState(false);
  const firstRow = products.slice(0, 5);
  const secondRow = products.slice(5, 10);
  const showSecondRow = featured || expanded;

  return (
    <section className="max-w-7xl mx-auto px-6 md:px-10 py-10">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold">{title}</h2>
        <Link
          href={href}
          className="text-sm font-semibold text-[#1F6F63] hover:underline transition-transform inline-block hover:translate-x-0.5"
        >
          View all &rarr;
        </Link>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4">
        {firstRow.map((product) => (
          <ProductCard key={`${title}-${product.id}`} product={product} />
        ))}
      </div>

      {showSecondRow && (
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4 mt-4 animate-in fade-in slide-in-from-top-2 duration-300">
          {secondRow.map((product) => (
            <ProductCard key={`${title}-${product.id}`} product={product} />
          ))}
        </div>
      )}

      {!featured && (
        <div className="flex flex-col items-center gap-3 mt-6">
          <Button
            onClick={() => setExpanded((prev) => !prev)}
            className="bg-[#1F6F63] hover:bg-[#18574d] text-white text-sm font-semibold rounded-full px-6 transition-all duration-200 hover:scale-105 active:scale-95 hover:shadow-md"
          >
            <span className="inline-flex items-center gap-1.5">
              {expanded ? "Show less" : "Show more"}
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                className={`transition-transform duration-300 ${expanded ? "rotate-180" : ""}`}
              >
                <path d="M6 9l6 6 6-6" />
              </svg>
            </span>
          </Button>
          {expanded && (
            <Link
              href="/categories"
              className="text-sm font-semibold text-[#10151F]/70 hover:text-[#1F6F63] transition-all hover:translate-x-0.5 animate-in fade-in duration-300"
            >
              View more similar products &rarr;
            </Link>
          )}
        </div>
      )}
    </section>
  );
}

export default function HomePage() {
  const categories = Array.from(new Set(PRODUCTS.map((p) => p.category_name)));
  const { loading, navigate } = useNavLoader();

  return (
    <div className="bg-[#F6F5F1] text-[#10151F]">
      <TopLoader active={loading} />
      <Navbar onNavigate={navigate} />

      {/* Hero */}
      <section className="border-b border-[#10151F]/10">
        <div className="max-w-4xl mx-auto px-6 md:px-10 pt-16 pb-14 flex flex-col items-center text-center gap-6">
          <span className="text-xs font-semibold tracking-[0.18em] uppercase text-[#1F6F63]">
            Everything, one storefront
          </span>
          <h1 className="text-[2.75rem] md:text-6xl font-bold leading-[0.95] tracking-tight">
            Whatever you're
            <br />
            looking for is
            <br />
            already here.
          </h1>
          <p className="text-[#10151F]/70 text-base max-w-md">
            Thousands of products across every category — electronics to essentials, restocked
            daily, shipped fast.
          </p>

          <SearchBar className="w-full max-w-lg pt-2" />

          <div className="flex flex-wrap justify-center gap-2 pt-2">
            {categories.map((category) => (
              <Link
                key={category}
                href={`/category/${encodeURIComponent(category.toLowerCase())}`}
                className="rounded-full px-4 py-2 text-sm font-medium bg-[#1F6F63] text-white hover:bg-[#18574d] transition-all hover:scale-105 active:scale-95"
              >
                {category}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Trust strip */}
      <section className="border-b border-[#10151F]/10 bg-white">
        <div className="max-w-7xl mx-auto px-6 md:px-10 py-4 flex flex-wrap justify-center gap-x-10 gap-y-2 text-xs font-medium text-[#10151F]/70">
          <span>Free shipping over $50</span>
          <span>30-day returns</span>
          <span>Secure checkout</span>
          <span>24/7 support</span>
        </div>
      </section>

      {/* Category rows */}
      {CATEGORY_ROWS.map((row) => (
        <CategoryRow
          key={row.title}
          title={row.title}
          href={row.href}
          products={row.products}
          featured={row.featured}
        />
      ))}

      {/* Footer band */}
      <section className="bg-[#10151F] text-white">
        <div className="max-w-7xl mx-auto px-6 md:px-10 py-10 flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
          <div>
            <h3 className="text-lg font-bold">Get 10% off your first order</h3>
            <p className="text-white/60 text-sm">Join our newsletter for deals and new arrivals.</p>
          </div>
          <form className="flex items-stretch w-full max-w-sm">
            <input
              type="email"
              placeholder="you@example.com"
              className="flex-1 bg-white/10 border border-white/20 rounded-l-lg px-4 py-3 text-sm text-white placeholder:text-white/40 focus:outline-none"
            />
            <button
              type="submit"
              className="bg-[#E8A23D] text-[#10151F] text-sm font-semibold px-6 rounded-r-lg hover:bg-[#f0b25a] transition-colors"
            >
              Subscribe
            </button>
          </form>
        </div>
      </section>
    </div>
  );
}
