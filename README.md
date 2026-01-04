# 💊 بازی آموزش آنتی‌بیوتیک (Antibiotic Play)

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Vue.js](https://img.shields.io/badge/Frontend-Vue.js_3-4FC08D?logo=vue.js)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb)

یک پلتفرم وب گیمیفیکیشن (Gamified) برای دانشجویان داروسازی جهت یادگیری و تمرین مباحث مربوط به آنتی‌بیوتیک‌ها، دوزینگ، مکانیسم اثر و طبقه‌بندی داروها.


## ✨ ویژگی‌ها

### 🎮 بخش آزمون و گیمیفیکیشن
- **انواع سوالات تعاملی:** Drag & Drop، انتخاب چندگزینه‌ای، پر کردن جاهای خالی و برچسب‌گذاری تصاویر.
- **سیستم امتیازدهی:** کسب امتیاز، ارتقای سطح (Level Up) و نمایش نوار پیشرفت.
- **نشان‌ها (Badges):** دریافت مدال‌های افتخار با تکمیل دستاوردهای خاص.
- **لیدربرد (Leaderboard):** رقابت در لیگ‌های برنز، نقره، طلا و الماس.

### 🛠 امکانات فنی
- احراز هویت امن با **JWT**.
- ذخیره‌سازی پیشرفت کاربران در **MongoDB**.
- پنل مدیریت و گزارش‌گیری (خروجی Excel).


## 🚀 تکنولوژی‌های استفاده شده

- **Frontend:** Vue.js 3, Vite, Pinia, Vue Router, Tailwind CSS, Axios.
- **Backend:** Python, Flask, Flask-RESTful, PyMongo.
- **Database:** MongoDB.


## 🛠 راهنمای نصب و اجرا (Local Development)

برای اجرای این پروژه روی سیستم خودتان، مراحل زیر را دنبال کنید.

### پیش‌نیازها
1. نصب [Node.js](https://nodejs.org/) (نسخه 16 به بالا).
2. نصب [Python](https://www.python.org/) (نسخه 3.8 به بالا).
3. نصب و اجرای سرویس [MongoDB](https://www.mongodb.com/try/download/community) روی پورت پیش‌فرض (27017).

### ۱. دریافت پروژه

```bash
git clone [https://github.com/aref-asadi/antibioticplay.git](https://github.com/aref-asadi/antibioticplay.git)
cd antibioticplay
```

### ۲. راه‌اندازی Backend

وارد پوشه بک‌اند شوید و محیط مجازی را بسازید:

```bash
cd backend

# ساخت محیط مجازی (Virtual Environment)
python -m venv venv

# فعال‌سازی محیط مجازی
# در ویندوز:
venv\Scripts\activate
# در مک/لینوکس:
source venv/bin/activate
```

نصب وابستگی‌ها و تنظیمات اولیه:

```bash
# نصب پکیج‌های پایتون
pip install -r requirements.txt

# (اختیاری) پر کردن دیتابیس با داده‌های اولیه
python seed_db.py

# اجرای سرور
python run.py
```

سرور بک‌اند اکنون روی آدرس `http://localhost:5000` در حال اجراست.

> **نکته:** تنظیمات دیتابیس در فایل `backend/config.py` قرار دارد. به صورت پیش‌فرض به `mongodb://localhost:27017/antibiotic-game` متصل می‌شود.

### ۳. راه‌اندازی Frontend

یک ترمینال جدید باز کنید (ترمینال قبلی را نبندید) و وارد پوشه فرانت‌اند شوید:

```bash
cd frontend

# نصب پکیج‌های جاوااسکریپت
npm install

# اجرای برنامه در حالت توسعه
npm run dev
```

برنامه اکنون روی آدرس `http://localhost:5173` در دسترس است.


## 👥 مشارکت (Contributing)

ما از مشارکت شما استقبال می‌کنیم! برای همکاری:

1. این مخزن را Fork کنید.
2. یک شاخه (Branch) جدید برای ویژگی خود بسازید (`git checkout -b feature/AmazingFeature`).
3. تغییرات را Commit کنید (`git commit -m 'Add some AmazingFeature'`).
4. به شاخه اصلی Push کنید (`git push origin feature/AmazingFeature`).
5. یک Pull Request باز کنید.