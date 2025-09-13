"use client";
import { useState, useEffect } from "react";

interface CarouselProps {
  photos: string[];
}

export default function Carousel({ photos }: CarouselProps) {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % photos.length);
    }, 3000);
    return () => clearInterval(timer);
  }, [photos.length]);

  return (
    <div className="w-full overflow-hidden py-6 bg-white flex justify-center">
      <div className="flex justify-center items-center gap-6 transition-all duration-700">
        {photos.map((photo, i) => {
          // Calculate relative position in carousel
          const relativeIndex = (i - index + photos.length) % photos.length;

          // Show only 5 photos at a time (relativeIndex 0 to 4)
          if (relativeIndex > 4) return null;

          // Base styles for all photos
          let className = "transition-all duration-700 rounded-xl overflow-hidden object-contain";

          // Apply different styles depending on relative position
          switch (relativeIndex) {
            case 0: // far left blurred photo
            case 4: // far right blurred photo
              className += " w-[200px] h-[280px] scale-90 blur-sm opacity-60";
              break;
            case 1: // left clear photo
            case 3: // right clear photo
              className += " w-[280px] h-[360px] scale-100 blur-0 opacity-90 shadow-lg";
              break;
            case 2: // center clear photo
              className += " w-[320px] h-[400px] scale-110 blur-0 opacity-100 shadow-2xl";
              break;
          }

          return (
            <img
              key={i}
              src={photo}
              alt={`Farmer ${i + 1}`}
              className={className}
              loading="lazy"
            />
          );
        })}
      </div>
    </div>
  );
}