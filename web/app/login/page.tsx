"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import BackButton from "../components/BackButton";

export default function LoginPage() {
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    try {
      const res = await fetch("https://crop-guru.onrender.com/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ phone, password }),
      });

      const data = await res.json();

      if (res.ok) {
        localStorage.setItem("farmer_name", data.farmer_name);
        localStorage.setItem("farmer_id", data.farmer_id);
        localStorage.setItem("access_token", data.access_token);

        // Redirect to feature if saved
        const redirectLink = localStorage.getItem("redirectAfterLogin");
        if (redirectLink) {
          localStorage.removeItem("redirectAfterLogin");
          router.push(redirectLink);
        } else {
          router.push("/"); // Otherwise home
        }
      } else {
        alert(data.detail || "Login failed");
      }
    } catch (error) {
      console.error("Login error:", error);
      alert("Something went wrong during login.");
    }
  }

  return (
    <div className="flex flex-col items-center min-h-screen bg-green-50 p-4">
      <div className="w-full max-w-md mb-4">
        <BackButton />
      </div>

      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md space-y-4"
      >
        <h1 className="text-2xl font-bold text-center">Farmer Login</h1>

        <input
          type="text"
          placeholder="Phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          className="w-full border p-2 rounded"
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-2 rounded"
          required
        />

        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded w-full"
        >
          Login
        </button>

        <p className="text-sm text-center">
          Don’t have an account?{" "}
          <a href="/signup" className="text-green-600 underline">
            Sign up
          </a>
        </p>
      </form>
    </div>
  );
}
