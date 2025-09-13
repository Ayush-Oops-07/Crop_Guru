"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

const states = [
  "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
  "Bihar", "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu",
  "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
  "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh",
  "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry",
  "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
  "Uttarakhand", "West Bengal"
];

export default function SchemesPage() {
  const [schemes, setSchemes] = useState<any[]>([]);
  const [selectedState, setSelectedState] = useState<string>("");

  useEffect(() => {
    // Fetches schemes based on the selected state or defaults to an empty list
    const fetchSchemes = async () => {
      let url = "";
      if (selectedState === "Central") {
        url = "https://crop-guru.onrender.com/schemes/central";
      } else if (selectedState) {
        url = `https://crop-guru.onrender.com/schemes/state?state=${selectedState}`;
      }

      if (url) {
        try {
          const res = await fetch(url);
          const data = await res.json();
          setSchemes(data);
        } catch (error) {
          console.error("Failed to fetch schemes:", error);
          setSchemes([]);
        }
      } else {
        setSchemes([]);
      }
    };

    fetchSchemes();
  }, [selectedState]);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <BackButton />
      <h1 className="text-2xl font-bold mb-4">🏛️ Government Schemes</h1>

      {/* ✅ Action Buttons */}
      <div className="flex flex-col md:flex-row gap-4 mb-6">
        <button
          onClick={() => setSelectedState("Central")}
          className="px-4 py-2 bg-green-500 text-white rounded-lg shadow-md hover:bg-green-600 transition-colors"
        >
          Central Schemes
        </button>

        <select
          value={selectedState}
          onChange={(e) => setSelectedState(e.target.value)}
          className="px-4 py-2 border rounded-lg shadow-md bg-white text-gray-700"
        >
          <option value="">Select a State</option>
          {states.map((state) => (
            <option key={state} value={state}>
              {state}
            </option>
          ))}
        </select>
      </div>

      {/* ✅ Display Schemes */}
      {schemes.length > 0 ? (
        <ul className="space-y-3">
          {schemes.map((s, i) => (
            <li key={i} className="p-4 border rounded bg-white shadow">
              <h2 className="font-semibold text-lg">{s.name}</h2>
              <p className="text-gray-600">{s.description}</p>
              <p className="mt-2 font-medium">Benefit: <span className="text-blue-600">{s.benefit}</span></p>
              {s.apply_link && (
                <a
                  href={s.apply_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 hover:underline mt-2 inline-block"
                >
                  Apply Now
                </a>
              )}
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-center text-gray-500 mt-10">
          Please select a state or click the "Central Schemes" button to view schemes.
        </p>
      )}
    </div>
  );
}
