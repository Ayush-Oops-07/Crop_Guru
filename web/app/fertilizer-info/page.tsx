"use client";
import { useState } from "react";
import BackButton from "../components/BackButton";

export default function FertilizerInfoPage() {
  const [name, setName] = useState("");
  const [info, setInfo] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchInfo = async () => {
    if (!name) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/fertilizer-info?name=${name}`
      );
      const data = await res.json();

      if (data.error) {
        setError(data.error);
        setInfo(null);
      } else {
        setInfo(data);
      }
    } catch (err: any) {
      setError("Failed to fetch fertilizer info");
      setInfo(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-green-50 p-6">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-md w-full">
        {/* Back Button */}
        <div className="mb-4">
          <BackButton />
        </div>

        <h1 className="text-3xl font-bold text-center mb-6 text-green-700">
          🧪 Fertilizer Info
        </h1>

        {/* Input & Button */}
        <div className="flex gap-2 mb-6">
          <input
            type="text"
            placeholder="Enter fertilizer name..."
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
          />
          <button
            onClick={fetchInfo}
            disabled={loading}
            className="bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 transition disabled:bg-green-400"
          >
            {loading ? "Loading..." : "Get Info"}
          </button>
        </div>

        {/* Error */}
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        {/* Fertilizer Info Card */}
        {info && (
          <div className="bg-green-50 rounded-xl p-6 text-center shadow-inner">
            {Object.entries(info).map(([key, value]) => (
              <div
                key={key}
                className="bg-white rounded-lg p-4 shadow mb-3 text-left"
              >
                <h2 className="text-lg font-semibold text-gray-800 capitalize">
                  {key}
                </h2>
                <p className="text-gray-600 mt-1">{String(value)}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}