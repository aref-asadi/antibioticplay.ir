# File: backend/app/quiz_data.py

# 
# این فایل شامل تمام داده‌های سوالات است که به صورت دستی از PDF استخراج شده‌اند.
# ساختار داده برای انواع مختلف سوالات:
#
# 1. type: "drag-drop-match"
#    - items: گزینه‌های قابل کشیدن (لیستی از دیکشنری‌ها)
#    - categories: ستون‌ها یا سبدهایی که آیتم‌ها در آن رها می‌شوند (لیستی از دیکشنری‌ها)
#    - solution: یک دیکشنری که { "item_id": "category_id" } را مشخص می‌کند
#
# 2. type: "multiple-select"
#    - options: لیستی از تمام گزینه‌های ممکن (رشته)
#    - solution: لیستی از گزینه‌های صحیح (رشته)
#
# 3. type: "true-false"
#    - statements: لیستی از دیکشنری‌ها، هر کدام شامل { "id": "s1", "text": "متن گزاره", "solution": True/False }
#
# 4. type: "drag-drop-fill"
#    - instruction_template: متن سوال با Placeholder هایی مانند _BLANK1_
#    - options: لیستی از گزینه‌های قابل کشیدن (دیکشنری)
#    - blanks: لیستی از دیکشنری‌ها، هر کدام شامل { "id": "_BLANK1_", "solution_id": "option_id_correct" }
#
# 5. type: "drag-drop-ordering"
#    - items: آیتم‌هایی که باید مرتب شوند (لیستی از دیکشنری‌ها)
#    - categories: جایگاه‌های مرتب (مثلاً ۱، ۲، ۳، ۴)
#    - solution: یک دیکشنری که { "item_id": "category_id" } را مشخص می‌کند
#

