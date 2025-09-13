"use client";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";

// Define the shape of the farmer prop
interface FarmerProfile {
  id: number;
  name: string;
  phone: string;
  location: string;
  crops: string;
}

// Define the Navbar's props
interface NavbarProps {
  farmer: FarmerProfile | null;
}

export default function Navbar({ farmer }: NavbarProps) {
  const router = useRouter();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("farmer_id");
    localStorage.removeItem("farmer_name");
    router.push("/login");
  };

  return (
    <nav className="w-full bg-green-700 text-white px-6 py-4 flex justify-between items-center shadow-lg sticky top-0 z-50">
      <Link href="/">
        <div className="font-bold text-2xl cursor-pointer">
          🌱 Crop-Guru
        </div>
      </Link>

      {/* Desktop Menu */}
      <div className="hidden md:flex gap-6 items-center font-medium">
        <a href="#home" className="hover:text-yellow-300 transition">Home</a>
        <a href="#dashboard" className="hover:text-yellow-300 transition">Dashboard</a>
        <a href="#schemes" className="hover:text-yellow-300 transition">Schemes</a>
        <a href="#about" className="hover:text-yellow-300 transition">About</a>
        <a href="#contact" className="hover:text-yellow-300 transition">Contact</a>

        {farmer ? (
          <>
            <Link href="/profile" className="bg-white text-green-700 px-4 py-1 rounded-lg shadow hover:bg-yellow-300 transition">
              Profile
            </Link>
            <button
              onClick={handleLogout}
              className="bg-red-500 text-white px-4 py-1 rounded-lg shadow hover:bg-red-600 transition"
            >
              Logout
            </button>
          </>
        ) : (
          <>
            <Link href="/login" className="bg-white text-green-700 px-4 py-1 rounded-lg shadow hover:bg-yellow-300 transition">
              Login
            </Link>
            <Link href="/signup" className="bg-yellow-400 text-black px-4 py-1 rounded-lg shadow hover:bg-yellow-500 transition">
              Signup
            </Link>
          </>
        )}
      </div>

      {/* Mobile Hamburger */}
      <div className="md:hidden flex items-center">
        {/* Your mobile hamburger button logic goes here */}
      </div>

      {/* Mobile Menu */}
      {/* Your mobile menu logic goes here */}
    </nav>
  );
}