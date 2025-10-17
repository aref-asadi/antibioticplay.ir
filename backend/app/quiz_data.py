# File: backend/app/quiz_data.py

QUIZZES = {
    "classification-structure": {
        "id": "classification-structure",
        "title": "Classification & Structure",
        "questions": [
            {
                "id": "penicillin_classification",
                "type": "drag-drop-match",
                "title": "طبقه‌بندی پنی‌سیلین‌ها",
                "instruction": "هر کدام از آنتی‌بیوتیک‌های پنی‌سیلین را در دسته درست خود قرار دهید.",
                "items": [
                    {"id": "item-1", "text": "پنی سیلین جی"},
                    {"id": "item-2", "text": "آمپی سیلین"},
                    {"id": "item-3", "text": "پیپراسیلین"},
                    {"id": "item-4", "text": "نفیسیلین"},
                    {"id": "item-5", "text": "پنی سیلین وی"},
                    {"id": "item-6", "text": "آموکسی سیلین"},
                    {"id": "item-7", "text": "کلوگزاسیلین"}
                ],
                "categories": [
                    {"id": "cat-1", "text": "پنی سیلین طبیعی"},
                    {"id": "cat-2", "text": "پنی سیلین ضد استافیلوکوک"},
                    {"id": "cat-3", "text": "پنی سیلین وسیع الطیف نسل دوم"},
                    {"id": "cat-4", "text": "پنی سیلین وسیع الطیف نسل چهارم"}
                ],
                "solution": {
                    "item-1": "cat-1", "item-5": "cat-1",
                    "item-4": "cat-2", "item-7": "cat-2",
                    "item-2": "cat-3", "item-6": "cat-3",
                    "item-3": "cat-4"
                }
            },
            # ... بقیه سوالات این ماژول
        ]
    },
    "dosage-forms": {
        "id": "dosage-forms",
        "title": "Dosage Forms",
        "questions": [
             # ... سوالات مربوط به اشکال دارویی
        ]
    },
    "clinical-application": {
        "id": "clinical-application",
        "title": "Clinical Application",
        "questions": [
             # ... سوالات مربوط به کاربرد بالینی
        ]
    }
}