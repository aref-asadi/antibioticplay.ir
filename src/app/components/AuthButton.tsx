// app/components/AuthButton.tsx
'use client';

import { useSession, signIn, signOut } from 'next-auth/react';
import Link from 'next/link'; // Import the Link component

export default function AuthButton() {
  const { data: session } = useSession();

  if (session) {
    return (
      <div className="flex items-center gap-4">
        <p className="text-sm text-gray-600">Signed in as {session.user?.email}</p>
        {/* Add a link to the dashboard */}
        <Link href="/dashboard" className="text-sm font-semibold text-blue-600 hover:underline">
          Dashboard
        </Link>
        <button 
          onClick={() => signOut()} 
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Sign Out
        </button>
      </div>
    );
  }
  return (
    <button 
      onClick={() => signIn('email')} 
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Sign In
    </button>
  );
}