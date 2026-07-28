import { NextRequest, NextResponse } from "next/server";

const PROTECTED_PREFIXES = [
  "/account",
  "/addresses",
  "/chat-history",
  "/checkout",
  "/notifications",
  "/orders",
  "/profile",
  "/settings",
  "/wishlist",
];

const AUTH_PREFIXES = ["/login", "/register", "/forgot-password", "/reset-password"];

const ACCESS_TOKEN_COOKIE = "access_token";
const REFRESH_TOKEN_COOKIE = "refresh_token";

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  const hasSession =
    request.cookies.has(ACCESS_TOKEN_COOKIE) || request.cookies.has(REFRESH_TOKEN_COOKIE);

  const isProtected = PROTECTED_PREFIXES.some((prefix) => pathname.startsWith(prefix));
  const isAuthPage = AUTH_PREFIXES.some((prefix) => pathname.startsWith(prefix));

  if (isProtected && !hasSession) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("redirect", pathname);
    return NextResponse.redirect(loginUrl);
  }

  if (isAuthPage && hasSession) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/account/:path*",
    "/addresses/:path*",
    "/chat-history/:path*",
    "/checkout/:path*",
    "/notifications/:path*",
    "/orders/:path*",
    "/profile/:path*",
    "/settings/:path*",
    "/wishlist/:path*",
    "/login",
    "/register",
    "/forgot-password",
    "/reset-password",
  ],
};
