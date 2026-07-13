import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4 text-center">
      <h1 className="text-6xl font-extrabold text-gray-900">404</h1>
      <h2 className="mt-4 text-xl font-bold text-gray-700">Page Not Found</h2>
      <p className="mt-2 text-base text-gray-500">
        Sorry, we couldn’t find the page you’re looking for.
      </p>
      <div className="mt-6">
        <Link
          href="/"
          className="inline-flex items-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-gray-800 focus:outline-none"
        >
          Go back home
        </Link>
      </div>
    </div>
  );
}
