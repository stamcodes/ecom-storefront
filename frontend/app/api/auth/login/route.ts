import { NextResponse } from "next/server";

export async function POST() {
  return NextResponse.json({ message: "Login via /customer/auth/login API" });
}
