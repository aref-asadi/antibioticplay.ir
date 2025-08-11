// app/components/classification-game/Dropzone.tsx
'use client';
import React from 'react';
import { useDroppable } from '@dnd-kit/core';

type Props = {
  id: string;
  name: string;
  children: React.ReactNode;
};

export function Dropzone({ id, name, children }: Props) {
  const { setNodeRef, isOver } = useDroppable({
    id: id,
  });

  const style = {
    backgroundColor: isOver ? '#e0e0e0' : '#f9f9f9',
  };

  return (
    <div className="p-4 border border-dashed border-gray-400 rounded-lg min-h-[80px]">
      <div className="mb-2 font-semibold text-gray-700">{name}</div>
      <div
        ref={setNodeRef}
        style={style}
        className="space-y-2 transition-colors min-h-[50px]"
      >
        {children}
      </div>
    </div>
  );
}