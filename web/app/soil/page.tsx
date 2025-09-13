"use client";
import { useState } from "react";
import BackButton from "../components/BackButton";

export default function SoilPage() {
  const [city, setCity] = useState("");
  const [info, setInfo] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchSoil = async () => {
    if (!city) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`http://127.0.0.1:8000/soil/${city}`);
      const data = await res.json();

      if (data.error) {
        setError(data.error);
        setInfo(null);
      } else {
        setInfo(data);
      }
    } catch (err) {
      setError("Failed to fetch soil info");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-green-50 p-6">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-2xl w-full">
        {/* ✅ Back Button */}
        <div className="mb-4">
          <BackButton />
        </div>

        <h1 className="text-3xl font-bold text-center mb-6 text-green-700">
          🌍 Soil Information
        </h1>

        {/* Input + Button */}
        <div className="flex gap-2 mb-6">
          <input
            type="text"
            placeholder="Enter city"
            className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
          <button
            onClick={fetchSoil}
            disabled={loading}
            className="bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 transition disabled:bg-green-400"
          >
            {loading ? "Loading..." : "Get Soil Info"}
          </button>
        </div>

        {/* Error */}
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        {/* Soil Info Card */}
        {info && (
          <div className="bg-green-50 rounded-xl p-6 shadow-inner text-center">
            <h2 className="text-2xl font-semibold text-gray-800 mb-2 capitalize">
              {info.city}
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-gray-700">
              <div className="bg-white rounded-lg p-3 shadow">
                🏞 Soil Type:{" "}
                <span className="font-bold">{info.soil_type}</span>
              </div>
              <div className="bg-white rounded-lg p-3 shadow">
                ⚖ pH Level:{" "}
                <span className="font-bold">{info.ph}</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}