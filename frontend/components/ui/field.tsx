import * as React from "react";
import { cn } from "@/lib/utils";

function FieldGroup({ className, ...props }: React.ComponentProps<"div">) {
  return <div className={cn("flex flex-col gap-5", className)} {...props} />;
}

function Field({ className, ...props }: React.ComponentProps<"div">) {
  return <div className={cn("flex flex-col gap-1.5", className)} {...props} />;
}

function FieldLabel({ className, ...props }: React.ComponentProps<"label">) {
  return <label className={cn("text-sm font-medium text-[#10151F]", className)} {...props} />;
}

function FieldDescription({ className, ...props }: React.ComponentProps<"p">) {
  return <p className={cn("text-xs text-[#10151F]/55", className)} {...props} />;
}

function FieldError({ className, ...props }: React.ComponentProps<"p">) {
  return <p className={cn("text-xs font-medium text-red-500", className)} {...props} />;
}

function FieldSeparator({ className, children, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={cn("relative flex items-center text-xs text-[#10151F]/45 my-1", className)}
      {...props}
    >
      <span className="flex-1 border-t border-[#10151F]/12" />
      {children && <span className="px-3">{children}</span>}
      <span className="flex-1 border-t border-[#10151F]/12" />
    </div>
  );
}

export { FieldGroup, Field, FieldLabel, FieldDescription, FieldError, FieldSeparator };
