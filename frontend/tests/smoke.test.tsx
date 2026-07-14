import React from "react";
import { render, screen } from "@testing-library/react";
import HomePage from "@/app/page";

describe("Next.js Storefront Root Application Smoke Test Suite", () => {
  it("should successfully mount and render the main home page component layout without throwing errors", () => {
    const { container } = render(<HomePage />);

    // Assert structural visibility matches layout expectations
    const headingElement = screen.getByRole("heading", {
      level: 1,
      name: /e-commerce storefront/i,
    });
    expect(headingElement).toBeInTheDocument();

    const actionButton = screen.getByRole("button", { name: /browse products/i });
    expect(actionButton).toBeInTheDocument();

    // Verify container generated real HTML rendering paths
    expect(container.firstChild).toBeInTheDocument();
  });
});
