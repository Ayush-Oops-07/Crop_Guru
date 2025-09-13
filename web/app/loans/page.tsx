"use client";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";

export default function LoansPage() {
  const [loans, setLoans] = useState<any[]>([]);

  useEffect(() => {
    fetch("https://crop-guru.onrender.com/loans")
      .then((res) => res.json())
      .then(setLoans);
  }, []);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      {/* ✅ Back Button */}
            <BackButton />
      <h1 className="text-2xl font-bold mb-4">💰 Loan Facilities</h1>
      <ul className="space-y-3">
        {loans.map((l, i) => (
          <li key={i} className="p-4 border rounded bg-white shadow">
            <h2 className="font-semibold">{l.scheme}</h2>
            <p>{l.benefit}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
