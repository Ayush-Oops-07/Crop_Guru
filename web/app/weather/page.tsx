"use client";
import { useState } from "react";
import BackButton from "../components/BackButton";

export default function WeatherPage() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchWeather = async () => {
    if (!city) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`http://crop-guru.onrender.com/weather?city=${city}`);
      const data = await res.json();

      if (data.error) {
        setError(data.error);
        setWeather(null);
      } else {
        setWeather(data);
      }
    } catch (err: any) {
      setError("Failed to fetch weather");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center bg-green-50 p-6">
      {/* Back Button */}
      <div className="w-full max-w-md mb-4">
        <BackButton />
      </div>

      {/* Weather Card */}
      <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-6 text-green-700">
          🌤 Weather Checker
        </h1>

        {/* Input & Button */}
        <div className="flex gap-2 mb-6">
          <input
            type="text"
            placeholder="Enter city name..."
            value={city}
            onChange={(e) => setCity(e.target.value)}
            className="flex-1 border border-gray-300 rounded px-4 py-2 focus:ring-2 focus:ring-green-400 outline-none"
          />
          <button
            onClick={fetchWeather}
            disabled={loading}
            className="bg-green-600 text-white px-4 py-2 rounded shadow hover:bg-green-700 transition disabled:bg-green-400"
          >
            {loading ? "Loading..." : "Get Weather"}
          </button>
        </div>

        {/* Error */}
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        {/* Weather Data */}
        {weather && (
          <div className="bg-green-50 rounded-lg p-6 text-center shadow-inner">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">
              {weather.city}, {weather.country}
            </h2>
            <p className="text-gray-600 capitalize mb-4">
              {weather.description}
            </p>

            <div className="grid grid-cols-2 gap-4 text-gray-700">
              <div className="bg-white rounded p-3 shadow">
                🌡 Temp: <span className="font-bold">{weather.temperature}°C</span>
              </div>
              <div className="bg-white rounded p-3 shadow">
                🤒 Feels Like: <span className="font-bold">{weather.feels_like}°C</span>
              </div>
              <div className="bg-white rounded p-3 shadow">
                💧 Humidity: <span className="font-bold">{weather.humidity}%</span>
              </div>
              <div className="bg-white rounded p-3 shadow">
                🌬 Wind: <span className="font-bold">{weather.wind_speed} m/s</span>
              </div>
              <div className="bg-white rounded p-3 shadow col-span-2">
                📊 Pressure: <span className="font-bold">{weather.pressure} hPa</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
