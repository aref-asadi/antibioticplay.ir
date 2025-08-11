import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Providers from "./providers"; // Import our new component

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AntibioticPlay.ir",
  description: "An educational game for pharmacy students",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers> {/* Wrap the children with the SessionProvider */}
          {children}
        </Providers>
      </body>
    </html>
  );
}