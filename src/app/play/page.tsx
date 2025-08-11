'use client';
import React, { useState } from 'react';
import AuthButton from '../components/AuthButton';
import { GameContainer } from '../components/classification-game/GameContainer';
import { MatchingGameContainer } from '../components/matching-game/MatchingGameContainer';
import Link from 'next/link';

const quizQuestions = [
  { type: 'classification', title: 'Penicillin Classification Challenge' },
  { type: 'matching', title: 'Dosage Forms Matching' },
];

export default function PlayPage() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [isQuizComplete, setIsQuizComplete] = useState(false);

  const handleQuestionComplete = async (result: { score: number, maxScore: number, quizName: string }) => {
    console.log(`Quiz '${result.quizName}' completed with score ${result.score}/${result.maxScore}`);

    // The saving logic is now inside each component, but we could also centralize it here.
    // For now, we'll just advance to the next question.

    setTimeout(() => {
      if (currentQuestionIndex < quizQuestions.length - 1) {
        setCurrentQuestionIndex(prevIndex => prevIndex + 1);
      } else {
        setIsQuizComplete(true);
      }
    }, 2500); // 2.5 second delay to review results
  };

  const currentQuestion = quizQuestions[currentQuestionIndex];
  
  let gameComponent;
  if (!isQuizComplete) {
    switch (currentQuestion.type) {
      case 'classification':
        gameComponent = <GameContainer onComplete={handleQuestionComplete} />;
        break;
      case 'matching':
        gameComponent = <MatchingGameContainer onComplete={handleQuestionComplete} />;
        break;
      default:
        gameComponent = <div>Unknown question type</div>;
    }
  }

  return (
    <main className="min-h-screen flex-col items-center p-8 bg-gray-100">
      <div className="w-full max-w-6xl mx-auto flex justify-end mb-4">
        <AuthButton />
      </div>
      
      <div className="w-full max-w-6xl p-8 mx-auto bg-white rounded-xl shadow-lg">
        {!isQuizComplete ? (
          <>
            <h1 className="text-3xl font-bold mb-2 text-center text-gray-800">
              {currentQuestion.title}
            </h1>
            <p className="text-center text-gray-500 mb-6">
              Question {currentQuestionIndex + 1} of {quizQuestions.length}
            </p>
            {gameComponent}
          </>
        ) : (
          <div className="text-center py-16">
            <h1 className="text-4xl font-bold text-green-600 mb-4">Quiz Complete!</h1>
            <p className="text-lg text-gray-700 mb-8">You have completed all the questions. Great job!</p>
            <Link href="/dashboard" className="bg-green-500 text-white font-bold py-3 px-6 rounded-lg hover:bg-green-600 transition-colors text-lg">
              View Your Dashboard
            </Link>
          </div>
        )}
      </div>
    </main>
  );
}