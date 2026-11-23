const backendUrl = process.env.RENDER_BACKEND_URL?.replace(/\/+$/, "");

if (!backendUrl) {
  throw new Error("RENDER_BACKEND_URL must be set in the environment.");
}

export const config = {
  services: {
    frontend: {
      root: "frontend/",
      framework: "vite",
    },
  },
  rewrites: [
    {
      source: "/api/:path*",
      destination: `${backendUrl}/api/:path*`,
    },
    {
      source: "/(.*)",
      destination: { service: "frontend" },
    },
  ],
};
