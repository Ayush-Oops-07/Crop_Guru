"use client";

import { useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react"; // nice icon
import { motion } from "framer-motion";

export default function BackButton() {
  const router = useRouter();

  return (
    <motion.button
      onClick={() => router.push("/")}
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      className="flex items-center gap-2 px-4 py-2 mb-6 
                 rounded-xl shadow-lg 
                 bg-white/30 backdrop-blur-md 
                 border border-white/40
                 text-green-800 font-semibold
                 hover:bg-white/50 transition"
    >
      <ArrowLeft size={20} />
      Back to Home
    </motion.button>
  );
}
