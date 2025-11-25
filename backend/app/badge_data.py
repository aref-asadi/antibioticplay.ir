BADGES = {
    "first_quiz": {
        "id": "first_quiz",
        "name": "شروع کننده",
        "description": "اولین آزمون خود را کامل کردید.",
        "icon": "fas fa-play",
        "criteria": {
            "type": "complete_quiz",
            "count": 1
        }
    },
    "score_30": {
        "id": "score_30",
        "name": "امتیاز آور",
        "description": "به ۳۰ امتیاز کل رسیدید.",
        "icon": "fas fa-star",
        "criteria": {
            "type": "reach_score",
            "score": 30
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
}