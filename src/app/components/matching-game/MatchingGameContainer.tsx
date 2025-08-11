'use client';
import React, { useState, useEffect } from 'react';

const QUIZ_NAME = "Dosage Forms Matching";

type Answer = { id: string; text: string; };

const QUESTIONS = [
  { id: 'q1', text: 'Amoxicillin' },
  { id: 'q2', text: 'Ampicillin' },
  { id: 'q3', text: 'Piperacillin' },
  { id: 'q4', text: 'Ceftazidime' },
];

const ANSWERS: Answer[] = [
  { id: 'a1', text: 'Clavulanate' },
  { id: 'a2', text: 'Sulbactam' },
  { id: 'a3', text: 'Tazobactam' },
  { id: 'a4', text: 'Avibactam' },
];

const CORRECT_PAIRS: { [key: string]: string } = {
  'q1': 'a1',
  'q2': 'a2',
  'q3': 'a3',
  'q4': 'a4',
};

type Props = {
  onComplete: (result: { score: number; maxScore: number; quizName: string }) => void;
};

export function MatchingGameContainer({ onComplete }: Props) {
  const [userAnswers, setUserAnswers] = useState<{ [key: string]: string | null }>({});
  const [selectedQuestion, setSelectedQuestion] = useState<string | null>(null);
  const [shuffledAnswers, setShuffledAnswers] = useState<Answer[]>(ANSWERS);
  const [score, setScore] = useState<number | null>(null);
  const [showResults, setShowResults] = useState(false);

  useEffect(() => {
    setShuffledAnswers(prev => [...prev].sort(() => Math.random() - 0.5));
  }, []);

  const handleSelectQuestion = (questionId: string) => {
    if (showResults) return;
    setSelectedQuestion(questionId);
  };

  const handleSelectAnswer = (answerId: string) => {
    if (selectedQuestion && !showResults) {
      setUserAnswers(prev => ({ ...prev, [selectedQuestion]: answerId }));
      setSelectedQuestion(null);
    }
  };

  async function handleCheckAnswers() {
    let currentScore = 0;
    for (const questionId in CORRECT_PAIRS) {
      if (userAnswers[questionId] === CORRECT_PAIRS[questionId]) {
        currentScore++;
      }
    }
    setScore(currentScore);
    setShowResults(true);

    // --- THIS IS THE FIX: ADD THE FETCH CALL BACK IN ---
    try {
      console.log('Attempting to save Matching score...');
      const response = await fetch('/api/scores', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ score: currentScore, maxScore: QUESTIONS.length, quizName: QUIZ_NAME }),
      });
      if (!response.ok) throw new Error('Failed to save score');
      const savedScore = await response.json();
      console.log('Matching score saved!', savedScore);
    } catch (error) {
      console.error('Error saving score:', error);
    }
    // --- END OF FIX ---

    onComplete({ score: currentScore, maxScore: QUESTIONS.length, quizName: QUIZ_NAME });
  }

  return (
    <div>
      <div className="grid grid-cols-2 gap-8">
        <div className="space-y-4">
          <h3 className="font-bold text-lg">Antibiotic</h3>
          {QUESTIONS.map(q => (
            <div
              key={q.id}
              onClick={() => handleSelectQuestion(q.id)}
              className={`p-3 border rounded-lg cursor-pointer transition-all ${selectedQuestion === q.id ? 'bg-blue-200 border-blue-400 ring-2 ring-blue-300' : 'bg-gray-50 hover:bg-gray-100'} ${userAnswers[q.id] ? 'bg-green-100 border-green-300' : ''}`}
            >
              {q.text}
              {userAnswers[q.id] && (
                <span className="ml-4 text-green-700 font-semibold">
                  → {ANSWERS.find(a => a.id === userAnswers[q.id])?.text}
                </span>
              )}
              {showResults && userAnswers[q.id] !== CORRECT_PAIRS[q.id] && (
                 <div className="text-red-600 text-sm mt-1">
                    Correct: {ANSWERS.find(a => a.id === CORRECT_PAIRS[q.id])?.text}
                 </div>
              )}
            </div>
          ))}
        </div>
        
        <div className="space-y-4">
          <h3 className="font-bold text-lg">Inhibitor</h3>
          {shuffledAnswers.map(a => (
            <div
              key={a.id}
              onClick={() => handleSelectAnswer(a.id)}
              className={`p-3 border rounded-lg cursor-pointer transition-all ${selectedQuestion ? 'hover:bg-blue-100' : 'cursor-not-allowed'}`}
            >
              {a.text}
            </div>
          ))}
        </div>
      </div>
      
      <div className="mt-8 text-center">
        {!showResults ? (
          <button
            onClick={handleCheckAnswers}
            className="bg-blue-600 text-white font-bold py-2 px-6 rounded-lg hover:bg-blue-700 transition-colors"
          >
            Check Answers
          </button>
        ) : (
          <div className="mt-4 text-2xl font-bold">
            Your Score: {score} / {QUESTIONS.length}
          </div>
        )}
      </div>
    </div>
  );
}