import { LoginForm } from "@/components/features/auth/login-form";

export default function LoginPage() {
  return (
    <div className="grid min-h-svh lg:grid-cols-2 bg-[#F6F5F1]">
      <div className="flex flex-col gap-4 p-6 md:p-10">
        <div className="flex justify-center gap-2 md:justify-start">
          <a href="/" className="flex items-center gap-2 font-bold text-[#10151F]">
            <div className="flex size-6 items-center justify-center rounded-md bg-[#1F6F63] text-white text-xs font-bold">
              M
            </div>
            Marketplace
          </a>
        </div>
        <div className="flex flex-1 items-center justify-center">
          <div className="w-full max-w-sm">
            <LoginForm />
          </div>
        </div>
      </div>
      <div className="relative hidden bg-[#10151F] lg:flex lg:items-center lg:justify-center">
        <div className="text-center px-10">
          <h2 className="text-3xl font-bold text-white leading-tight">
            Whatever you're looking for is already here.
          </h2>
          <p className="text-white/60 text-sm mt-3">Sign in to pick up right where you left off.</p>
        </div>
      </div>
    </div>
  );
}
