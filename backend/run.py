# File: backend/run.py

from app import create_app

# ساخت یک نمونه از اپلیکیشن با استفاده از factory
app = create_app()

if __name__ == '__main__':
    # اجرای سرور توسعه فلسک
    # debug=True باعث می‌شود که با هر تغییر در کد، سرور به صورت خودکار ری‌استارت شود.
    app.run(debug=True)