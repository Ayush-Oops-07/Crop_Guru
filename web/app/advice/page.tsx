"use client";
import { useState } from "react";
import BackButton from "../components/BackButton";

export default function CropAdvicePage() {
  const [query, setQuery] = useState("");
  const [crop, setCrop] = useState("");
  const [language, setLanguage] = useState("English");
  const [info, setInfo] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchAdvice = async () => {
    if (!query) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`http://crop-guru.onrender.com/advice`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: query,
          crop: crop,
          locale: language,
        }),
      });
      const data = await res.json();

      if (data.error) {
        setError(data.error);
        setInfo(null);
      } else {
        setInfo(data);
      }
    } catch (err) {
      setError("Failed to fetch crop advice");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-green-50 p-6">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-3xl w-full">
        {/* ✅ Back Button */}
        <div className="mb-4">
          <BackButton />
        </div>

        <h1 className="text-3xl font-bold text-center mb-6 text-green-700">
          🌾 Crop Advice
        </h1>

        {/* Inputs */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
          <input
            type="text"
            placeholder="Enter query (e.g. How to grow rice)"
            className="border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <input
            type="text"
            placeholder="Enter crop name"
            className="border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
            value={crop}
            onChange={(e) => setCrop(e.target.value)}
          />
          {/* Language Dropdown */}
          <select
            className="border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="English">English</option>
            <option value="Hindi">Hindi</option>
            <option value="Malayalam">Malayalam</option>
            <option value="Odia">Odia</option>
            <option value="Telugu">Telugu</option>
            <option value="Bhojpuri">Bhojpuri</option>
            <option value="Gujarati">Gujarati</option>
            <option value="Haryanvi">Haryanvi</option>
            <option value="Rajasthani">Rajasthani</option>
          </select>
        </div>

        {/* Button */}
        <button
          onClick={fetchAdvice}
          disabled={loading}
          className="w-full bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 transition disabled:bg-green-400"
        >
          {loading ? "Loading..." : "Get Advice"}
        </button>

        {/* Error */}
        {error && <p className="text-red-500 text-center mt-4">{error}</p>}

        {/* Advice Card */}
        {info && (
          <div className="bg-green-50 rounded-xl p-6 shadow-inner mt-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-3">
              {info.query}
            </h2>
            <p className="text-green-700 font-medium mb-2">🌱 Crop: {info.crop || "Not specified"}</p>
            <p className="text-gray-700 font-medium mb-2">🌐 Language: {info.language}</p>
            <p className="text-gray-700 leading-relaxed whitespace-pre-line">
              {info.reply}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
