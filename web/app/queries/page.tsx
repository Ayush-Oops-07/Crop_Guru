"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

export default function QueriesPage() {
  const [queries, setQueries] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/queries")
      .then((res) => res.json())
      .then(setQueries);
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      {/* ✅ Back Button */}
            <BackButton />
      <h1 className="text-2xl font-bold mb-4">❓ Past Queries</h1>
      <ul className="space-y-3">
        {queries.map((q) => (
          <li key={q.id} className="p-4 border rounded bg-white shadow">
            <p><strong>Query:</strong> {q.message}</p>
            <p><strong>Reply:</strong> {q.reply}</p>
            <p className="text-sm text-gray-500">Crop: {q.crop} </p>
          </li>
        ))}
      </ul>
    </div>
  );
}
