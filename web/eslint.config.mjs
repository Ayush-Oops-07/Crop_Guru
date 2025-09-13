import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

export default [
  // Next.js defaults
  ...compat.extends("next/core-web-vitals", "next/typescript"),

  // Custom rules
  {
    rules: {
      "@typescript-eslint/no-explicit-any": "off",   // disable "Unexpected any"
      "@typescript-eslint/no-unused-vars": "off",   // disable unused vars
      "react/no-unescaped-entities": "off",         // disable quotes escaping
      "react-hooks/exhaustive-deps": "off",         // disable hook deps check
      "@next/next/no-img-element": "off"            // disable <img> instead of <Image />
    },
  },

  // Ignore big folders
  {
    ignores: [
      "node_modules/**",
      ".next/**",
      "out/**",
      "build/**",
      "next-env.d.ts",
    ],
  },
];
