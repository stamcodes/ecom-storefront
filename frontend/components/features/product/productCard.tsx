import Link from "next/link";
import { Button } from "@/components/ui/button";

interface Product {
  id: string | number;
  name: string;
  slug?: string;
  price: number;
  image_url?: string;
  category_name?: string;
  rating?: number;
  reviewCount?: number;
}

interface ProductCardProps {
  product: Product;
}

export function ProductCard({ product }: ProductCardProps) {
  const rating = product.rating ?? null;
  const href = `/products/${product.slug ?? product.id}`;

  return (
    <div className="group relative bg-white border border-[#10151F]/10 rounded-xl overflow-hidden hover:border-[#1F6F63]/40 hover:shadow-[0_8px_24px_-8px_rgba(16,21,31,0.15)] transition-all flex flex-col">
      <div className="aspect-square bg-[#F1EFE8] relative overflow-hidden flex items-center justify-center">
        {product.image_url ? (
          <img
            src={product.image_url}
            alt={product.name}
            className="w-full h-full object-cover object-center group-hover:scale-[1.03] transition-transform duration-300"
          />
        ) : (
          <div className="flex flex-col items-center gap-1 text-[#10151F]/35">
            <svg
              width="28"
              height="28"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
            >
              <rect x="3" y="3" width="18" height="18" rx="2" />
              <circle cx="8.5" cy="8.5" r="1.5" />
              <path d="M21 15l-5-5L5 21" />
            </svg>
            <span className="text-[11px] font-medium">No product image</span>
          </div>
        )}
        {product.category_name && (
          <span className="absolute top-2 left-2 bg-white/90 text-[10px] font-semibold tracking-wide text-[#1F6F63] uppercase px-2 py-1 rounded-full">
            {product.category_name}
          </span>
        )}
      </div>

      <div className="p-4 flex flex-col gap-2 flex-1">
        <h3 className="text-sm font-semibold text-[#10151F] leading-snug line-clamp-2">
          <Link href={href} className="hover:text-[#1F6F63] transition-colors">
            <span aria-hidden="true" className="absolute inset-0" />
            {product.name}
          </Link>
        </h3>

        <div className="flex items-center gap-1 text-xs">
          {rating !== null ? (
            <>
              <div className="flex text-[#E8A23D]" aria-hidden="true">
                {Array.from({ length: 5 }).map((_, i) => (
                  <svg
                    key={i}
                    width="13"
                    height="13"
                    viewBox="0 0 20 20"
                    fill={i < Math.round(rating) ? "currentColor" : "none"}
                    stroke="currentColor"
                    strokeWidth="1"
                  >
                    <path d="M10 1.5l2.6 5.6 6.1.6-4.6 4.1 1.3 6-5.4-3.1-5.4 3.1 1.3-6-4.6-4.1 6.1-.6L10 1.5z" />
                  </svg>
                ))}
              </div>
              <span className="text-[#10151F]/60 font-medium">
                {rating.toFixed(1)}
                {product.reviewCount ? ` (${product.reviewCount})` : ""}
              </span>
            </>
          ) : (
            <span className="text-[#10151F]/40 font-medium">No ratings yet</span>
          )}
        </div>

        <div className="mt-auto flex items-center justify-between pt-2 gap-2">
          <p className="text-base font-bold text-[#10151F]">${Number(product.price).toFixed(2)}</p>
          <Button
            size="sm"
            className="relative z-10 bg-[#10151F] hover:bg-[#1F6F63] text-white text-xs font-semibold rounded-full px-4"
          >
            Buy now
          </Button>
        </div>
      </div>
    </div>
  );
}
