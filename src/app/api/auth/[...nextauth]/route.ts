import NextAuth from "next-auth";
import type { Session, User } from "next-auth"; // Import Session and User types
import { PrismaAdapter } from "@auth/prisma-adapter";
import prisma from "@/app/lib/prisma";
import EmailProvider from "next-auth/providers/email";
import nodemailer from "nodemailer";

export const authOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    EmailProvider({
      sendVerificationRequest: async (params) => {
        const { identifier, url, provider } = params;
        const { host } = new URL(url);

        const transport = nodemailer.createTransport({
          jsonTransport: true,
        });

        const result = await transport.sendMail({
          to: identifier,
          from: provider.from,
          subject: `Sign in to ${host}`,
          text: `Sign in to ${host}\n${url}\n\n`,
          html: `<p>Sign in to <strong>${host}</strong> by clicking this link: <a href="${url}">Click here</a></p>`,
        });

        console.log("--- DEVELOPMENT EMAIL ---");
        console.log(`To: ${identifier}`);
        console.log("Message (contains sign-in link):");
        console.log(result.message);
        console.log("------------------------");
      },
      from: "no-reply@antibioticplay.ir",
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
  
  // --- FIX for Error #2: Add user ID to the session ---
  callbacks: {
    // Add types for session and user parameters
    session({ session, user }: { session: Session; user: User }) {
      if (session.user) {
        session.user.id = user.id;
      }
      return session;
    },
  },

  // --- FIX for Error #1: Explicitly type 'message' as 'any' ---
  events: {
    signIn: async (message: any) => { console.log("NextAuth SIGN IN Event:", message); },
    signOut: async (message: any) => { console.log("NextAuth SIGN OUT Event:", message); },
    createUser: async (message: any) => { console.log("NextAuth CREATE USER Event:", message); },
    linkAccount: async (message: any) => { console.log("NextAuth LINK ACCOUNT Event:", message); },
    session: async (message: any) => { console.log("NextAuth SESSION Event:", message); },
    error: async (message: any) => { console.log("NextAuth ERROR Event:", message); }
  },
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };