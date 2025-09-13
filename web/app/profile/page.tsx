"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

export default function ProfilePage() {
  const [profile, setProfile] = useState<any>(null);
  const [farmerId, setFarmerId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    const storedId = localStorage.getItem("farmer_id");

    if (token && storedId) {
      fetch("http://localhost:8000/profile", {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((res) => res.json())
        .then((data) => {
          setProfile(data);
          setFarmerId(storedId);
        })
        .catch((err) => {
          console.error("Profile fetch error:", err);
        })
        .finally(() => setLoading(false));
    } else {
      const inputId = prompt("Enter Farmer ID to view profile:");
      setFarmerId(inputId || null);
      setLoading(false);
    }
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-lg text-gray-500">Loading profile...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-green-50 flex flex-col items-center p-6">
      <BackButton />
      <h1 className="text-3xl font-bold mb-6">Farmer Profile</h1>

      {farmerId && (
        <p className="mb-6 text-lg text-gray-700">
          Farmer ID: <span className="font-semibold">{farmerId}</span>
        </p>
      )}

      {profile ? (
        <div className="bg-white shadow-lg rounded-xl p-6 w-full max-w-md space-y-3">
          <p>
            <span className="font-semibold">Name:</span> {profile.name}
          </p>
          <p>
            <span className="font-semibold">Phone:</span> {profile.phone}
          </p>
          <p>
            <span className="font-semibold">Location:</span>{" "}
            {profile.location || "Not Provided"}
          </p>
          <p>
            <span className="font-semibold">Crops:</span>{" "}
            {profile.crops || "Not Provided"}
          </p>
        </div>
      ) : (
        <p className="text-gray-500 mt-4">
          No profile data available for this farmer.
        </p>
      )}
    </div>
  );
}