import { FaFacebookF, FaTwitter, FaInstagram } from "react-icons/fa";

export default function Footer() {
  return (
    <footer className="bg-green-700 text-white text-center py-8 mt-auto shadow-inner">
      <div className="max-w-6xl mx-auto px-6 grid sm:grid-cols-2 md:grid-cols-3 gap-8 text-sm">
        <div className="text-left">
          <h3 className="font-bold text-lg mb-2">🌾 Crop-Guru</h3>
          <p className="text-gray-200">Smart Farming Assistant for Indian Farmers</p>
        </div>
        <div className="text-left">
          <h3 className="font-bold text-lg mb-2">Quick Links</h3>
          <ul className="space-y-2">
            <li>
              <a href="#dashboard" className="hover:underline hover:text-yellow-300 transition">
                Dashboard
              </a>
            </li>
            <li>
              <a href="#contact" className="hover:underline hover:text-yellow-300 transition">
                Contact
              </a>
            </li>
            <li>
              <a href="#schemes" className="hover:underline hover:text-yellow-300 transition">
                Schemes
              </a>
            </li>
          </ul>
        </div>
        <div className="text-left">
          <h3 className="font-bold text-lg mb-2">Contact</h3>
          <p>Email: <a href="mailto:support@cropguru.com" className="hover:underline hover:text-yellow-300">support@cropguru.com</a></p>
          <p>Phone: <a href="tel:+918235308885" className="hover:underline hover:text-yellow-300">+91 82353 08885</a></p>
          {/* Optional Social Icons */}
          <div className="flex space-x-4 mt-4 text-yellow-300">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook" className="hover:text-yellow-400 transition">
              <FaFacebookF />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter" className="hover:text-yellow-400 transition">
              <FaTwitter />
            </a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram" className="hover:text-yellow-400 transition">
              <FaInstagram />
            </a>
          </div>
        </div>
      </div>
      <p className="mt-8 text-xs text-gray-300">© 2025 Crop-Guru. All rights reserved.</p>
    </footer>
  );
}
