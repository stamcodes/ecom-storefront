"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/lib/stores/authStore";

export default function AccountPage() {
  const router = useRouter();
  const { user, logout, fetchCurrentUser, isInitialized } = useAuthStore();
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  useEffect(() => {
    if (!isInitialized) {
      fetchCurrentUser();
    }
  }, [isInitialized, fetchCurrentUser]);

  const handleLogout = async () => {
    setIsLoggingOut(true);
    try {
      // Clear store state & call backend logout endpoint
      await logout();
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      // Force a full location change to /login to ensure all middleware,
      // client router cache, and session cookies are completely cleared.
      if (typeof window !== "undefined") {
        window.location.href = "/login";
      }
    }
  };

  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between border-b border-gray-200 pb-6 mb-8 gap-4">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Account Dashboard</h1>
          <p className="mt-1 text-sm text-gray-600">Manage your profile and session settings.</p>
        </div>

        <button
          onClick={handleLogout}
          disabled={isLoggingOut}
          className="inline-flex items-center justify-center rounded-md bg-red-600 px-4 py-2.5 text-sm font-medium text-white shadow-sm transition hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {isLoggingOut ? (
            <span className="flex items-center gap-2">
              <svg className="h-4 w-4 animate-spin text-white" viewBox="0 0 24 24" fill="none">
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                />
              </svg>
              Logging out...
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                />
              </svg>
              Sign Out
            </span>
          )}
        </button>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Profile Card */}
        <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">User Details</h2>
          {user ? (
            <dl className="space-y-3 text-sm">
              <div>
                <dt className="text-gray-500 font-medium">Full Name</dt>
                <dd className="mt-0.5 text-gray-900">{user.name || "N/A"}</dd>
              </div>
              <div>
                <dt className="text-gray-500 font-medium">Email Address</dt>
                <dd className="mt-0.5 text-gray-900">{user.email}</dd>
              </div>
              <div>
                <dt className="text-gray-500 font-medium">Account Status</dt>
                <dd className="mt-0.5 inline-flex items-center rounded-full bg-green-50 px-2.5 py-0.5 text-xs font-medium text-green-700">
                  {user.emailVerified ? "Verified User" : "Active Session"}
                </dd>
              </div>
            </dl>
          ) : (
            <p className="text-sm text-gray-500">Loading user info...</p>
          )}
        </div>

        {/* Quick Links / Session Info */}
        <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm flex flex-col justify-between">
          <div>
            <h2 className="text-lg font-semibold text-gray-900 mb-2">Session Control</h2>
            <p className="text-sm text-gray-600 mb-4">
              Signing out will end your active session, clear cached credentials, and redirect you
              back to the sign-in page.
            </p>
          </div>
          <div className="pt-4 border-t border-gray-100">
            <button
              onClick={handleLogout}
              disabled={isLoggingOut}
              className="w-full text-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition focus:outline-none"
            >
              Log out of account
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
