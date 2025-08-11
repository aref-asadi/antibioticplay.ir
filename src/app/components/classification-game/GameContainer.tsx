'use client';
import React, { useState } from 'react';
import { DndContext, DragEndEvent, PointerSensor, useSensor, useSensors } from '@dnd-kit/core';
import { DraggableItem } from './DraggableItem';
import { Dropzone } from './Dropzone';

type Drug = {
  id: string;
  name: string;
};

const DRUGS: Drug[] = [
  { id: 'drug-1', name: 'Penicillin G' },
  { id: 'drug-2', name: 'Ampicillin' },
  { id: 'drug-3', name: 'Piperacillin' },
  { id: 'drug-4', name: 'Nafcillin' },
  { id: 'drug-5', name: 'Penicillin V' },
  { id: 'drug-6', name: 'Amoxicillin' },
  { id: 'drug-7', name: 'Cloxacillin' },
];

const CATEGORIES = {
  'zone-natural': 'Natural penicillin',
  'zone-anti-staph': 'Anti-staphylococcal penicillin',
  'zone-gen2': 'Second-generation broad-spectrum penicillin',
  'zone-gen4': 'Fourth-generation broad-spectrum penicillin',
};

const CORRECT_ANSWERS: { [key: string]: string[] } = {
  'zone-natural': ['drug-1', 'drug-5'],
  'zone-anti-staph': ['drug-4', 'drug-7'],
  'zone-gen2': ['drug-2', 'drug-6'],
  'zone-gen4': ['drug-3'],
};

type Props = {
  onComplete: (result: { score: number; maxScore: number; quizName: string }) => void;
};

export function GameContainer({ onComplete }: Props) {
  const [droppedItems, setDroppedItems] = useState<{ [key: string]: string[] }>({
    'zone-natural': [], 'zone-anti-staph': [], 'zone-gen2': [], 'zone-gen4': [],
  });
  const [unassignedItems, setUnassignedItems] = useState(DRUGS);
  const [showResults, setShowResults] = useState(false);
  const [score, setScore] = useState<number | null>(null);

  const sensors = useSensors(useSensor(PointerSensor));

  // --- THIS FUNCTION HAS BEEN REWRITTEN TO FIX THE DUPLICATION BUG ---
  function handleDragEnd(event: DragEndEvent) {
    if (showResults) return;
    const { active, over } = event;
    const drugId = active.id as string;
    const targetZoneId = over?.id as string | null;

    // Find which zone the item is currently in (if any)
    let sourceZoneId: string | null = null;
    for (const zone in droppedItems) {
      if (droppedItems[zone].includes(drugId)) {
        sourceZoneId = zone;
        break;
      }
    }

    // If the item hasn't moved, do nothing
    if (sourceZoneId === targetZoneId) return;

    // Create copies of the state to modify
    const newDroppedItems = { ...droppedItems };
    let newUnassignedItems = [...unassignedItems];

    // 1. Remove the item from its original location
    if (sourceZoneId) {
      // It was in a dropzone
      newDroppedItems[sourceZoneId] = newDroppedItems[sourceZoneId].filter(id => id !== drugId);
    } else {
      // It was in the unassigned list
      newUnassignedItems = newUnassignedItems.filter(item => item.id !== drugId);
    }

    // 2. Add the item to its new location
    if (targetZoneId && newDroppedItems[targetZoneId]) {
      // It's being dropped into a valid zone
      newDroppedItems[targetZoneId].push(drugId);
    } else {
      // It's being dropped back into the unassigned list
      const drug = DRUGS.find(d => d.id === drugId);
      if (drug) {
        newUnassignedItems.push(drug);
      }
    }
    
    // 3. Update the state
    setDroppedItems(newDroppedItems);
    setUnassignedItems(newUnassignedItems);
  }
  // --- END OF REWRITTEN FUNCTION ---

  async function handleCheckAnswers() {
    setShowResults(true);
    let currentScore = 0;
    const maxScore = DRUGS.length;

    for (const zoneId in droppedItems) {
      for (const drugId of droppedItems[zoneId]) {
        if (CORRECT_ANSWERS[zoneId]?.includes(drugId)) {
          currentScore++;
        }
      }
    }
    setScore(currentScore);
    
    try {
      console.log('Attempting to save Classification score...');
      const response = await fetch('/api/scores', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ score: currentScore, maxScore, quizName: 'Penicillin Classification' }),
      });
      if (!response.ok) throw new Error('Failed to save score');
      const savedScore = await response.json();
      console.log('Classification score saved!', savedScore);
    } catch (error) {
      console.error('Error saving score:', error);
    }
    
    onComplete({ score: currentScore, maxScore, quizName: 'Penicillin Classification' });
  }

  return (
    <DndContext onDragEnd={handleDragEnd} sensors={sensors}>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="md:col-span-2 space-y-4">
          {Object.entries(CATEGORIES).map(([zoneId, name]) => (
            <Dropzone key={zoneId} id={zoneId} name={name}>
              {droppedItems[zoneId].map((drugId) => {
                const drug = DRUGS.find((d) => d.id === drugId);
                return drug ? <DraggableItem key={drugId} id={drugId} name={drug.name} /> : null;
              })}
            </Dropzone>
          ))}
        </div>

        <div className="p-4 bg-gray-100 border rounded-lg">
          <h3 className="font-bold mb-4">Antibiotics</h3>
          <div className="space-y-2">
            {unassignedItems.map((drug) => (
              <DraggableItem key={drug.id} id={drug.id} name={drug.name} />
            ))}
          </div>
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
          <div className="text-2xl font-bold">
            Your Score: {score} / {DRUGS.length}
          </div>
        )}
      </div>
    </DndContext>
  );
}