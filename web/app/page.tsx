"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Navbar from "./components/Navbar";
import Carousel from "./components/Carousel";
import DashboardBox from "./components/DashboardBox";
import Footer from "./components/Footer";

interface FarmerProfile {
  id: number;
  name: string;
  phone: string;
  location: string;
  crops: string;
}

export default function Home() {
  const [farmer, setFarmer] = useState<FarmerProfile | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const router = useRouter();

  useEffect(() => {
    const fetchFarmerProfile = async () => {
      const storedToken = localStorage.getItem("access_token");
      if (storedToken) {
        try {
          const res = await fetch("http://127.0.0.1:8000/profile", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${storedToken}`,
            },
          });

            if (res.ok) {
              const profileData = await res.json();
              setFarmer(profileData);
            } else {
              localStorage.removeItem("access_token");
            }
          } catch (error) {
            console.error("Failed to fetch profile:", error);
          }
        }
        setLoading(false);
      };

    fetchFarmerProfile();
  }, [router]);

  const photos = [
    "/farmer1.jpeg", "/farmer2.jpeg", "/farmer3.jpeg", "/farmer4.jpeg", "/farmer5.jpeg",
    "/farmer6.jpeg", "/farmer7.jpeg", "/farmer8.jpeg", "/farmer9.jpeg", "/farmer10.jpeg", "/farmer11.jpeg"
  ];

  const features = [
    { title: "Crop Advice", link: "/advice", icon: "🌾" },
    { title: "Crop Queries", link: "/queries", icon: "❓" },
    { title: "Weather", link: "/weather", icon: "⛅" },
    { title: "Government Schemes", link: "/schemes", icon: "🏛️" },
    { title: "Farmer Profile", link: "/profile", icon: "👨‍🌾" },
    { title: "Crop Information", link: "/crops", icon: "🌱" },
    { title: "Soil Information", link: "/soil", icon: "🌍" },
    { title: "Crop Detection (YOLO - Future)", link: "/detection", icon: "📷" },
    { title: "Market Rate of All Crops", link: "/market-rates", icon: "📈" },
    { title: "Information of Fertilizer", link: "/fertilizer-info", icon: "🧪" },
    { title: "Irrigation System", link: "/irrigation", icon: "💧" },
    { title: "Loan Facilities", link: "/loans", icon: "💰" },
  ];

  const handleFeatureClick = (link: string) => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      localStorage.setItem("redirectAfterLogin", link);
      router.push("/login");
    } else {
      router.push(link);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen text-xl">
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-green-50 to-white">
      <Navbar farmer={farmer} />

      <Carousel photos={photos} />

      {farmer && (
        <section className="text-center py-6 bg-green-100 shadow-inner">
          <h1 className="text-2xl font-bold">Welcome, {farmer.name}! 👨‍🌾</h1>
        </section>
      )}

      <section className="text-center py-10 bg-gray-100 shadow-inner">
        <p className="text-2xl italic text-gray-700 max-w-2xl mx-auto">
          "The future of farming lies in the hands of those who innovate today."
        </p>
      </section>

      <section
        id="dashboard"
        className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 p-6 max-w-7xl mx-auto"
      >
        {features.map(({ title, link, icon }, i) => (
          <DashboardBox
            key={i}
            title={title}
            icon={icon}
            onClick={() => handleFeatureClick(link)}
          />
        ))}
      </section>

      <Footer />
    </div>
  );
}