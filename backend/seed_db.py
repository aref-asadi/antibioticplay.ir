# File: backend/seed_db.py

from app import create_app, mongo
from app.quiz_data import QUIZZES

app = create_app()

with app.app_context():
    # حذف داده‌های قبلی برای جلوگیری از تکرار
    mongo.db.quizzes.drop()
    print("Existing quizzes collection dropped.")

    all_quizzes = list(QUIZZES.values())

    # وارد کردن داده‌های جدید
    mongo.db.quizzes.insert_many(all_quizzes)

    count = mongo.db.quizzes.count_documents({})
    print(f"Successfully inserted {count} quiz modules into the database.")