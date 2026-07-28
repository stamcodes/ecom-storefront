// File: frontend/app/(auth)/login/page.tsx
"use client";

import { useState, useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema, LoginSchemaType } from "@/lib/validation/auth";
import { useAuthStore } from "@/lib/stores/authStore";
import { ApiError } from "@/lib/api/client";

export default function LoginPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const redirectTo = searchParams.get("redirect") || "/account";
  const justRegistered = searchParams.get("registered") === "true";
  const login = useAuthStore((state) => state.login);
  const isLoading = useAuthStore((state) => state.isLoading);
  const [formError, setFormError] = useState<string | null>(null);
  const [justVerified, setJustVerified] = useState(false);

  useEffect(() => {
    // Read the same-session flag set by verify-email/page.tsx immediately after
    // a real, successful API verification. Query params are never trusted for
    // this, since ?verified=true could be typed into the address bar by anyone.
    if (typeof window !== "undefined") {
      const flag = sessionStorage.getItem("emailJustVerified");
      if (flag === "true") {
        setJustVerified(true);
        sessionStorage.removeItem("emailJustVerified"); // one-time use only
      }
    }
  }, []);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginSchemaType>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginSchemaType) => {
    setFormError(null);
    try {
      await login(data);
      router.replace(redirectTo);
    } catch (error) {
      if (error instanceof ApiError) {
        setFormError(error.message);
      } else {
        setFormError("We couldn't sign you in. Please try again.");
      }
    }
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900">Sign In</h1>
          <p className="mt-1 text-sm text-gray-600">
            Welcome back! Please enter your details to log in.
          </p>
        </div>

        {justVerified && (
          <div className="rounded-md bg-green-50 px-4 py-3 text-sm text-green-700" role="status">
            Email verified, enter credentials to login.
          </div>
        )}

        {justRegistered && !justVerified && (
          <div className="rounded-md bg-blue-50 px-4 py-3 text-sm text-blue-700" role="status">
            Account created. Please verify your email before logging in.
          </div>
        )}

        <form onSubmit={handleSubmit(onSubmit)} noValidate className="space-y-4">
          {formError && (
            <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
              {formError}
            </div>
          )}

          <div>
            <label htmlFor="email" className="mb-1 block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              id="email"
              type="email"
              autoComplete="email"
              {...register("email")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.email && <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>}
          </div>

          <div>
            <label htmlFor="password" className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              id="password"
              type="password"
              autoComplete="current-password"
              {...register("password")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.password && (
              <p className="mt-1 text-sm text-red-600">{errors.password.message}</p>
            )}
          </div>

          <div className="flex justify-end">
            <Link href="/forgot-password" className="text-sm text-gray-600 hover:text-gray-900">
              Forgot password?
            </Link>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {isLoading ? "Signing in..." : "Sign In"}
          </button>
        </form>

        <p className="text-center text-sm text-gray-600">
          Don&apos;t have an account?{" "}
          <Link href="/register" className="font-medium text-gray-900 hover:underline">
            Create one
          </Link>
        </p>
      </div>
    </div>
  );
}
