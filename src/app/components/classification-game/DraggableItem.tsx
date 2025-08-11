// app/components/classification-game/DraggableItem.tsx
'use client';
import React from 'react';
import { useDraggable } from '@dnd-kit/core';
import { CSS } from '@dnd-kit/utilities';

type Props = {
  id: string;
  name: string;
};

export function DraggableItem({ id, name }: Props) {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: id,
  });
  const style = {
    transform: CSS.Translate.toString(transform),
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...listeners}
      {...attributes}
      className="p-2 bg-white border border-gray-300 rounded-md shadow-sm cursor-grab touch-none"
    >
      {name}
    </div>
  );
}