import { z } from "zod";

export const addressSchema = z.object({
  title: z.string().min(1, "Address label title is required."),
  streetAddress: z.string().min(1, "Street address is required."),
  apartment: z.string().optional(),
  city: z.string().min(1, "City is required."),
  state: z.string().min(1, "State or province is required."),
  postalCode: z.string().min(1, "Postal code is required."),
  country: z.string().min(1, "Country name is required."),
  isDefault: z.boolean().default(false),
});

export type AddressSchemaType = z.infer<typeof addressSchema>;
