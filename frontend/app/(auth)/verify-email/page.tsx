// File: frontend/app/(auth)/verify-email/page.tsx
"use client";

import { useEffect, useState, useCallback } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { verifyEmail, resendVerification } from "@/lib/api/auth";
import { ApiError } from "@/lib/api/client";

type Status = "pending" | "verifying" | "success" | "error" | "missing_token";

export default function VerifyEmailPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token");
  const isPending = searchParams.get("pending") === "true";
  const prefillEmail = searchParams.get("email") || "";

  const [status, setStatus] = useState<Status>(
    token ? "verifying" : isPending ? "pending" : "missing_token"
  );
  const [message, setMessage] = useState<string>("");
  const [resendEmail, setResendEmail] = useState(prefillEmail);
  const [resendStatus, setResendStatus] = useState<"idle" | "sending" | "sent">("idle");

  const runVerification = useCallback(async (t: string) => {
    setStatus("verifying");
    try {
      const res = await verifyEmail(t);
      setMessage(res.message);
      setStatus("success");
      // Set a one-time, same-browser-session flag proving verification actually
      // succeeded via the API. This is NOT derived from the URL, so it cannot
      // be spoofed by someone manually typing /login?verified=true.
      if (typeof window !== "undefined") {
        sessionStorage.setItem("emailJustVerified", "true");
      }
    } catch (error) {
      if (error instanceof ApiError) {
        setMessage(error.message);
      } else {
        setMessage("We couldn't verify your email. The link may be invalid or expired.");
      }
      setStatus("error");
    }
  }, []);

  useEffect(() => {
    if (token) {
      runVerification(token);
    }
  }, [token, runVerification]);

  const handleResend = async () => {
    if (!resendEmail) return;
    setResendStatus("sending");
    try {
      await resendVerification(resendEmail);
    } finally {
      setResendStatus("sent");
    }
  };

  const goToLogin = () => {
    // Navigate with plain client-side routing (no query param) — the
    // login page reads the sessionStorage flag set above instead.
    router.push("/login");
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Verify Email</h1>

        {status === "pending" && (
          <>
            <div className="rounded-md bg-blue-50 px-4 py-3 text-sm text-blue-700" role="status">
              We have sent a verification link to{" "}
              {prefillEmail ? <strong>{prefillEmail}</strong> : "your registered email address"}.
              Click the link in that email to verify your account.
            </div>
            <div className="pt-4 space-y-2 text-left">
              <label htmlFor="resendEmail" className="block text-sm font-medium text-gray-700">
                Didn&apos;t get it? Resend verification email
              </label>
              <input
                id="resendEmail"
                type="email"
                value={resendEmail}
                onChange={(e) => setResendEmail(e.target.value)}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
                placeholder="you@example.com"
              />
              <button
                onClick={handleResend}
                disabled={resendStatus === "sending" || resendStatus === "sent"}
                className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {resendStatus === "sent"
                  ? "If that email exists, a new link has been sent"
                  : resendStatus === "sending"
                    ? "Sending..."
                    : "Resend Verification Email"}
              </button>
            </div>
          </>
        )}

        {status === "missing_token" && (
          <>
            <p className="text-sm text-gray-600">
              We have sent a verification link to your registered email address. Click the link in
              that email to verify your account.
            </p>
            <div className="pt-4 space-y-2 text-left">
              <label htmlFor="resendEmail" className="block text-sm font-medium text-gray-700">
                Didn&apos;t get it? Resend verification email
              </label>
              <input
                id="resendEmail"
                type="email"
                value={resendEmail}
                onChange={(e) => setResendEmail(e.target.value)}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
                placeholder="you@example.com"
              />
              <button
                onClick={handleResend}
                disabled={resendStatus === "sending" || resendStatus === "sent"}
                className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {resendStatus === "sent"
                  ? "If that email exists, a new link has been sent"
                  : resendStatus === "sending"
                    ? "Sending..."
                    : "Resend Verification Email"}
              </button>
            </div>
          </>
        )}

        {status === "verifying" && (
          <p className="text-sm text-gray-600">Verifying your email, please wait...</p>
        )}

        {status === "success" && (
          <>
            <div className="rounded-md bg-green-50 px-4 py-3 text-sm text-green-700" role="status">
              {message}
            </div>
            <button
              onClick={goToLogin}
              className="inline-block font-medium text-gray-900 hover:underline"
            >
              Continue to Sign In
            </button>
          </>
        )}

        {status === "error" && (
          <>
            <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
              {message}
            </div>
            <Link
              href="/verify-email"
              className="inline-block font-medium text-gray-900 hover:underline"
            >
              Request a new verification link
            </Link>
          </>
        )}
      </div>
    </div>
  );
}
