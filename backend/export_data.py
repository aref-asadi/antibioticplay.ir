import csv
import json
import datetime
from app import create_app, mongo

# ایجاد اپلیکیشن برای دسترسی به دیتابیس
app = create_app()

def export_users_to_csv():
    with app.app_context():
        print("⏳ در حال دریافت اطلاعات کاربران...")
        users = mongo.db.users.find()
        
        # نام فایل خروجی با تاریخ و ساعت
        filename = f"users_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        
        # باز کردن فایل برای نوشتن (encoding='utf-8-sig' برای پشتیبانی صحیح از فارسی در اکسل)
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = [
                'نام کاربری', 
                'نام', 
                'نام خانوادگی', 
                'ایمیل', 
                'امتیاز کل', 
                'سطح (Level)', 
                'تعداد آزمون‌های تکمیل شده',
                'تعداد نشان‌ها',
                'جزئیات آزمون‌ها (Quiz Progress)'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            count = 0
            for user in users:
                # تبدیل داده‌های پیچیده به متن ساده
                quiz_progress_str = ""
                if 'quiz_progress' in user and user['quiz_progress']:
                    # خلاصه کردن وضعیت آزمون‌ها
                    details = []
                    for quiz_id, data in user['quiz_progress'].items():
                        score = data.get('best_score', 0)
                        attempts = data.get('attempts', 0)
                        details.append(f"{quiz_id}: (نمره: {score} | تلاش: {attempts})")
                    quiz_progress_str = " | ".join(details)

                writer.writerow({
                    'نام کاربری': user.get('username', ''),
                    'نام': user.get('first_name', ''),
                    'نام خانوادگی': user.get('last_name', ''),
                    'ایمیل': user.get('email', ''),
                    'امتیاز کل': user.get('score', 0),
                    'سطح (Level)': user.get('level', 1),
                    'تعداد آزمون‌های تکمیل شده': user.get('quizzes_completed', 0),
                    'تعداد نشان‌ها': len(user.get('badges_earned', [])),
                    'جزئیات آزمون‌ها (Quiz Progress)': quiz_progress_str
                })
                count += 1
                
        print(f"✅ اطلاعات {count} کاربر با موفقیت در فایل '{filename}' ذخیره شد.")

if __name__ == "__main__":
    export_users_to_csv()