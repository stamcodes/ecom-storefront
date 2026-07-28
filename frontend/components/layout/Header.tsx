import Link from "next/link";
import { SearchBar } from "@/components/features/search/searchBar";

export function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        <Link href="/" className="font-extrabold text-xl tracking-tight text-indigo-600">
          Storefront
        </Link>

        <div className="flex-1 max-w-md hidden sm:block">
          <SearchBar />
        </div>

        <nav className="flex items-center space-x-6 text-sm font-medium">
          <Link href="/products" className="text-slate-700 hover:text-indigo-600 transition-colors">
            Products
          </Link>
          <Link href="/cart" className="text-slate-700 hover:text-indigo-600 transition-colors">
            Cart
          </Link>
          <Link href="/login" className="text-slate-700 hover:text-indigo-600 transition-colors">
            Login
          </Link>
          <Link
            href="/register"
            className="bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-md transition-colors shadow-sm"
          >
            Sign Up
          </Link>
        </nav>
      </div>
    </header>
  );
}
