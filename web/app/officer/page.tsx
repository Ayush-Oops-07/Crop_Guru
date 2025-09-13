"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

type Query = {
  id: number;
  message: string;
  reply: string;
  crop: string | null;
  city: string | null;
  created_at: string | null;
  escalated: boolean;
};

export default function OfficerDashboard() {
  const [queries, setQueries] = useState<Query[]>([]);
  const [loading, setLoading] = useState(false);
  const [onlyEscalated, setOnlyEscalated] = useState(false);
  const [search, setSearch] = useState("");
  const backend = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

  const fetchQueries = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${backend}/queries`);
      if (!res.ok) throw new Error("Failed to fetch");
      const data = await res.json();
      setQueries(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Error fetching queries:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchQueries();
    const id = setInterval(fetchQueries, 30_000); // refresh every 30s
    return () => clearInterval(id);
  }, []);

  const toggleEscalate = async (id: number) => {
    try {
      const res = await fetch(`${backend}/queries/${id}/escalate`, { method: "POST" });
      const data = await res.json();
      setQueries((prev) => prev.map((q) => (q.id === id ? { ...q, escalated: data.escalated } : q)));
    } catch (err) {
      console.error("Error toggling escalate:", err);
    }
  };

  const filtered = queries
    .filter((q) => (onlyEscalated ? q.escalated : true))
    .filter((q) => {
      const s = search.trim().toLowerCase();
      if (!s) return true;
      return (
        q.message?.toLowerCase().includes(s) ||
        q.reply?.toLowerCase().includes(s) ||
        (q.crop || "").toLowerCase().includes(s) ||
        (q.city || "").toLowerCase().includes(s)
      );
    })
    .sort((a, b) => {
      const ta = a.created_at ? new Date(a.created_at).getTime() : 0;
      const tb = b.created_at ? new Date(b.created_at).getTime() : 0;
      return tb - ta;
    });

  return (
    <main className="min-h-screen p-6 bg-slate-50">
      {/* ✅ Back Button */}
            <BackButton />
      
      <div className="max-w-5xl mx-auto">
        <h1 className="text-3xl font-bold mb-4">👮 Officer Dashboard</h1>

        <div className="flex gap-3 items-center mb-4">
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="border p-2 rounded flex-1"
            placeholder="Search message, crop, city..."
          />
          <label className="flex items-center gap-2 text-sm">
            <input type="checkbox" checked={onlyEscalated} onChange={(e) => setOnlyEscalated(e.target.checked)} />
            Only escalated
          </label>
          <button onClick={fetchQueries} className="bg-blue-600 text-white px-3 py-2 rounded">Refresh</button>
        </div>

        {loading ? (
          <div>Loading...</div>
        ) : (
          <div className="space-y-3">
            {filtered.length === 0 && <div className="text-gray-500">No queries match your filter.</div>}

            {filtered.map((q) => (
              <div key={q.id} className={`bg-white p-4 rounded shadow flex gap-4 ${q.escalated ? "ring-2 ring-red-300" : ""}`}>
                <div className="w-12 flex-shrink-0 flex flex-col items-center justify-center">
                  <div className="text-sm font-semibold">{q.id}</div>
                  <div className="text-xs text-gray-400">{q.crop || "-"}</div>
                </div>

                <div className="flex-1">
                  <div className="flex items-baseline justify-between gap-3">
                    <div className="text-sm font-medium">{q.message}</div>
                    <div className="text-xs text-gray-500">{q.created_at ? new Date(q.created_at).toLocaleString() : "-"}</div>
                  </div>

                  <div className="mt-2 text-sm text-gray-700 whitespace-pre-wrap">{q.reply}</div>

                  <div className="mt-3 flex items-center gap-2">
                    <div className="text-xs text-gray-500">City: {q.city || "-"}</div>
                    {q.escalated ? (
                      <div className="text-xs bg-red-500 text-white px-2 py-1 rounded">Escalated</div>
                    ) : (
                      <div className="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Normal</div>
                    )}
                  </div>
                </div>

                <div className="flex flex-col gap-2 items-end">
                  <button
                    onClick={() => toggleEscalate(q.id)}
                    className={`px-3 py-1 rounded text-white ${q.escalated ? "bg-gray-600" : "bg-red-500"}`}
                  >
                    {q.escalated ? "Un-escalate" : "Escalate"}
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
