import React from "react";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <div className="max-w-md w-full bg-white shadow-md rounded-lg p-8 border border-gray-200">
        <h1 className="text-2xl font-bold text-gray-900 mb-2">E-commerce Storefront</h1>
        <p className="text-gray-600 mb-4">
          Welcome to the Next.js automated code factory enterprise web store instance.
        </p>
        <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors">
          Browse Products
        </button>
      </div>
    </main>
  );
}
