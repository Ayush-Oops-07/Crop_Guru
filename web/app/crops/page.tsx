"use client";
import { useState } from "react";
import BackButton from "../components/BackButton";

export default function CropsPage() {
  const [crop, setCrop] = useState("");
  const [info, setInfo] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchCrop = async () => {
    if (!crop) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`http://127.0.0.1:8000/crops/${crop}`);
      const data = await res.json();

      if (data.error) {
        setError(data.error);
        setInfo(null);
      } else {
        setInfo(data);
      }
    } catch (err) {
      setError("Failed to fetch crop info");
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
          🌱 Crop Information
        </h1>

        {/* Input + Button */}
        <div className="flex gap-2 mb-6">
          <input
            type="text"
            placeholder="Enter crop name"
            className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
            value={crop}
            onChange={(e) => setCrop(e.target.value)}
          />
          <button
            onClick={fetchCrop}
            disabled={loading}
            className="bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 transition disabled:bg-green-400"
          >
            {loading ? "Loading..." : "Get Info"}
          </button>
        </div>

        {/* Error */}
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        {/* Crop Info Card */}
        {info && (
          <div className="bg-green-50 rounded-xl p-6 shadow-inner text-center">
            <h2 className="text-2xl font-semibold text-gray-800 mb-2 capitalize">
              {info.crop}
            </h2>
            <p className="text-gray-700 text-lg">{info.info}</p>
          </div>
        )}
      </div>
    </div>
  );
}