QUIZZES = {
    # ====================================================================
    # MODULE 1: Classification & Structure
    # ====================================================================
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
                    {"id": "p-item-1", "text": "پنی سیلین جی"},
                    {"id": "p-item-2", "text": "آمپی سیلین"},
                    {"id": "p-item-3", "text": "پیپراسیلین"},
                    {"id": "p-item-4", "text": "نفیسیلین"},
                    {"id": "p-item-5", "text": "پنی سیلین وی"},
                    {"id": "p-item-6", "text": "آموکسی سیلین"},
                    {"id": "p-item-7", "text": "کلوگزاسیلین"}
                ],
                "categories": [
                    {"id": "p-cat-1", "text": "پنی سیلین طبیعی"},
                    {"id": "p-cat-2", "text": "پنی سیلین ضد استافیلوکوک"},
                    {"id": "p-cat-3", "text": "پنی سیلین وسیع الطیف نسل دوم"},
                    {"id": "p-cat-4", "text": "پنی سیلین وسیع الطیف نسل چهارم"}
                ],
                "solution": {
                    "p-item-1": "p-cat-1",
                    "p-item-5": "p-cat-1",
                    "p-item-4": "p-cat-2",
                    "p-item-7": "p-cat-2",
                    "p-item-2": "p-cat-3",
                    "p-item-6": "p-cat-3",
                    "p-item-3": "p-cat-4"
                },
                "points_per_correct": 1
            },
            {
                "id": "cephalosporin_classification",
                "type": "drag-drop-match",
                "title": "طبقه‌بندی سفالوسپورین‌ها",
                "instruction": "هر داروی سفالوسپورین را در گروه مناسب خود قرار دهید.",
                "items": [
                    {"id": "c-item-1", "text": "سفیکسیم"},
                    {"id": "c-item-2", "text": "سفپیم"},
                    {"id": "c-item-3", "text": "سفتریاکسون"},
                    {"id": "c-item-4", "text": "سفوروکسیم"},
                    {"id": "c-item-5", "text": "سفازولین"},
                    {"id": "c-item-6", "text": "سفالکسین"},
                    {"id": "c-item-7", "text": "سفوتاکسیم"},
                    {"id": "c-item-8", "text": "سفتی زوکسیم"}
                ],
                "categories": [
                    {"id": "c-cat-1", "text": "نسل اول"},
                    {"id": "c-cat-2", "text": "نسل دوم"},
                    {"id": "c-cat-3", "text": "نسل سوم"},
                    {"id": "c-cat-4", "text": "نسل چهارم"}
                ],
                "solution": {
                    "c-item-5": "c-cat-1",
                    "c-item-6": "c-cat-1",
                    "c-item-4": "c-cat-2",
                    "c-item-1": "c-cat-3",
                    "c-item-3": "c-cat-3",
                    "c-item-7": "c-cat-3",
                    "c-item-8": "c-cat-3",
                    "c-item-2": "c-cat-4"
                },
                "points_per_correct": 1
            }
        ]
    },
    # ====================================================================
    # MODULE 2: Dosage Forms
    # ====================================================================
    "dosage-forms": {
        "id": "dosage-forms",
        "title": "Dosage Forms",
        "questions": [
            {
                "id": "inhibitor_combinations",
                "type": "drag-drop-match",
                "title": "ترکیب با مهارکننده‌های بتالاکتاماز",
                "instruction": "هر آنتی بیوتیک بتالاکتام را به مهارکننده بتالاکتاماز صحیح خود وصل کنید.",
                "items": [
                    {"id": "df-item-1", "text": "آموکسی سیلین"},
                    {"id": "df-item-2", "text": "آمپی سیلین"},
                    {"id": "df-item-3", "text": "پیپراسیلین"},
                    {"id": "df-item-4", "text": "سفتازیدیم"}
                ],
                "categories": [
                    {"id": "df-cat-1", "text": "کلاوولانات"},
                    {"id": "df-cat-2", "text": "سولباکتام"},
                    {"id": "df-cat-3", "text": "تازو باکتام"},
                    {"id": "df-cat-4", "text": "آویباکتام"}
                ],
                "solution": {
                    "df-item-1": "df-cat-1",
                    "df-item-2": "df-cat-2",
                    "df-item-3": "df-cat-3",
                    "df-item-4": "df-cat-4"
                },
                "points_per_correct": 2
            },
            {
                "id": "coamoxiclav_ratios",
                "type": "drag-drop-match",
                "title": "نسبت‌های کوآموکسی کلاو",
                "instruction": "هر فرآورده سوسپانسیون کوآموکسی کلاو را به نسبت صحیح آموکسی سیلین به کلاوولانات وصل کنید.",
                "items": [
                    {"id": "df-item-5", "text": "سوسپانسیون کوآموکسی کلاو ۲۲۸"},
                    {"id": "df-item-6", "text": "سوسپانسیون کوآموکسی کلاو ۱۵۶"},
                    {"id": "df-item-7", "text": "سوسپانسیون کوآموکسی کلاو ۶۴۳"},
                    {"id": "df-item-8", "text": "سوسپانسیون کوآموکسی کلاو ۴۵۷"},
                    {"id": "df-item-9", "text": "سوسپانسیون کوآموکسی کلاو ۳۱۲"}
                ],
                "categories": [
                    {"id": "df-cat-5", "text": "نسبت ۱:۴"},
                    {"id": "df-cat-6", "text": "نسبت ۱:۷"},
                    {"id": "df-cat-7", "text": "نسبت ۱:۱۴"}
                ],
                "solution": {
                    "df-item-6": "df-cat-5",
                    "df-item-9": "df-cat-5",
                    "df-item-5": "df-cat-6",
                    "df-item-8": "df-cat-6",
                    "df-item-7": "df-cat-7"
                },
                "points_per_correct": 2
            },
            {
                "id": "amp_sul_dosing",
                "type": "drag-drop-fill",
                "title": "ویژگی‌های آمپی‌سیلین-سولباکتام",
                "instruction_template": "داروی آمپی سیلین سولباکتام با اشکال دارویی _BLANK1_ و _BLANK2_ در بازار دارویی ایران وجود دارد و نسبت آمپی سیلین به سولباکتام در این فرآورده ها _BLANK3_ است. دوزینگ این دارو بر اساس جزء _BLANK4_ صورت می گیرد.",
                "options": [
                    {"id": "opt-7-1", "text": "۳۰ گرم"},
                    {"id": "opt-7-2", "text": "۳/۳۷۵ گرم"},
                    {"id": "opt-7-3", "text": "۱/۵ گرم"},
                    {"id": "opt-7-4", "text": "۴/۵ گرم"},
                    {"id": "opt-7-5", "text": "۲/۲۵۰ گرم"},
                    {"id": "opt-7-6", "text": "۲:۱"},
                    {"id": "opt-7-7", "text": "۳:۱"},
                    {"id": "opt-7-8", "text": "۸:۱"},
                    {"id": "opt-7-9", "text": "۱۶:۱"},
                    {"id": "opt-7-10", "text": "۴:۱"},
                    {"id": "opt-7-11", "text": "آمپی سیلین"},
                    {"id": "opt-7-12", "text": "سولباکتام"},
                    {"id": "opt-7-13", "text": "مجموع آمپی سیلین و سولباکتام"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "opt-7-3"},
                    {"id": "_BLANK2_", "solution_id": "opt-7-1"}, # 30g is likely a typo for 3g, but using PDF text
                    {"id": "_BLANK3_", "solution_id": "opt-7-6"},
                    {"id": "_BLANK4_", "solution_id": "opt-7-13"}
                ],
                "points_per_correct": 2
            },
            {
                "id": "pip_taz_dosing",
                "type": "drag-drop-fill",
                "title": "ویژگی‌های پیپراسیلین-تازو باکتام",
                "instruction_template": "داروی پیپراسیلین تازو باکتام با اشکال دارویی _BLANK1_ و _BLANK2_ در بازار دارویی ایران وجود دارد و نسبت پیپراسیلین به تازو باکتام در این فرآورده ها _BLANK3_ است. دوزینگ این دارو بر اساس جزء _BLANK4_ صورت می گیرد.",
                "options": [
                    {"id": "opt-8-1", "text": "۳۰ گرم"},
                    {"id": "opt-8-2", "text": "۳/۳۷۵ گرم"},
                    {"id": "opt-8-3", "text": "۱/۵ گرم"},
                    {"id": "opt-8-4", "text": "۴/۵ گرم"},
                    {"id": "opt-8-5", "text": "۲/۲۵۰۰ گرم"}, # Assuming 2.25g
                    {"id": "opt-8-6", "text": "۲:۱"},
                    {"id": "opt-8-7", "text": "۳:۱"},
                    {"id": "opt-8-8", "text": "۸:۱"},
                    {"id": "opt-8-9", "text": "۱۶:۱"},
                    {"id": "opt-8-10", "text": "۴:۱"},
                    {"id": "opt-8-11", "text": "پیپراسیلین"},
                    {"id": "opt-8-12", "text": "تازو باکتام"},
                    {"id": "opt-8-13", "text": "مجموع پیپراسیلین تازو باکتام"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "opt-8-5"},
                    {"id": "_BLANK2_", "solution_id": "opt-8-4"},
                    {"id": "_BLANK3_", "solution_id": "opt-8-8"},
                    {"id": "_BLANK4_", "solution_id": "opt-8-13"}
                ],
                "points_per_correct": 2
            },
            {
                "id": "imipenem_dosing",
                "type": "multiple-select",
                "title": "محاسبه دوز ایمی‌پنم-سیلاستاتین",
                "instruction": "برای بیماری داروی ایمی پنم سیلاستاتین با دوز ۵۰۰ میلی گرم هر ۶ ساعت تجویز شده است کدام یک از گزینههای زیر را میتوان در هر بار تزریق دارو برای بیمار انتخاب کرد؟ (ممکن است بیش از یک گزینه صحیح باشد)",
                "options": [
                    "یک ویال ۵۰۰/۵۰۰ میلی گرم",
                    "یک ویال ۲۵۰/۲۵۰ میلی گرم",
                    "دو ویال ۲۵۰/۲۵۰ میلی گرم",
                    "نصف ویال ۵۰۰/۵۰۰ میلی گرم",
                    "نصف ویال ۷۵۰/۲۵۰ میلی گرم"
                ],
                "solution": [
                    "یک ویال ۵۰۰/۵۰۰ میلی گرم",
                    "دو ویال ۲۵۰/۲۵۰ میلی گرم"
                ],
                "points_per_correct": 5
            },
            {
                "id": "quinolone_eye_drops",
                "type": "multiple-select",
                "title": "قطره‌های چشمی فلوروکینولون",
                "instruction": "کدام یک از داروهای فلوروکینولون در بازار دارویی ایران شکل دارویی قطره چشمی دارند؟",
                "options": [
                    "سیپروفلوکساسین",
                    "لووفلوكساسين",
                    "موکسی فلوکساسین",
                    "جمی فلوکساسین"
                ],
                "solution": [
                    "سیپروفلوکساسین",
                    "لووفلوكساسين",
                    "موکسی فلوکساسین"
                ],
                "points_per_correct": 3
            },
            {
                "id": "macrolide_dosage_forms",
                "type": "drag-drop-match",
                "title": "اشکال دارویی ماکرولیدها",
                "instruction": "هر شکل دارویی را به داروی ماکرولید متناسب آن وصل کنید.",
                "items": [
                    {"id": "m-item-1", "text": "سوسپانسیون 250mg/5ml"},
                    {"id": "m-item-2", "text": "محلول موضعی ۴ درصد"},
                    {"id": "m-item-3", "text": "سوسپانسیون 125mg/5ml"},
                    {"id": "m-item-4", "text": "سوسپانسیون ER دو گرمی"},
                    {"id": "m-item-5", "text": "قطره چشمی ۱ درصد"},
                    {"id": "m-item-6", "text": "پماد چشمی"},
                    {"id": "m-item-7", "text": "ژل موضعی ۲ درصد"},
                    {"id": "m-item-8", "text": "پودر تزریقی ۵۰۰ میلی گرم"}
                ],
                "categories": [
                    {"id": "m-cat-1", "text": "کلاریترومایسین"},
                    {"id": "m-cat-2", "text": "آزیترومایسین"},
                    {"id": "m-cat-3", "text": "اریترومایسین"}
                ],
                "solution": {
                    "m-item-1": "m-cat-1",
                    "m-item-3": "m-cat-1",
                    "m-item-4": "m-cat-2",
                    "m-item-5": "m-cat-2",
                    "m-item-8": "m-cat-2",
                    "m-item-2": "m-cat-3",
                    "m-item-6": "m-cat-3",
                    "m-item-7": "m-cat-3"
                },
                "points_per_correct": 1
            },
            {
                "id": "nitrofurantoin_formulations",
                "type": "drag-drop-match",
                "title": "فرمولاسیون‌های نیتروفورانتوئین",
                "instruction": "هر خصوصیت را به فرمولاسیون مربوطه وصل کنید.",
                "items": [
                    {"id": "n-item-1", "text": "دوزینگ چهار بار در روز"},
                    {"id": "n-item-2", "text": "تشکیل ژل در معده و آزادسازی طولانی مدت دارو"},
                    {"id": "n-item-3", "text": "دوزینگ دو بار در روز"},
                    {"id": "n-item-4", "text": "انحلال کند در معده"},
                    {"id": "n-item-5", "text": "عوارض گوارشی کمتر"}
                ],
                "categories": [
                    {"id": "n-cat-1", "text": "نیتروفورانتوئین مونوهیدرات ماکروکریستال"},
                    {"id": "n-cat-2", "text": "نیتروفورانتوئین ماکروکریستال"}
                ],
                "solution": {
                    "n-item-2": "n-cat-1",
                    "n-item-3": "n-cat-1",
                    "n-item-1": "n-cat-2",
                    "n-item-4": "n-cat-2",
                    "n-item-5": "n-cat-2"
                },
                "points_per_correct": 2
            },
            {
                "id": "antiviral_features",
                "type": "drag-drop-match",
                "title": "ویژگی‌های داروهای آنتی‌ویروس",
                "instruction": "هر ویژگی را به داروی مربوطه وصل کنید.",
                "items": [
                    {"id": "av-item-1", "text": "کرم موضعی ٪۵ و پماد چشمی ۳٪ دارد."},
                    {"id": "av-item-2", "text": "پیش دارو است و برای درمان عفونت CMV کاربرد دارد."},
                    {"id": "av-item-3", "text": "تزریقی است و در زمان آماده سازی آن باید از دستکش یکبار مصرف استفاده شود."},
                    {"id": "av-item-4", "text": "قرصهای ۵۰۰ و ۱۰۰۰ میلی گرم دارد."}
                ],
                "categories": [
                    {"id": "av-cat-1", "text": "آسیکلوویر"},
                    {"id": "av-cat-2", "text": "والاسیکلوویر"},
                    {"id": "av-cat-3", "text": "گانسیکلوویر"},
                    {"id": "av-cat-4", "text": "والگانسیلوویر"}
                ],
                "solution": {
                    "av-item-1": "av-cat-1",
                    "av-item-4": "av-cat-2",
                    "av-item-3": "av-cat-3",
                    "av-item-2": "av-cat-4"
                },
                "points_per_correct": 2
            },
            {
                "id": "azole_forms",
                "type": "drag-drop-match",
                "title": "اشکال دارویی آزول‌های ضدقارچ",
                "instruction": "هر داروی آزول ضدقارچ را به شکل دارویی خود در بازار دارویی ایران وصل کنید.",
                "items": [
                    {"id": "az-item-1", "text": "کپسول ۱۰۰ و ۱۵۰ میلی گرم"},
                    {"id": "az-item-2", "text": "شامپو ۲ درصد و قرص ۲۰۰ میلی گرم"},
                    {"id": "az-item-3", "text": "قرص ۵۰ و ۲۰۰ میلی گرم"},
                    {"id": "az-item-4", "text": "آمپول ۳۰۰ میلی گرم"},
                    {"id": "az-item-5", "text": "کپسول ۱۰۰ میلی گرم"}
                ],
                "categories": [
                    {"id": "az-cat-1", "text": "کتوکونازول"},
                    {"id": "az-cat-2", "text": "فلوکونازول"},
                    {"id": "az-cat-3", "text": "ایتراکونازول"},
                    {"id": "az-cat-4", "text": "وریکونازول"},
                    {"id": "az-cat-5", "text": "پوساکونازول"}
                ],
                "solution": {
                    "az-item-1": "az-cat-2",
                    "az-item-2": "az-cat-1",
                    "az-item-3": "az-cat-4",
                    "az-item-4": "az-cat-5",
                    "az-item-5": "az-cat-3"
                },
                "points_per_correct": 2
            }
        ]
    },
    # ====================================================================
    # MODULE 3: Clinical Application
    # ====================================================================
    "clinical-application": {
        "id": "clinical-application",
        "title": "Clinical Application",
        "questions": [
            {
                "id": "anaerobic_coverage",
                "type": "drag-drop-match",
                "title": "پوشش بیهوازی",
                "instruction": "آنتی‌بیوتیک‌های زیر را بر اساس پوشش بیهوازی در یکی از سبدها قرار دهید.",
                "items": [
                    {"id": "an-item-1", "text": "سفتازیدیم"},
                    {"id": "an-item-2", "text": "کلیندامایسین"},
                    {"id": "an-item-3", "text": "پیپراسیلین تازو باکتام"},
                    {"id": "an-item-4", "text": "مروپنم"},
                    {"id": "an-item-5", "text": "مترونیدازول"},
                    {"id": "an-item-6", "text": "موکسی فلوکساسین"},
                    {"id": "an-item-7", "text": "سیپروفلوکساسین"}
                ],
                "categories": [
                    {"id": "an-cat-1", "text": "بدون پوشش بیهوازی"},
                    {"id": "an-cat-2", "text": "دارای پوشش بیهوازی"}
                ],
                "solution": {
                    "an-item-1": "an-cat-1",
                    "an-item-7": "an-cat-1",
                    "an-item-2": "an-cat-2",
                    "an-item-3": "an-cat-2",
                    "an-item-4": "an-cat-2",
                    "an-item-5": "an-cat-2",
                    "an-item-6": "an-cat-2"
                },
                "points_per_correct": 1
            },
            {
                "id": "iv_penicillins",
                "type": "multiple-select",
                "title": "پنی‌سیلین‌های وریدی",
                "instruction": "کدام یک از پنی سیلینهای زیر به صورت وریدی قابل تجویز هستند؟",
                "options": [
                    "پنی سیلین جی سدیم",
                    "پنی سیلین وی بنزاتین",
                    "پنیسیلین وی پتاسیم",
                    "پنی سیلین جی پتاسیم",
                    "پنی سیلین جی بنزاتین",
                    "پنی سیلین ۶.۳.۳",
                    "پنی سیلین جی پروکائین"
                ],
                "solution": [
                    "پنی سیلین جی سدیم",
                    "پنی سیلین جی پتاسیم"
                ],
                "points_per_correct": 5
            },
            {
                "id": "skin_test_hold_times",
                "type": "drag-drop-match",
                "title": "قطع داروها قبل از تست پوستی پنی‌سیلین",
                "instruction": "زمان مناسب قطع هر دارو قبل از انجام تست را به نام دارو وصل کنید.",
                "items": [
                    {"id": "st-item-1", "text": "کپسول دیفن هیدرامین"},
                    {"id": "st-item-2", "text": "اسپری بینی آزلاستین"},
                    {"id": "st-item-3", "text": "شربت پرومتازین"},
                    {"id": "st-item-4", "text": "مونتلوکاست"},
                    {"id": "st-item-5", "text": "اسپری استنشاقی فلوتیکازون"},
                    {"id": "st-item-6", "text": "قرص پردنیزولون"},
                    {"id": "st-item-7", "text": "قرص فاموتیدین"}
                ],
                "categories": [
                    {"id": "st-cat-1", "text": "سه روز"},
                    {"id": "st-cat-2", "text": "یک هفته"},
                    {"id": "st-cat-3", "text": "دو هفته"},
                    {"id": "st-cat-4", "text": "دو روز"},
                    {"id": "st-cat-5", "text": "نیازی به قطع ندارد"}
                ],
                "solution": {
                    "st-item-1": "st-cat-1",
                    "st-item-2": "st-cat-1",
                    "st-item-3": "st-cat-2",
                    "st-item-4": "st-cat-4",
                    "st-item-5": "st-cat-5",
                    "st-item-6": "st-cat-5",
                    "st-item-7": "st-cat-5"
                },
                "points_per_correct": 1
            },
            {
                "id": "ceftriaxone_calcium_admin",
                "type": "drag-drop-match",
                "title": "تجویز همزمان سفتریاکسون و کلسیم",
                "instruction": "هر گروه سنی را به روش صحیح تجویز این دو دارو وصل کنید.",
                "items": [
                    {"id": "cc-item-1", "text": "تزریق یکی از دو دارو فلاشینگ لاین و سپس تزریق داروی دیگر"},
                    {"id": "cc-item-2", "text": "امکان تجویز دو دارو در یک دوره درمانی وجود ندارد"},
                    {"id": "cc-item-3", "text": "تزریق همزمان دو دارو از دو لاین مختلف"},
                    {"id": "cc-item-4", "text": "تزریق همزمان دارو از یک لاین و در یک سرم"}
                ],
                "categories": [
                    {"id": "cc-cat-1", "text": "بزرگسالان"},
                    {"id": "cc-cat-2", "text": "کودکان با سن ۲-۶ سال"},
                    {"id": "cc-cat-3", "text": "نوزادان با سن زیر ۴ هفته"},
                    {"id": "cc-cat-4", "text": "اطفال با سن ۱ ماه تا ۲ سال"}
                ],
                "solution": {
                    "cc-item-1": "cc-cat-1",
                    "cc-item-1": "cc-cat-2", # PDF shows one item to two cats, my model doesn't support this. Reversing.
                },
                "solution_reversed": { # PDF shows Cat -> Item, so I will reverse the logic for this question
                    "cc-cat-1": "cc-item-1",
                    "cc-cat-2": "cc-item-1",
                    "cc-cat-3": "cc-item-2",
                    "cc-cat-4": "cc-item-3"
                },
                "points_per_correct": 2 # This question needs custom logic in the frontend
            },
            {
                "id": "cdiff_risk_factors",
                "type": "multiple-select",
                "title": "شیوع عفونت کلستریدیوم دیفیسیل",
                "instruction": "شیوع عفونت کلستریدیوم دیفیسیل با کدام آنتی بیوتیکها از بقیه بیشتر است؟ چهار گزینه صحیح وجود دارد",
                "options": [
                    "ایمی پنم سیلاستاتین",
                    "کلرامفنیکل",
                    "سفالوسپورین ها",
                    "آمپی سیلین / آموکسی سیلین",
                    "کلیندامایسین",
                    "پنی سیلین جی",
                    "فلوروکینولون ها",
                    "مترونیدازول",
                    "ونکومایسین",
                    "ریفامپین",
                    "تتراسیکلین ها"
                ],
                "solution": [
                    "سفالوسپورین ها",
                    "آمپی سیلین / آموکسی سیلین",
                    "کلیندامایسین",
                    "فلوروکینولون ها"
                ],
                "points_per_correct": 2
            },
            {
                "id": "myasthenia_gravis_contra",
                "type": "multiple-select",
                "title": "منع مصرف در میاستنی گراویس",
                "instruction": "کدام آنتی بیوتیک ها در بیماران مبتلا به میاستنی گراویس منع مصرف یا احتیاط جدی مصرف دارند؟",
                "options": [
                    "آمپی سیلین",
                    "کوتریموکسازول",
                    "لووفلوکساسین",
                    "آمیکاسین",
                    "سیپروفلوکساسین",
                    "کلیندامایسین",
                    "سفتریاکسون",
                    "تتراسیکلین",
                    "داکسی سیکلین",
                    "نیتروفورانتوئین"
                ],
                "solution": [
                    "لووفلوکساسین",
                    "آمیکاسین",
                    "سیپروفلوکساسین",
                    "کلیندامایسین",
                    "تتراسیکلین",
                    "داکسی سیکلین"
                ],
                "points_per_correct": 1
            },
            {
                "id": "divalent_cation_interaction",
                "type": "multiple-select",
                "title": "تداخل با کاتیون‌های دو ظرفیتی",
                "instruction": "مصرف همزمان کدام آنتی بیوتیک با لبنیات و کاتیونهای دو ظرفیتی باعث *کاهش* جذب خوراکی آنها میشود؟", # Note: I corrected the PDF's question
                "options": [
                    "داکسی سیکلین",
                    "کلیندامایسین",
                    "تتراسیکلین",
                    "سیپروفلوکساسین",
                    "لووفلوکساسین",
                    "آمپی سیلین",
                    "کوآموکسی کلاو",
                    "سفیکسیم",
                    "نیتروفورانتوئین",
                    "کوتریموکسازول",
                    "آزیترومایسین",
                    "اریترومایسین"
                ],
                "solution": [
                    "داکسی سیکلین",
                    "تتراسیکلین",
                    "سیپروفلوکساسین",
                    "لووفلوکساسین"
                ],
                "points_per_correct": 2
            },
            {
                "id": "quinolone_spectrum",
                "type": "drag-drop-match",
                "title": "طیف اثر فلوروکینولون‌ها",
                "instruction": "هر داروی فلوروکینولون را به طیف اثر متناسب با آن وصل کنید.",
                "items": [
                    {"id": "q-item-1", "text": "سیپروفلوکساسین"},
                    {"id": "q-item-2", "text": "لووفلوكساسين"},
                    {"id": "q-item-3", "text": "موکسی فلوکساسین"}
                ],
                "categories": [
                    {"id": "q-cat-1", "text": "عفونت های بی هوازی"},
                    {"id": "q-cat-2", "text": "باکتریهای گرم منفی روده ای"},
                    {"id": "q-cat-3", "text": "عفونت های گرم مثبت تنفسی"}
                ],
                "solution": {
                    "q-item-3": "q-cat-1",
                    "q-item-1": "q-cat-2",
                    "q-item-2": "q-cat-3"
                },
                "points_per_correct": 3
            },
            {
                "id": "abx_side_effects",
                "type": "drag-drop-match",
                "title": "عوارض جانبی آنتی‌بیوتیک‌ها",
                "instruction": "هر عارضه را به آنتی بیوتیک ایجاد کننده آن متصل کنید.",
                "items": [
                    {"id": "se-item-1", "text": "لووفلوکساسین"},
                    {"id": "se-item-2", "text": "ریفامپین"},
                    {"id": "se-item-3", "text": "مترونیدازول"},
                    {"id": "se-item-4", "text": "ایمی پنم سیلاستاتین"},
                    {"id": "se-item-5", "text": "تتراسیکلین"}
                ],
                "categories": [
                    {"id": "se-cat-1", "text": "زرد شدن دندان ها"},
                    {"id": "se-cat-2", "text": "طعم تلخ دهان"},
                    {"id": "se-cat-3", "text": "طولانی شدن QT در نوار قلب"},
                    {"id": "se-cat-4", "text": "تغییر رنگ ترشحات بدن"},
                    {"id": "se-cat-5", "text": "تشنج"}
                ],
                "solution": {
                    "se-item-5": "se-cat-1",
                    "se-item-3": "se-cat-2",
                    "se-item-1": "se-cat-3",
                    "se-item-2": "se-cat-4",
                    "se-item-4": "se-cat-5"
                },
                "points_per_correct": 2
            },
            {
                "id": "tetracycline_properties",
                "type": "drag-drop-match",
                "title": "ویژگی‌های خانواده تتراسیکلین",
                "instruction": "هر دارو را به خصوصیت متناسب با آن وصل کنید.",
                "items": [
                    {"id": "t-item-1", "text": "قابلیت استفاده در کودکان زیر ۸ سال"},
                    {"id": "t-item-2", "text": "مؤثر بر علیه باکتریهای مقاوم به سایر تتراسیکلین ها"},
                    {"id": "t-item-3", "text": "عدم نیاز به تعدیل دوز در نارسایی کلیوی و کبدی"},
                    {"id": "t-item-4", "text": "کاهش شدید جذب خوراکی در مصرف همزمان با کاتیونها"}
                ],
                "categories": [
                    {"id": "t-cat-1", "text": "تتراسیکلین"},
                    {"id": "t-cat-2", "text": "داکسی سیکلین"},
                    {"id": "t-cat-3", "text": "تیگسیکلین"},
                    {"id": "t-cat-4", "text": "مینوسیکلین"}
                ],
                "solution": {
                    "t-item-1": "t-cat-2",
                    "t-item-2": "t-cat-3",
                    "t-item-3": "t-cat-3", # As per PDF, two items point to Tigecycline
                    "t-item-4": "t-cat-1"
                },
                "points_per_correct": 2
            },
            {
                "id": "tetracycline_side_effects",
                "type": "drag-drop-match",
                "title": "عوارض جانبی تتراسیکلین‌ها",
                "instruction": "در مورد داروهای تتراسیکلین هر عارضه را به داروی مربوطه وصل کنید.",
                "items": [
                    {"id": "tse-item-1", "text": "طولانی شدن PT و aPTT"},
                    {"id": "tse-item-2", "text": "بیشترین ریسک سمیت نوری"},
                    {"id": "tse-item-3", "text": "بیشترین ریسک سرگیجه"},
                    {"id": "tse-item-4", "text": "بیشترین ریسک زخم مری"}
                ],
                "categories": [
                    {"id": "tse-cat-1", "text": "تیگسیکلین"},
                    {"id": "tse-cat-2", "text": "داکسی سیکلین"},
                    {"id": "tse-cat-3", "text": "دمکلوسیکلین"},
                    {"id": "tse-cat-4", "text": "مینوسیکلین"}
                ],
                "solution": {
                    "tse-item-1": "tse-cat-1",
                    "tse-item-4": "tse-cat-2",
                    "tse-item-2": "tse-cat-3",
                    "tse-item-3": "tse-cat-4"
                },
                "points_per_correct": 2
            },
            {
                "id": "macrolide_admin",
                "type": "drag-drop-match",
                "title": "روش صحیح مصرف ماکرولیدها",
                "instruction": "هر دارو را به روش صحیح مصرف خود متصل کنید.",
                "items": [
                    {"id": "ma-item-1", "text": "قرص پیوسته رهش کلاریترومایسین"},
                    {"id": "ma-item-2", "text": "سوسپانسیون پیوسته رهش آزیترومایسین"},
                    {"id": "ma-item-3", "text": "سوسپانسیون سریع رهش آزیترومایسین"},
                    {"id": "ma-item-4", "text": "قرص کلاریترومایسین"},
                    {"id": "ma-item-5", "text": "قرص آزیترومایسین"}
                ],
                "categories": [
                    {"id": "ma-cat-1", "text": "با معده خالی"},
                    {"id": "ma-cat-2", "text": "همراه غذا"},
                    {"id": "ma-cat-3", "text": "با یا بدون غذا"}
                ],
                "solution": {
                    "ma-item-3": "ma-cat-1",
                    "ma-item-1": "ma-cat-2",
                    "ma-item-2": "ma-cat-2",
                    "ma-item-4": "ma-cat-3",
                    "ma-item-5": "ma-cat-3"
                },
                "points_per_correct": 2
            },
            {
                "id": "cotrimoxazole_folate",
                "type": "true-false",
                "title": "عارضه کمبود فولات کوتریموکسازول",
                "instruction": "گزینههای درست و نادرست را مشخص کنید.",
                "statements": [
                    {"id": "tf-1-1", "text": "کمبود فولات منجر به علایم بالینی مانند آنمی ماکروسیتیک نمیشود.", "solution": False},
                    {"id": "tf-1-2", "text": "هم فولیک اسید و هم فولینیک اسید را میتوان برای آنتاگونیزه کردن این عارضه استفاده کرد.", "solution": False},
                    {"id": "tf-1-3", "text": "استفاده از مکمل فولیک اسید و یا فولینیک اسید منجر به کاهش اثر آنتی باکتریال کوتریموکسازول میشود.", "solution": False},
                    {"id": "tf-1-4", "text": "در صورت استفاده از کوتریموکسازول در زنان باردار ریسک بروز نقایص لوله عصبی وجود دارد.", "solution": True},
                    {"id": "tf-1-5", "text": "در استفاده از کوتریموکسازول برای درمان توکسوپلاسما فقط باید از فولینیک اسید به همراه آن استفاده شود نه فولیک اسید.", "solution": True}
                ],
                "points_per_correct": 2
            },
            {
                "id": "resistant_bacteria_spectrum",
                "type": "drag-drop-match",
                "title": "طیف اثر آنتی‌بیوتیک‌های مقاوم",
                "instruction": "طیف اثر هر آنتی بیوتیک را مشخص نمایید.",
                "items": [
                    {"id": "r-item-1", "text": "لینزولید"},
                    {"id": "r-item-2", "text": "ونکومايسين"},
                    {"id": "r-item-3", "text": "تیکوپلانین"},
                    {"id": "r-item-4", "text": "کلیستین"}
                ],
                "categories": [
                    {"id": "r-cat-1", "text": "عفونت گرم منفی مقاوم"},
                    {"id": "r-cat-2", "text": "عفونت گرم مثبت مقاوم"}
                ],
                "solution": {
                    "r-item-4": "r-cat-1",
                    "r-item-1": "r-cat-2",
                    "r-item-2": "r-cat-2",
                    "r-item-3": "r-cat-2"
                },
                "points_per_correct": 2
            },
            {
                "id": "abx_routes_of_admin",
                "type": "drag-drop-match",
                "title": "راه‌های تجویز آنتی‌بیوتیک",
                "instruction": "هر آنتی بیوتیک را به راههای مناسب تجویز آن وصل کنید.",
                "items": [
                    {"id": "ro-item-1", "text": "ونکومايسين"},
                    {"id": "ro-item-2", "text": "تیکو پلانین"},
                    {"id": "ro-item-3", "text": "پیپراسیلین تازو باکتام"},
                    {"id": "ro-item-4", "text": "توبرامایسین"}
                ],
                "categories": [
                    {"id": "ro-cat-1", "text": "وریدی"},
                    {"id": "ro-cat-2", "text": "وریدی / خوراکی"},
                    {"id": "ro-cat-3", "text": "وریدی / عضلانی"},
                    {"id": "ro-cat-4", "text": "وریدی / استنشاقی"}
                ],
                "solution": {
                    "ro-item-3": "ro-cat-1",
                    "ro-item-1": "ro-cat-2",
                    "ro-item-2": "ro-cat-3",
                    "ro-item-4": "ro-cat-4"
                },
                "points_per_correct": 2
            },
            {
                "id": "glycopeptide_features",
                "type": "drag-drop-match",
                "title": "ویژگی‌های ونکومایسین و لینزولید",
                "instruction": "هر آنتی بوتیک را به ویژگی متناسب با آن وصل کنید.",
                "items": [
                    {"id": "g-item-1", "text": "عارضه فلاشینگ ناشی از تزریق سریع"},
                    {"id": "g-item-2", "text": "جذب خوراکی ۱۰۰ درصدی"},
                    {"id": "g-item-3", "text": "عارضه سندروم سروتونین در مصرف همزمان با SSRI"},
                    {"id": "g-item-4", "text": "عارضه سرکوب مغز استخوان"}
                ],
                "categories": [
                    {"id": "g-cat-1", "text": "ونکومایسین"},
                    {"id": "g-cat-2", "text": "تیکوپلانین"},
                    {"id": "g-cat-3", "text": "لینزولید"}
                ],
                "solution": {
                    "g-item-1": "g-cat-1",
                    "g-item-2": "g-cat-3",
                    "g-item-3": "g-cat-3",
                    "g-item-4": "g-cat-3"
                },
                "points_per_correct": 2
            },
            {
                "id": "clinda_vs_metro",
                "type": "drag-drop-match",
                "title": "کلیندامایسین در مقابل مترونیدازول",
                "instruction": "هر ویژگی را به داروی مربوطه وصل کنید.",
                "items": [
                    {"id": "cm-item-1", "text": "جذب خوراکی تقریباً ۱۰۰ درصدی"},
                    {"id": "cm-item-2", "text": "اثر بهتر بر میکروارگانیسمهای گرم مثبت"},
                    {"id": "cm-item-3", "text": "نفوذ بهتر از سد خونی مغزی"},
                    {"id": "cm-item-4", "text": "شیوع بیشتر عفونت کلستریدیوم دیفیسیل"},
                    {"id": "cm-item-5", "text": "تداخل با الکل"},
                    {"id": "cm-item-6", "text": "عارضه طعم فلزی در دهان"}
                ],
                "categories": [
                    {"id": "cm-cat-1", "text": "کلیندامایسین"},
                    {"id": "cm-cat-2", "text": "مترونیدازول"}
                ],
                "solution": {
                    "cm-item-2": "cm-cat-1",
                    "cm-item-4": "cm-cat-1",
                    "cm-item-1": "cm-cat-2",
                    "cm-item-3": "cm-cat-2",
                    "cm-item-5": "cm-cat-2",
                    "cm-item-6": "cm-cat-2"
                },
                "points_per_correct": 1
            },
            {
                "id": "pregnancy_safety",
                "type": "drag-drop-match",
                "title": "ایمنی آنتی‌بیوتیک‌ها در بارداری",
                "instruction": "در مورد استفاده از آنتی بیوتیکها در دوران بارداری گزینه‌های درست را به هم وصل کنید.",
                "items": [
                    {"id": "pr-item-1", "text": "کلیندامایسین واژینال"},
                    {"id": "pr-item-2", "text": "کلیندامایسین تزریقی"},
                    {"id": "pr-item-3", "text": "کوتریموکسازول خوراکی"},
                    {"id": "pr-item-4", "text": "مترونیدازول خوراکی در تریمستر اول"},
                    {"id": "pr-item-5", "text": "ریفامپین"}
                ],
                "categories": [
                    {"id": "pr-cat-1", "text": "مجاز در بارداری"},
                    {"id": "pr-cat-2", "text": "ممنوع در بارداری"}
                ],
                "solution": {
                    "pr-item-1": "pr-cat-1",
                    "pr-item-2": "pr-cat-1",
                    "pr-item-5": "pr-cat-1",
                    "pr-item-3": "pr-cat-2",
                    "pr-item-4": "pr-cat-2"
                },
                "points_per_correct": 2
            },
            {
                "id": "inhaled_abx_features",
                "type": "drag-drop-match",
                "title": "ویژگی‌های آنتی‌بیوتیک‌های استنشاقی",
                "instruction": "هر ویژگی را به آنتی بیوتیک مربوطه وصل کنید.",
                "items": [
                    {"id": "in-item-1", "text": "هم شکل کپسول استنشاقی دارد و هم میتوان محلول استنشاقی را با استفاده از آمپول آن تهیه کرد."},
                    {"id": "in-item-2", "text": "محلول استنشاقی آن باید به صورت تازه تهیه شود تا از آسیب شدید تنفسی جلوگیری شود."},
                    {"id": "in-item-3", "text": "تجویز استنشاقی این دارو برای جلوگیری از عفونت ریوی در بیماران مبتلا به کنسر استفاده میشود."}
                ],
                "categories": [
                    {"id": "in-cat-1", "text": "کلیستین"},
                    {"id": "in-cat-2", "text": "توبرامایسین"},
                    {"id": "in-cat-3", "text": "آمفوتریسین-بی"}
                ],
                "solution": {
                    "in-item-2": "in-cat-1",
                    "in-item-1": "in-cat-2",
                    "in-item-3": "in-cat-3"
                },
                "points_per_correct": 3
            },
            {
                "id": "cf_inhalation_order",
                "type": "drag-drop-ordering",
                "title": "ترتیب مصرف داروهای استنشاقی در CF",
                "instruction": "ترتیب صحیح مصرف داروهای زیر را در مصرف همزمان در بیماران مبتلا به سیستیک فیبروزیس مشخص کنید.",
                "items": [
                    {"id": "cf-item-1", "text": "در ناز آلفا"},
                    {"id": "cf-item-2", "text": "توبرامایسین"},
                    {"id": "cf-item-3", "text": "برونکودیلاتور"},
                    {"id": "cf-item-4", "text": "سالین هیپرتونیک"}
                ],
                "categories": [
                    {"id": "cf-cat-1", "text": "مرحله ۱"},
                    {"id": "cf-cat-2", "text": "مرحله ۲"},
                    {"id": "cf-cat-3", "text": "مرحله ۳"},
                    {"id": "cf-cat-4", "text": "مرحله ۴"}
                ],
                "solution": {
                    "cf-item-3": "cf-cat-1",
                    "cf-item-4": "cf-cat-2",
                    "cf-item-1": "cf-cat-3",
                    "cf-item-2": "cf-cat-4"
                },
                "points_per_correct": 2
            },
            {
                "id": "antiviral_spectrum",
                "type": "drag-drop-match",
                "title": "طیف اثر داروهای ضد ویروس",
                "instruction": "طیف اثر هر داروی ضد ویروس را به آن متصل کنید.",
                "items": [
                    {"id": "avs-item-1", "text": "والاسيكلووير"},
                    {"id": "avs-item-2", "text": "والگانسیکلوویر"},
                    {"id": "avs-item-3", "text": "اوسلتا میویر"}
                ],
                "categories": [
                    {"id": "avs-cat-1", "text": "Influenza"},
                    {"id": "avs-cat-2", "text": "HSV / VZV"},
                    {"id": "avs-cat-3", "text": "EBV / CMV / VZV"}
                ],
                "solution": {
                    "avs-item-3": "avs-cat-1",
                    "avs-item-1": "avs-cat-2",
                    "avs-item-2": "avs-cat-3"
                },
                "points_per_correct": 3
            },
            {
                "id": "fluconazole_properties",
                "type": "true-false",
                "title": "ویژگی‌های فلوکونازول",
                "instruction": "گزینه های درست و نادرست را در مورد فلوکونازول مشخص کنید.",
                "statements": [
                    {"id": "tf-2-1", "text": "جذب خوراکی کمی دارد.", "solution": False},
                    {"id": "tf-2-2", "text": "جذب خوراکی آن تحت تأثیر pH معده و غذا است.", "solution": False},
                    {"id": "tf-2-3", "text": "نفوذ مناسبی به CNS دارد.", "solution": True},
                    {"id": "tf-2-4", "text": "باید به صورت منقسم استفاده شود.", "solution": False},
                    {"id": "tf-2-5", "text": "دفع کبدی دارد و نیازی به تعدیل دوز دارو در نارسایی کلیوی نیست.", "solution": False}
                ],
                "points_per_correct": 2
            },
            {
                "id": "vori_posa_properties",
                "type": "drag-drop-match",
                "title": "ویژگی‌های وریکونازول و پوساکونازول",
                "instruction": "ویژگیهای مربوط به هر داروی ضد قارچ را به آن وصل کنید.",
                "items": [
                    {"id": "vp-item-1", "text": "غذای چرب باعث کاهش جذب آن میشود."},
                    {"id": "vp-item-2", "text": "جذب قرص خوراکی آن بسیار بیشتر از شکل سوسپانسیون است."},
                    {"id": "vp-item-3", "text": "نفوذ مناسبی به CSF دارد."},
                    {"id": "vp-item-4", "text": "سطح سرمی آن اندازه گیری میشود و با بروز عوارض جانبی دارو مرتبط است."},
                    {"id": "vp-item-5", "text": "داروی انتخابی عفونت موکور مایکوزیس است."}
                ],
                "categories": [
                    {"id": "vp-cat-1", "text": "وریکونازول"},
                    {"id": "vp-cat-2", "text": "پوساکونازول"}
                ],
                "solution": {
                    "vp-item-1": "vp-cat-1",
                    "vp-item-3": "vp-cat-1",
                    "vp-item-4": "vp-cat-1",
                    "vp-item-2": "vp-cat-2",
                    "vp-item-5": "vp-cat-2"
                },
                "points_per_correct": 2
            },
            {
                "id": "azole_side_effects",
                "type": "drag-drop-match",
                "title": "عوارض جانبی آزول‌ها",
                "instruction": "هر عارضه جانبی را به داروی ضد قارچ مربوطه وصل کنید.",
                "items": [
                    {"id": "ase-item-1", "text": "تغییرات بینایی"},
                    {"id": "ase-item-2", "text": "ادم محیطی"},
                    {"id": "ase-item-3", "text": "ترک لب"},
                    {"id": "ase-item-4", "text": "حساسیت به نور"},
                    {"id": "ase-item-5", "text": "هیپوکالمی"},
                    {"id": "ase-item-6", "text": "عوارض گوارشی زیاد"}
                ],
                "categories": [
                    {"id": "ase-cat-1", "text": "فلوکونازول"},
                    {"id": "ase-cat-2", "text": "ایتراکونازول"},
                    {"id": "ase-cat-3", "text": "کتوکونازول"},
                    {"id": "ase-cat-4", "text": "وریکونازول"}
                ],
                "solution": {
                    "ase-item-2": "ase-cat-2",
                    "ase-item-6": "ase-cat-3",
                    "ase-item-1": "ase-cat-4",
                    "ase-item-3": "ase-cat-4",
                    "ase-item-4": "ase-cat-4",
                    "ase-item-5": "ase-cat-4"
                },
                "points_per_correct": 1
            },
            {
                "id": "amphotericin_formulations",
                "type": "drag-drop-match",
                "title": "فرمولاسیون‌های آمفوتریسین بی",
                "instruction": "هر ویژگی را به فرمولاسیون درست خود وصل کنید.",
                "items": [
                    {"id": "am-item-1", "text": "دوز روزانه بین ۰/۵ تا ۱/۵ میلی گرم بر کیلوگرم"},
                    {"id": "am-item-2", "text": "نیاز به تست دوز ۱ میلی گرم قبل از اولین تزریق"},
                    {"id": "am-item-3", "text": "عوارض کلیوی کمتر"},
                    {"id": "am-item-4", "text": "قیمت بیشتر"},
                    {"id": "am-item-5", "text": "دوز روزانه ۳ تا ۵ میلیگرم بر کی..."}
                ],
                "categories": [
                    {"id": "am-cat-1", "text": "conventional فرم"},
                    {"id": "am-cat-2", "text": "فرم لیپوزومال"}
                ],
                "solution": {
                    "am-item-1": "am-cat-1",
                    "am-item-2": "am-cat-1",
                    "am-item-3": "am-cat-2",
                    "am-item-4": "am-cat-2",
                    "am-item-5": "am-cat-2"
                },
                "points_per_correct": 2
            }
        ]
    }
}