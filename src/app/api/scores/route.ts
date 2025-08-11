import { getServerSession } from "next-auth";
import { authOptions } from "../auth/[...nextauth]/route";
import prisma from "@/app/lib/prisma";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  console.log("--- Score API Endpoint Hit ---");

  const session = await getServerSession(authOptions);

  if (!session || !session.user?.id) {
    console.log("API Error: User not authenticated.");
    return new NextResponse("Unauthorized", { status: 401 });
  }

  const body = await request.json();
  // Destructure the new quizName property
  const { score, maxScore, quizName } = body;

  if (typeof score !== 'number' || typeof maxScore !== 'number' || typeof quizName !== 'string' || !quizName) {
    console.log("API Error: Invalid data received.", body);
    return new NextResponse("Invalid data received", { status: 400 });
  }

  const gameScore = await prisma.gameScore.create({
    data: {
      score: score,
      maxScore: maxScore,
      quizName: quizName, // Save the quizName to the database
      userId: session.user.id,
    },
  });

  console.log("API Success: Score saved to database.", gameScore);
  return NextResponse.json(gameScore, { status: 201 });
}