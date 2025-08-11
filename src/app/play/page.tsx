'use client'; // This is crucial for using hooks like useEffect

import React, { useEffect } from 'react';
import Script from 'next/script';

// We need to declare the H5PStandalone object on the window for TypeScript
declare global {
  interface Window {
    H5PStandalone: any;
  }
}

export default function PlayPage() {

  useEffect(() => {
    // This code will run only after the component has mounted
    // and the H5P script has loaded.
    if (window.H5PStandalone) {
      const el = document.getElementById('h5p-container');

      const options = {
        h5pJsonPath: '/h5p/content/penicillin-classification', // Path to the extracted folder 
        frameJs: '/h5p/dist/frame.bundle.js', // Path to the player's frame.bundle.js 
        frameCss: '/h5p/dist/styles/h5p.css', // Path to the player's h5p.css 
      };
      
      // Instantiate the player 
      new window.H5PStandalone.H5P(el, options);
    }
  }, []); // The empty array ensures this effect runs only once

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8 bg-gray-100">
      <h1 className="text-4xl font-bold mb-8">Antibiotic Challenge</h1>
      
      {/* 1. Include the main H5P player script using Next.js's Script component */}
      <Script src="/h5p/dist/main.bundle.js" strategy="afterInteractive" />

      {/* 2. This is the container where H5P will be rendered  */}
      <div id="h5p-container" className="w-full max-w-4xl h-[600px] border-4 border-gray-300 rounded-lg shadow-lg"></div>

      <p className="mt-4 text-gray-600">
        Based on the "Classification & Structure" module.
      </p>
    </main>
  );
}