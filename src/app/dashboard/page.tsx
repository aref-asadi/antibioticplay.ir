// app/dashboard/page.tsx
import { getServerSession } from "next-auth";
import { authOptions } from "../api/auth/[...nextauth]/route";
import { redirect } from "next/navigation";
import prisma from "@/app/lib/prisma";

export default async function DashboardPage() {
  // Get the user's session on the server
  const session = await getServerSession(authOptions);

  // If no user is logged in, redirect them to the play page
  if (!session || !session.user) {
    redirect("/play");
  }

  // Fetch all scores for the current user from the database, newest first
  const scores = await prisma.gameScore.findMany({
    where: {
      userId: session.user.id,
    },
    orderBy: {
      createdAt: "desc",
    },
  });

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-lg p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">
          My Dashboard
        </h1>
        <p className="text-gray-600 mb-6">
          Welcome back, {session.user.email}! Here are your recent scores.
        </p>

        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border">
            <thead className="bg-gray-200">
              <tr>
                <th className="text-left py-3 px-4 uppercase font-semibold text-sm">Score</th>
                <th className="text-left py-3 px-4 uppercase font-semibold text-sm">Date</th>
              </tr>
            </thead>
            <tbody className="text-gray-700">
              {scores.length > 0 ? (
                scores.map((score) => (
                  <tr key={score.id} className="border-b hover:bg-gray-50">
                    <td className="py-3 px-4">{score.score} / {score.maxScore}</td>
                    <td className="py-3 px-4">
                      {new Date(score.createdAt).toLocaleDateString("en-US", {
                        year: 'numeric', month: 'long', day: 'numeric'
                      })}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={2} className="py-3 px-4 text-center text-gray-500">
                    You have no scores yet. Go play a game!
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}