"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useAuthStore } from "@/lib/stores/authStore";

export default function HomePage() {
  const { user, isAuthenticated, logout, fetchCurrentUser, isInitialized } = useAuthStore();
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  useEffect(() => {
    if (!isInitialized) {
      fetchCurrentUser();
    }
  }, [isInitialized, fetchCurrentUser]);

  const handleLogout = async () => {
    setIsLoggingOut(true);
    try {
      await logout();
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      if (typeof window !== "undefined") {
        localStorage.clear();
        sessionStorage.clear();
        window.location.href = "/login";
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header / Navbar */}
      <header className="sticky top-0 z-10 bg-white border-b border-gray-200 shadow-sm">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <Link href="/" className="text-xl font-bold text-gray-900 tracking-tight">
            🛍️ StoreFront
          </Link>

          <nav className="flex items-center gap-4">
            <Link href="/products" className="text-sm font-medium text-gray-700 hover:text-gray-900 transition">
              Products
            </Link>
            <Link href="/categories" className="text-sm font-medium text-gray-700 hover:text-gray-900 transition">
              Categories
            </Link>
            <Link href="/cart" className="text-sm font-medium text-gray-700 hover:text-gray-900 transition">
              Cart
            </Link>

            {isAuthenticated && user ? (
              <div className="flex items-center gap-3 pl-4 border-l border-gray-200">
                <Link href="/account" className="text-sm font-medium text-gray-900 hover:underline">
                  {user.name || user.email}
                </Link>
                <button
                  onClick={handleLogout}
                  disabled={isLoggingOut}
                  className="rounded-md bg-red-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm hover:bg-red-700 transition focus:outline-none disabled:opacity-60"
                >
                  {isLoggingOut ? "Logging out..." : "Logout"}
                </button>
              </div>
            ) : (
              <div className="flex items-center gap-2 pl-4 border-l border-gray-200">
                <Link
                  href="/login"
                  className="rounded-md border border-gray-300 bg-white px-3 py-1.5 text-xs font-semibold text-gray-700 hover:bg-gray-50 transition"
                >
                  Sign In
                </Link>
                <Link
                  href="/register"
                  className="rounded-md bg-gray-900 px-3 py-1.5 text-xs font-semibold text-white hover:bg-gray-800 transition"
                >
                  Register
                </Link>
              </div>
            )}
          </nav>
        </div>
      </header>

      {/* Main Hero Content */}
      <main className="flex-1 mx-auto max-w-4xl px-4 py-16 text-center flex flex-col items-center justify-center">
        <div className="rounded-2xl bg-white p-8 sm:p-12 shadow-sm border border-gray-200 w-full space-y-6">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
            Welcome to E-Commerce Storefront
          </h1>
          <p className="text-base text-gray-600 max-w-xl mx-auto">
            Discover curated items, seamless checkout, and account management built with Next.js and FastAPI.
          </p>

          {/* User Session Banner */}
          {isAuthenticated && user && (
            <div className="my-6 rounded-xl bg-blue-50 border border-blue-100 p-4 text-left sm:flex sm:items-center sm:justify-between gap-4">
              <div>
                <p className="text-xs font-bold uppercase tracking-wider text-blue-600">Logged In Session</p>
                <p className="text-sm font-semibold text-gray-900 mt-0.5">{user.name || "Customer"}</p>
                <p className="text-xs text-gray-600">{user.email}</p>
              </div>
              <div className="mt-3 sm:mt-0 flex gap-2">
                <Link
                  href="/account"
                  className="inline-flex items-center rounded-lg border border-blue-200 bg-white px-3.5 py-2 text-xs font-medium text-blue-700 hover:bg-blue-50 transition"
                >
                  Account Dashboard
                </Link>
                <button
                  onClick={handleLogout}
                  disabled={isLoggingOut}
                  className="inline-flex items-center rounded-lg bg-red-600 px-3.5 py-2 text-xs font-semibold text-white hover:bg-red-700 transition disabled:opacity-60"
                >
                  {isLoggingOut ? "Logging out..." : "Sign Out"}
                </button>
              </div>
            </div>
          )}

          {/* Action CTAs */}
          <div className="flex flex-wrap justify-center gap-4 pt-2">
            <Link
              href="/products"
              className="rounded-lg bg-gray-900 px-6 py-3 text-sm font-semibold text-white shadow hover:bg-gray-800 transition"
            >
              Browse Products
            </Link>
            {!isAuthenticated && (
              <Link
                href="/login"
                className="rounded-lg border border-gray-300 bg-white px-6 py-3 text-sm font-semibold text-gray-700 shadow-sm hover:bg-gray-50 transition"
              >
                Sign In to Account
              </Link>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
