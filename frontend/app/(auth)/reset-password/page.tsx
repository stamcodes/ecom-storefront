// File: frontend/app/(auth)/reset-password/page.tsx
"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { resetPasswordSchema, ResetPasswordSchemaType } from "@/lib/validation/auth";
import { resetPassword } from "@/lib/api/auth";
import { ApiError } from "@/lib/api/client";

export default function ResetPasswordPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token") || "";

  const [formError, setFormError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ResetPasswordSchemaType>({
    resolver: zodResolver(resetPasswordSchema),
    defaultValues: { token, password: "", confirmPassword: "" },
  });

  const onSubmit = async (data: ResetPasswordSchemaType) => {
    setFormError(null);
    setIsSubmitting(true);
    try {
      await resetPassword({ ...data, token });
      setSuccess(true);
      setTimeout(() => router.replace("/login"), 2000);
    } catch (error) {
      if (error instanceof ApiError) {
        setFormError(error.message);
      } else {
        setFormError("Something went wrong. Please try again.");
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!token) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
        <div className="w-full max-w-md space-y-4 text-center">
          <h1 className="text-2xl font-bold text-gray-900">Reset Password</h1>
          <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
            This reset link is missing or invalid. Please request a new one.
          </div>
          <Link
            href="/forgot-password"
            className="inline-block font-medium text-gray-900 hover:underline"
          >
            Request new reset link
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900">Reset Password</h1>
          <p className="mt-1 text-sm text-gray-600">Please enter your new password below.</p>
        </div>

        {success ? (
          <div className="rounded-md bg-green-50 px-4 py-3 text-sm text-green-700" role="status">
            Password reset successfully. Redirecting to login...
          </div>
        ) : (
          <form onSubmit={handleSubmit(onSubmit)} noValidate className="space-y-4">
            {formError && (
              <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
                {formError}
              </div>
            )}

            <input type="hidden" {...register("token")} value={token} />

            <div>
              <label htmlFor="password" className="mb-1 block text-sm font-medium text-gray-700">
                New Password
              </label>
              <input
                id="password"
                type="password"
                autoComplete="new-password"
                {...register("password")}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
              />
              {errors.password && (
                <p className="mt-1 text-sm text-red-600">{errors.password.message}</p>
              )}
            </div>

            <div>
              <label
                htmlFor="confirmPassword"
                className="mb-1 block text-sm font-medium text-gray-700"
              >
                Confirm New Password
              </label>
              <input
                id="confirmPassword"
                type="password"
                autoComplete="new-password"
                {...register("confirmPassword")}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
              />
              {errors.confirmPassword && (
                <p className="mt-1 text-sm text-red-600">{errors.confirmPassword.message}</p>
              )}
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {isSubmitting ? "Resetting..." : "Reset Password"}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
