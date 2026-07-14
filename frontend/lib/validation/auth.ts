import { z } from "zod";

export const loginSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
});

export const registerSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
  firstName: z.string().min(1, "First name is required."),
  lastName: z.string().min(1, "Last name is required."),
});

export const forgotPasswordSchema = z.object({
  email: z.string().email("Invalid email address format."),
});

export const resetPasswordSchema = z
  .object({
    token: z.string().min(1, "Reset token is required."),
    password: z.string().min(8, "Password must be at least 8 characters long."),
    confirmPassword: z.string().min(8, "Confirm password must be at least 8 characters long."),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords must match.",
    path: ["confirmPassword"],
  });

export type LoginSchemaType = z.infer<typeof loginSchema>;
export type RegisterSchemaType = z.infer<typeof registerSchema>;
export type ForgotPasswordSchemaType = z.infer<typeof forgotPasswordSchema>;
export type ResetPasswordSchemaType = z.infer<typeof resetPasswordSchema>;
