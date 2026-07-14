---
globs: "*"
---

# Core Project Configuration & Architecture

## Tech Stack

- Frontend Framework: Next.js (App Router, Version 15+)
- Language: TypeScript (Strict Type Checking)
- Styling: Tailwind CSS (Utility-first configuration)
- State Management: Zustand (Global Client-Side Stores)
- Form Handling: React Hook Form
- Validation: Zod (Schema validation for forms and API responses)
- Payments: Stripe (@stripe/stripe-js and @stripe/react-stripe-js)
- Backend: External FastAPI Backend Engine

## Folder Layout Structure

- `/app`: Pages, layouts, and route handlers.
- `/components`: Reusable global UI elements (buttons, inputs, modals).
- `/lib`: Modular code utilities.
- `/lib/api`: HTTP and WebSocket connection clients for FastAPI.
- `/lib/stores`: Zustand global state store modules.
- `/hooks`: Custom stateful React hooks.
- `/types`: Explicit TypeScript data interfaces and types.
- `/tests`: Unit, integration, and End-to-End test suites.

## Strict Production Guardrails

1. NO PLACEHOLDERS: Never output placeholders, partial modifications, or comments like `// TODO: Implement logic` or `// ... rest of code here`. Write out every file completely.
2. NO PROSE IN GENERATION: When acting as a code generator, skip conversational pleasantries, introductory text, and closing summaries. Output only the file path indicator followed by the raw code block.
3. ERROR HANDLING: Every API network operation and state transaction must be wrapped inside defensive `try/catch` processing blocks with strict user-facing fallback messages.
4. TYPE SAFETY: Avoid the use of `any` types. Every utility parameter, API response payload, and form state must be strictly declared with a definitive TypeScript interface or type.
5. BEST PRACTICES: Always follow elite, production-grade software engineering practices. Avoid quick fixes, lazy shortcuts, and architectural hacks. Write clean, modular, and highly scalable logic.
6. COMPREHENSIVE GUIDANCE: Do not give vague or high-level instructions. Instead of stating "make changes" or "write tests," explicitly guide step by step on how to execute those changes and write out the exact, actionable code blocks or testing logic required.
