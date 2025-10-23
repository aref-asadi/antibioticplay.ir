# File: backend/seed_db.py

from app import create_app, mongo
from app.quiz_data import QUIZZES
from app.badge_data import BADGES # <-- *** ایمپورت جدید ***

app = create_app()

with app.app_context():
    # --- Seed Quizzes (بدون تغییر) ---
    mongo.db.quizzes.drop()
    print("Existing quizzes collection dropped.")
    all_quizzes = list(QUIZZES.values())
    mongo.db.quizzes.insert_many(all_quizzes)
    count_q = mongo.db.quizzes.count_documents({})
    print(f"Successfully inserted {count_q} quiz modules.")

    # --- *** بخش جدید: Seed Badges *** ---
    mongo.db.badges.drop()
    print("Existing badges collection dropped.")
    all_badges = list(BADGES.values())
    mongo.db.badges.insert_many(all_badges)
    count_b = mongo.db.badges.count_documents({})
    print(f"Successfully inserted {count_b} badges.")