"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import BackButton from "../components/BackButton";

export default function SignupPage() {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [location, setLocation] = useState("");
  const [crops, setCrops] = useState("");
  const router = useRouter();

  const BACKEND_URL ="https://crop-guru.onrender.com";

  async function handleSignup(e: React.FormEvent) {
    e.preventDefault();
    try {
      // Signup request
      const res = await fetch(`${BACKEND_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, phone, password, location, crops }),
      });

      if (res.ok) {
        alert("Signup successful! Logging you in...");

        // Login request (same backend)
        const loginRes = await fetch(`${BACKEND_URL}/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ phone, password }),
        });

        if (loginRes.ok) {
          const loginData = await loginRes.json();
          localStorage.setItem("farmer_name", loginData.farmer_name);
          localStorage.setItem("farmer_id", loginData.farmer_id);
          localStorage.setItem("access_token", loginData.access_token);
          router.push("/");
        } else {
          alert("Automatic login failed. Please try logging in manually.");
          router.push("/login");
        }
      } else {
        const data = await res.json();
        alert(data.detail || "Signup failed");
      }
    } catch (error) {
      console.error("Signup error:", error);
      alert("Something went wrong during signup.");
    }
  }

  return (
    <div className="flex flex-col items-center min-h-screen bg-green-50 p-4">
      <div className="w-full max-w-md mb-4">
        <BackButton />
      </div>

      <form
        onSubmit={handleSignup}
        className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md space-y-4"
      >
        <h1 className="text-2xl font-bold text-center">Farmer Sign Up</h1>

        <input
          type="text"
          placeholder="Full Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full border p-2 rounded"
          required
        />

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

        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="w-full border p-2 rounded"
        />

        <input
          type="text"
          placeholder="Crops (e.g., Wheat, Rice)"
          value={crops}
          onChange={(e) => setCrops(e.target.value)}
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded w-full"
        >
          Sign Up
        </button>

        <p className="text-sm text-center">
          Already have an account?{" "}
          <a href="/login" className="text-green-600 underline">
            Login
          </a>
        </p>
      </form>
    </div>
  );
}
