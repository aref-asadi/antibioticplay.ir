# AntibioticPlay 💊

**AntibioticPlay** یک پلتفرم گیمیفیکیشن و آزمون تعاملی برای دانشجویان داروسازی است. هدف این پروژه آموزش مباحث پیچیده آنتی‌بیوتیک‌ها از طریق آزمون‌های جذاب، رقابت در لیدربورد و کسب نشان‌های افتخار است.

## 🚀 ویژگی‌ها

* **آزمون‌های تعاملی:** شامل سوالات چندگزینه‌ای، جای خالی (Drag & Drop) و وصل‌کردنی.
* **گیمیفیکیشن:** سیستم امتیازدهی هوشمند، سطح‌بندی (Leveling) و استریک (Streak).
* **لیدربورد (لیگ):** رقابت با سایر کاربران در لیگ‌های برنز تا الماس.
* **نشان‌ها (Badges):** اهدای مدال برای دستاوردهای خاص.
* **طراحی واکنش‌گرا:** قابل استفاده در موبایل و دسکتاپ با رابط کاربری مدرن.

## 🛠 تکنولوژی‌های استفاده شده

* **Frontend:** Vue.js 3 (Vite), Pinia, Axios
* **Backend:** Python (Flask), Flask-RESTful, Flask-JWT-Extended
* **Database:** MongoDB
* **Design:** Custom CSS (Duolingo-inspired style), FontAwesome

## 📦 نصب و راه‌اندازی (لوکال)

برای اجرای پروژه روی سیستم خودتان مراحل زیر را طی کنید:

### ۱. پیش‌نیازها
* Python 3.8+
* Node.js 16+
* MongoDB (نصب شده یا استفاده از سرویس ابری مثل Atlas/Liara)

### ۲. تنظیمات Backend
```bash
cd backend
# ساخت محیط مجازی
python -m venv venv
# فعال‌سازی (ویندوز)
venv\Scripts\activate
# فعال‌سازی (مک/لینوکس)
source venv/bin/activate

# نصب پکیج‌ها
pip install -r requirements.txt

# ساخت فایل .env و تنظیم متغیرهای محیطی (SECRET_KEY, MONGO_URI, JWT_SECRET_KEY)
# سپس برای پر کردن دیتابیس با سوالات اولیه:
python seed_db.py

# اجرای سرور
python run.py