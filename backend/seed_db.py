from app import create_app, mongo
from app.quiz_data import QUIZZES
from app.badge_data import BADGES

app = create_app()

with app.app_context():
    print("--- Starting Database Reset ---")

    mongo.db.quizzes.drop()
    print("✅ Existing quizzes collection dropped.")
    
    mongo.db.badges.drop()
    print("✅ Existing badges collection dropped.")

    mongo.db.users.drop()
    print("✅ Users collection dropped (Fresh Start).")

    all_quizzes = list(QUIZZES.values())
    if all_quizzes:
        mongo.db.quizzes.insert_many(all_quizzes)
    print(f"🚀 Successfully inserted {len(all_quizzes)} quiz modules.")

    all_badges = list(BADGES.values())
    if all_badges:
        mongo.db.badges.insert_many(all_badges)
    print(f"🚀 Successfully inserted {len(all_badges)} badges.")

    print("--- Database Reset Complete ---")