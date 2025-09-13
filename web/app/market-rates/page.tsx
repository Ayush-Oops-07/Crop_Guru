"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

export default function MarketRatesPage() {
  const [rates, setRates] = useState<Record<string, string> | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchRates = async () => {
      try {
        const res = await fetch("crop-guru.onrender.com/market-rates");
        const data = await res.json();

        if (data.error) {
          setError(data.error);
        } else {
          setRates(data);
        }
      } catch (err) {
        setError("Failed to fetch market rates");
      } finally {
        setLoading(false);
      }
    };

    fetchRates();
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-green-50 p-6">
      <div className="bg-white shadow-2xl rounded-2xl p-8 max-w-2xl w-full">
        {/* Back Button */}
        <div className="mb-4">
          <BackButton />
        </div>

        <h1 className="text-3xl font-bold text-center mb-6 text-green-700">
          📈 Market Rates
        </h1>

        {/* Loading / Error */}
        {loading && <p className="text-center text-gray-600">Loading...</p>}
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        {/* Rates Table */}
        {rates && (
          <div className="bg-green-50 rounded-xl p-6 shadow-inner">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-green-200">
                  <th className="p-3 border border-green-300 text-gray-800 font-semibold">
                    Crop
                  </th>
                  <th className="p-3 border border-green-300 text-gray-800 font-semibold">
                    Price
                  </th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(rates).map(([crop, price], i) => (
                  <tr
                    key={i}
                    className="hover:bg-green-100 transition"
                  >
                    <td className="p-3 border border-green-200 capitalize">{crop}</td>
                    <td className="p-3 border border-green-200 font-bold text-gray-700">
                      {price}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
