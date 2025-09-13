"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

export default function DetectionPage() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch("http://crop-guru.onrender.com/detection", { method: "POST" })
      .then((res) => res.json())
      .then(setData);
  }, []);

  return (
    <div className="p-6 max-w-2xl mx-auto">
      {/* ✅ Back Button */}
            <BackButton />
      <h1 className="text-2xl font-bold mb-4">📷 Crop Detection (YOLO)</h1>
      {data ? (
        <pre className="bg-gray-100 p-4 rounded">{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
