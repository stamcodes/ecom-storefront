import Link from "next/link";

interface Product {
  id: string | number;
  name: string;
  slug?: string;
  price: number;
  image_url?: string;
  category_name?: string;
}

interface ProductCardProps {
  product: Product;
}

export function ProductCard({ product }: ProductCardProps) {
  return (
    <div className="group relative bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md hover:border-indigo-300 transition-all flex flex-col justify-between">
      <div>
        {/* Image Container */}
        <div className="aspect-square bg-slate-100 relative overflow-hidden">
          {product.image_url ? (
            <img
              src={product.image_url}
              alt={product.name}
              className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300"
            />
          ) : (
            <div className="w-full h-full flex items-center justify-center text-slate-400 text-xs">
              No Image Available
            </div>
          )}
        </div>

        {/* Info */}
        <div className="p-4 space-y-1">
          {product.category_name && (
            <span className="text-[10px] font-semibold tracking-wider text-indigo-600 uppercase">
              {product.category_name}
            </span>
          )}
          <h3 className="text-sm font-semibold text-slate-900 group-hover:text-indigo-600 line-clamp-1 transition-colors">
            <Link href={`/products/${product.slug || product.id}`}>
              <span aria-hidden="true" className="absolute inset-0" />
              {product.name}
            </Link>
          </h3>
        </div>
      </div>

      {/* Footer / Price */}
      <div className="p-4 pt-0 flex items-center justify-between">
        <p className="text-base font-bold text-slate-900">${Number(product.price).toFixed(2)}</p>
        <span className="text-xs font-medium text-indigo-600 group-hover:underline">
          View details &rarr;
        </span>
      </div>
    </div>
  );
}
