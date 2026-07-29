import * as React from "react";
import { cn } from "@/lib/utils";

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        ref={ref}
        className={cn(
          "flex h-10 w-full rounded-lg border border-[#10151F]/15 bg-white px-3 py-2 text-sm text-[#10151F]",
          "placeholder:text-[#10151F]/40",
          "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#1F6F63] focus-visible:border-[#1F6F63]",
          "disabled:cursor-not-allowed disabled:opacity-50",
          "aria-invalid:border-red-400 aria-invalid:ring-red-200",
          className
        )}
        {...props}
      />
    );
  }
);
Input.displayName = "Input";

export { Input };
