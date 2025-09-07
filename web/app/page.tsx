"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/advice", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: query, crop: "wheat" }),
      });
      const data = await res.json();
      setReply(data.reply);
    } catch (err) {
      console.error(err);
      setReply("Error connecting to backend");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6">
      <h1 className="text-2xl font-bold mb-4">🌱 Crop-Guru</h1>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          className="border rounded p-2"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about your crop..."
        />
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded"
          disabled={loading}
        >
          {loading ? "..." : "Ask"}
        </button>
      </form>

      {reply && (
        <div className="mt-6 p-4 border rounded w-full max-w-md bg-gray-50">
          <p className="font-medium">Response:</p>
          <p>{reply}</p>
        </div>
      )}
    </main>
  );
}
