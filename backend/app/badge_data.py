# File: backend/app/badge_data.py

BADGES = {
    "first_quiz": {
        "id": "first_quiz",
        "name": "شروع کننده",
        "description": "اولین آزمون خود را کامل کردید.",
        "icon": "fas fa-play", # (از آیکون‌های Font Awesome استفاده خواهیم کرد)
        "criteria": {
            "type": "complete_quiz",
            "count": 1
        }
    },
    "score_100": {
        "id": "score_100",
        "name": "امتیاز آور",
        "description": "به ۱۰۰ امتیاز کل رسیدید.",
        "icon": "fas fa-star",
        "criteria": {
            "type": "reach_score",
            "score": 100
        }
    },
    "level_5": {
        "id": "level_5",
        "name": "حرفه‌ای",
        "description": "به سطح ۵ رسیدید.",
        "icon": "fas fa-trophy",
        "criteria": {
            "type": "reach_level",
            "level": 5
        }
    },
    "streak_3": {
        "id": "streak_3",
        "name": "روی دور",
        "description": "۳ سوال را پشت سر هم درست جواب دادید.",
        "icon": "fas fa-fire",
        "criteria": {
            "type": "correct_streak",
            "count": 3
        }
    }
    # ... می‌توان نشان‌های بیشتری برای ماژول‌های خاص اضافه کرد ...
}