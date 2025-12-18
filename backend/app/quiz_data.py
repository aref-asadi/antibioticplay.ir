QUIZZES = {
    # ====================================================================
    # UNIT 1: Classification & Structure (مبانی و ساختار)
    # ====================================================================
    
    # --- Level 1: پنی‌سیلین‌ها ---
    "class_1_penicillins": {
        "id": "class_1_penicillins",
        "title": "پنی‌سیلین‌ها",
        "icon": "capsules",
        "description": "دسته‌بندی خانواده پنی‌سیلین بر اساس طیف اثر",
        "questions": [
            {
                "id": "q_pen_class_1",
                "type": "drag-drop-match",
                "title": "دسته‌بندی پنی‌سیلین‌ها",
                "instruction": "هر دارو را در گروه صحیح قرار دهید.",
                "hint": "پنی‌سیلین‌های G و V طبیعی هستند. کلوگزاسیلین ضد استاف است.",
                "items": [
                    {"id": "p1", "text": "پنی سیلین جی"},
                    {"id": "p2", "text": "پنی سیلین وی"},
                    {"id": "p3", "text": "آمپی سیلین"},
                    {"id": "p4", "text": "آموکسی سیلین"},
                    {"id": "p5", "text": "کلوگزاسیلین"},
                    {"id": "p6", "text": "نفی سیلین"},
                    {"id": "p7", "text": "پیپراسیلین"},
                    {"id": "p8", "text": "پنی سیلین بنزاتین"}
                ],
                "categories": [
                    {"id": "c1", "text": "طبیعی (Natural)"},
                    {"id": "c2", "text": "آمینوپنی‌سیلین (وسیع‌الطیف)"},
                    {"id": "c3", "text": "ضد استافیلوکوک"},
                    {"id": "c4", "text": "ضد سودومونا"}
                ],
                "solution": {
                    "p1": "c1", "p2": "c1", "p8": "c1",
                    "p3": "c2", "p4": "c2",
                    "p5": "c3", "p6": "c3",
                    "p7": "c4"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_pd_chart_label",
                "type": "image-labeling",
                # تغییر title و instruction به text (چون کامپوننت question.text را نمایش می‌دهد)
                "text": "پارامترهای فارماکودینامیک را در جای صحیح روی نمودار قرار دهید.",
                
                # تغییر question_image به image
                "image": "/images/questions/pkpd_chart.png", 
                
                "points_per_correct": 20,
                
                # تغییر drop_zones به zones و تبدیل مختصات به x, y (به صورت عدد بدون %)
                "zones": [
                    # left -> x, top -> y (اعداد باید درصد باشند اما بدون علامت %)
                    {"id": "z_conc", "y": 10, "x": 60, "width": 35, "height": 15}, # بالا
                    {"id": "z_auc",  "y": 40, "x": 60, "width": 35, "height": 15}, # وسط
                    {"id": "z_time", "y": 75, "x": 60, "width": 35, "height": 15}  # پایین
                ],
                
                "options": [
                    {"id": "o1", "text": "وابسته به غلظت (آمینوگلیکوزید)"},
                    {"id": "o2", "text": "وابسته به AUC (ونکومایسین)"},
                    {"id": "o3", "text": "وابسته به زمان (بتا-لاکتام)"}
                ],
                
                # سولوشن باید به صورت لیست باشد (چون سیستم جدید چند‌انتخابی است)
                "solution": {
                    "z_conc": ["o1"],
                    "z_auc":  ["o2"],
                    "z_time": ["o3"]
                }
            },
            {
                "id": "q3_pkpd_chart",
                "type": "image-labeling",
                "text": "هر آنتی‌بیوتیک را بر اساس رفتار فارماکودینامیک، در جایگاه صحیح نمودار قرار دهید.",
                "image": "/images/questions/pkpd_chart.png",
                "points_per_correct": 10,
                
                # گزینه‌های سمت راست (داروها)
                "options": [
                    {"id": "amikacin", "text": "Amikacin"},
                    {"id": "gentamicin", "text": "Gentamicin"},
                    {"id": "meropenem", "text": "Meropenem"},
                    {"id": "pip_tazo", "text": "Pip/Tazo"},
                    {"id": "vancomycin", "text": "Vancomycin"}
                ],
                
                # نواحی پاسخ روی نمودار (مختصات باید بر اساس عکس شما تنظیم دقیق شود)
                # فرض: عرض عکس 100% و ارتفاع 100% است.
                "zones": [
                    # ناحیه ۱: بالا (Concentration Dependent) -> برای آمینوگلیکوزیدها
                    {"id": "z_conc", "x": 65, "y": 10, "width": 30, "height": 25},
                    
                    # ناحیه ۲: وسط (AUC/MIC) -> برای ونکومایسین
                    {"id": "z_auc", "x": 65, "y": 40, "width": 30, "height": 25},
                    
                    # ناحیه ۳: پایین (Time Dependent) -> برای بتالاکتام‌ها
                    {"id": "z_time", "x": 65, "y": 70, "width": 30, "height": 25}
                ],
                
                # پاسخ صحیح (چند گزینه برای هر ناحیه)
                "solution": {
                    "z_conc": ["amikacin", "gentamicin"],
                    "z_auc": ["vancomycin"],
                    "z_time": ["meropenem", "pip_tazo"]
                }
            }
        ]
    },

    # --- Level 2: سفالوسپورین‌ها (نسل ۱ تا ۳) ---
    "class_2_ceph_basic": {
        "id": "class_2_ceph_basic",
        "title": "سفالوسپورین‌ها (۱)",
        "icon": "tablets",
        "description": "شناسایی نسل‌های اول، دوم و سوم سفالوسپورین‌ها",
        "questions": [
            {
                "id": "q_ceph_123",
                "type": "drag-drop-match",
                "title": "نسل‌های ۱ تا ۳",
                "instruction": "داروها را به نسل صحیح متصل کنید.",
                "hint": "سفازولین نسل ۱ است. سفتریاکسون معروف‌ترین نسل ۳ است.",
                "items": [
                    {"id": "c1", "text": "سفازولین"},
                    {"id": "c2", "text": "سفالکسین"},
                    {"id": "c3", "text": "سفوروکسیم"},
                    {"id": "c4", "text": "سفوکسیتین"},
                    {"id": "c5", "text": "سفتریاکسون"},
                    {"id": "c6", "text": "سفیکسیم"},
                    {"id": "c7", "text": "سفتازیدیم"}
                ],
                "categories": [
                    {"id": "g1", "text": "نسل اول"},
                    {"id": "g2", "text": "نسل دوم"},
                    {"id": "g3", "text": "نسل سوم"}
                ],
                "solution": {
                    "c1": "g1", "c2": "g1",
                    "c3": "g2", "c4": "g2",
                    "c5": "g3", "c6": "g3", "c7": "g3"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 3: سفالوسپورین‌های پیشرفته (نسل ۴ و ۵) ---
    "class_3_ceph_adv": {
        "id": "class_3_ceph_adv",
        "title": "سفالوسپورین‌ها (۲)",
        "icon": "shield-virus",
        "description": "نسل‌های پیشرفته سفالوسپورین‌ها",
        "questions": [
            {
                "id": "q_ceph_45",
                "type": "drag-drop-match",
                "title": "نسل‌های پیشرفته",
                "instruction": "داروهای نسل جدید را دسته‌بندی کنید.",
                "items": [
                    {"id": "c8", "text": "سفپیم"},
                    {"id": "c9", "text": "سفتارولین"},
                    {"id": "c10", "text": "سفپیریم"}
                ],
                "categories": [
                    {"id": "g4", "text": "نسل چهارم"},
                    {"id": "g5", "text": "نسل پنجم (ضد MRSA)"}
                ],
                "solution": {
                    "c8": "g4", "c10": "g4",
                    "c9": "g5"
                },
                "points_per_correct": 15
            }
        ]
    },

    # --- Level 4: سایر بتا-لاکتام‌ها و دیواره سلولی ---
    "class_4_cellwall_others": {
        "id": "class_4_cellwall_others",
        "title": "سایر مهارکنندگان دیواره",
        "icon": "wall", # آیکون فرضی
        "description": "کارباپنم‌ها، مونوباکتام‌ها و گلیکوپپتیدها",
        "questions": [
            {
                "id": "q_carb_glyco",
                "type": "drag-drop-match",
                "title": "خانواده‌های دیگر",
                "instruction": "هر آنتی‌بیوتیک متعلق به کدام خانواده است؟",
                "items": [
                    {"id": "o1", "text": "مروپنم"},
                    {"id": "o2", "text": "ایمی پنم"},
                    {"id": "o3", "text": "آزترئونام"},
                    {"id": "o4", "text": "ونکومایسین"},
                    {"id": "o5", "text": "تیکوپلانین"},
                    {"id": "o6", "text": "باستیرایسین"}
                ],
                "categories": [
                    {"id": "cat1", "text": "کارباپنم‌ها"},
                    {"id": "cat2", "text": "مونوباکتام‌ها"},
                    {"id": "cat3", "text": "گلیکوپپتیدها"},
                    {"id": "cat4", "text": "پلی‌پپتیدها"}
                ],
                "solution": {
                    "o1": "cat1", "o2": "cat1",
                    "o3": "cat2",
                    "o4": "cat3", "o5": "cat3",
                    "o6": "cat4"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 5: مهارکنندگان پروتئین (30S و 50S) ---
    "class_5_protein": {
        "id": "class_5_protein",
        "title": "مهارکنندگان پروتئین",
        "icon": "dna",
        "description": "آمینوگلیکوزیدها، تتراسیکلین‌ها و ماکرولیدها",
        "questions": [
            {
                "id": "q_protein_syn",
                "type": "drag-drop-match",
                "title": "دسته‌بندی مهارکنندگان پروتئین",
                "instruction": "داروها را در خانواده صحیح قرار دهید.",
                "items": [
                    {"id": "pr1", "text": "جنتامایسین"},
                    {"id": "pr2", "text": "آمیکاسین"},
                    {"id": "pr3", "text": "داکسی سیکلین"},
                    {"id": "pr4", "text": "تتراسیکلین"},
                    {"id": "pr5", "text": "آزیترومایسین"},
                    {"id": "pr6", "text": "کلیندامایسین"},
                    {"id": "pr7", "text": "لینزولید"}
                ],
                "categories": [
                    {"id": "pc1", "text": "آمینوگلیکوزید"},
                    {"id": "pc2", "text": "تتراسیکلین"},
                    {"id": "pc3", "text": "ماکرولید/لینکوزامید"},
                    {"id": "pc4", "text": "اکسازولیدینون"}
                ],
                "solution": {
                    "pr1": "pc1", "pr2": "pc1",
                    "pr3": "pc2", "pr4": "pc2",
                    "pr5": "pc3", "pr6": "pc3",
                    "pr7": "pc4"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 6: مهارکنندگان DNA و فولات ---
    "class_6_dna": {
        "id": "class_6_dna",
        "title": "مهارکنندگان DNA و فولات",
        "icon": "bacteria",
        "description": "فلوروکینولون‌ها و آنتی‌متابولیت‌ها",
        "questions": [
            {
                "id": "q_dna_folate",
                "type": "drag-drop-match",
                "title": "هدف آنتی‌بیوتیک",
                "instruction": "مکانیسم اثر یا خانواده دارو را مشخص کنید.",
                "items": [
                    {"id": "d1", "text": "سیپروفلوکساسین"},
                    {"id": "d2", "text": "لووفلوکساسین"},
                    {"id": "d3", "text": "کوتریموکسازول"},
                    {"id": "d4", "text": "مترونیدازول"},
                    {"id": "d5", "text": "ریفامپین"}
                ],
                "categories": [
                    {"id": "dc1", "text": "فلوروکینولون (DNA Gyrase)"},
                    {"id": "dc2", "text": "آنتی‌متابولیت (فولات)"},
                    {"id": "dc3", "text": "آسیب مستقیم DNA"},
                    {"id": "dc4", "text": "مهار RNA پلیمراز"}
                ],
                "solution": {
                    "d1": "dc1", "d2": "dc1",
                    "d3": "dc2",
                    "d4": "dc3",
                    "d5": "dc4"
                },
                "points_per_correct": 10
            }
        ]
    },

    # ====================================================================
    # UNIT 2: Dosage Forms (اشکال دارویی)
    # ====================================================================

    # --- Level 1: بتا-لاکتام‌ها و مهارکننده‌ها ---
    "dosage_1_betalactams": {
        "id": "dosage_1_betalactams",
        "title": "بتا-لاکتام‌ها و مهارکننده‌ها",
        "icon": "vials",
        "description": "ترکیبات آنتی‌بیوتیک با مهارکننده‌های بتالاکتاماز و نسبت‌های آن‌ها",
        "questions": [
            {
                "id": "q_inhibitors_match",
                "type": "drag-drop-match",
                "title": "ترکیب با مهارکننده",
                "instruction": "هر آنتی‌بیوتیک را به مهارکننده بتالاکتاماز مخصوص آن وصل کنید.",
                "items": [
                    {"id": "i1", "text": "آموکسی سیلین"},
                    {"id": "i2", "text": "آمپی سیلین"},
                    {"id": "i3", "text": "پیپراسیلین"},
                    {"id": "i4", "text": "سفتازیدیم"}
                ],
                "categories": [
                    {"id": "c1", "text": "کلاوولانات"},
                    {"id": "c2", "text": "سولباکتام"},
                    {"id": "c3", "text": "تازوباکتام"},
                    {"id": "c4", "text": "آویباکتام"}
                ],
                "solution": {
                    "i1": "c1",
                    "i2": "c2",
                    "i3": "c3",
                    "i4": "c4"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_coamox_ratios",
                "type": "drag-drop-match",
                "title": "نسبت‌های کوآموکسی‌کلاو",
                "instruction": "هر دوز سوسپانسیون را به نسبت صحیح آموکسی‌سیلین به کلاوولانات وصل کنید.",
                "hint": "دوز ۶۴۳ بالاترین نسبت (۱:۱۴) را دارد.",
                "items": [
                    {"id": "r1", "text": "سوسپانسیون ۱۵۶ و ۳۱۲"},
                    {"id": "r2", "text": "سوسپانسیون ۲۲۸ و ۴۵۷"},
                    {"id": "r3", "text": "سوسپانسیون ۶۴۳"}
                ],
                "categories": [
                    {"id": "rc1", "text": "نسبت ۱:۴"},
                    {"id": "rc2", "text": "نسبت ۱:۷"},
                    {"id": "rc3", "text": "نسبت ۱:۱۴"}
                ],
                "solution": {
                    "r1": "rc1",
                    "r2": "rc2",
                    "r3": "rc3"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 2: محاسبات دوزینگ (Dosing) ---
    "dosage_2_dosing": {
        "id": "dosage_2_dosing",
        "title": "محاسبات دوزینگ",
        "icon": "calculator",
        "description": "دوزینگ داروهای ترکیبی و نکات مهم تجویز",
        "questions": [
            {
                "id": "q_amp_sul_fill",
                "type": "drag-drop-fill",
                "title": "آمپی‌سیلین-سولباکتام",
                "instruction_template": "این دارو با نسبت _BLANK1_ فرموله شده است. اشکال دارویی _BLANK2_ و _BLANK3_ دارد و دوزینگ بر اساس _BLANK4_ انجام می‌شود.",
                "options": [
                    {"id": "o1", "text": "۲:۱"},
                    {"id": "o2", "text": "۱/۵ گرم"},
                    {"id": "o3", "text": "۳ گرم"},
                    {"id": "o4", "text": "مجموع (کل دارو)"},
                    {"id": "o5", "text": "۴:۱"},
                    {"id": "o6", "text": "فقط آمپی‌سیلین"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "o1"},
                    {"id": "_BLANK2_", "solution_id": "o2"},
                    {"id": "_BLANK3_", "solution_id": "o3"},
                    {"id": "_BLANK4_", "solution_id": "o4"}
                ],
                "points_per_correct": 15
            },
            {
                "id": "q_pip_taz_fill",
                "type": "drag-drop-fill",
                "title": "پیپراسیلین-تازوباکتام",
                "instruction_template": "این دارو با نسبت _BLANK1_ فرموله شده است. اشکال دارویی رایج شامل _BLANK2_ و _BLANK3_ است.",
                "options": [
                    {"id": "p1", "text": "۸:۱"},
                    {"id": "p2", "text": "۲/۲۵۰ گرم"},
                    {"id": "p3", "text": "۴/۵ گرم"},
                    {"id": "p4", "text": "۴:۱"},
                    {"id": "p5", "text": "۳ گرم"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "p1"},
                    {"id": "_BLANK2_", "solution_id": "p2"},
                    {"id": "_BLANK3_", "solution_id": "p3"}
                ],
                "points_per_correct": 15
            },
            {
                "id": "q_imipenem_select",
                "type": "multiple-select",
                "title": "انتخاب دوز ایمی‌پنم",
                "instruction": "برای تجویز دوز ۵۰۰ میلی‌گرم ایمی‌پنم-سیلاستاتین، کدام گزینه‌ها صحیح هستند؟ (ویال‌ها به صورت مجموع نوشته می‌شوند)",
                "options": [
                    "یک ویال ۵۰۰/۵۰۰ (مجموع ۱ گرم)",
                    "دو ویال ۲۵۰/۲۵۰ (مجموع ۵۰۰ میلی‌گرم)",
                    "نصف ویال ۵۰۰/۵۰۰",
                    "یک ویال ۲۵۰/۲۵۰"
                ],
                "solution": [
                    "یک ویال ۵۰۰/۵۰۰ (مجموع ۱ گرم)",
                    "دو ویال ۲۵۰/۲۵۰ (مجموع ۵۰۰ میلی‌گرم)"
                ],
                "explanation": "دوز ۵۰۰ میلی‌گرم یعنی ۵۰۰ میلی‌گرم از جزء ایمی‌پنم. ویال ۵۰۰/۵۰۰ حاوی ۵۰۰ ایمی‌پنم است. دو ویال ۲۵۰/۲۵۰ نیز حاوی ۵۰۰ ایمی‌پنم هستند.",
                "points_per_correct": 20
            }
        ]
    },

    # --- Level 3: اشکال دارویی آنتی‌بیوتیک‌ها ---
    "dosage_3_abx_forms": {
        "id": "dosage_3_abx_forms",
        "title": "اشکال دارویی آنتی‌بیوتیک‌ها",
        "icon": "eye-dropper",
        "description": "قطره‌های چشمی، سوسپانسیون‌ها و فرمولاسیون‌های خاص",
        "questions": [
            {
                "id": "q_quinolone_eyes",
                "type": "multiple-select",
                "title": "قطره‌های چشمی کینولون",
                "instruction": "کدام یک از داروهای زیر شکل دارویی قطره چشمی دارند؟",
                "options": [
                    "سیپروفلوکساسین",
                    "لووفلوکساسین",
                    "موکسی فلوکساسین",
                    "جمی فلوکساسین"
                ],
                "solution": [
                    "سیپروفلوکساسین",
                    "لووفلوکساسین",
                    "موکسی فلوکساسین"
                ],
                "points_per_correct": 10
            },
            {
                "id": "q_macrolide_forms",
                "type": "drag-drop-match",
                "title": "اشکال ماکرولیدها",
                "instruction": "اشکال دارویی را به داروی مربوطه وصل کنید.",
                "items": [
                    {"id": "m1", "text": "سوسپانسیون ۲۵۰ و ۱۲۵"},
                    {"id": "m2", "text": "سوسپانسیون ER دو گرمی"},
                    {"id": "m3", "text": "قطره چشمی ۱٪"},
                    {"id": "m4", "text": "ویال تزریقی ۵۰۰"},
                    {"id": "m5", "text": "محلول موضعی ۴٪"},
                    {"id": "m6", "text": "پماد چشمی و ژل ۲٪"}
                ],
                "categories": [
                    {"id": "azi", "text": "آزیترومایسین"},
                    {"id": "ery", "text": "اریترومایسین"}
                ],
                "solution": {
                    "m1": "azi", "m2": "azi", "m3": "azi", "m4": "azi",
                    "m5": "ery", "m6": "ery"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_nitro_forms",
                "type": "drag-drop-match",
                "title": "فرمولاسیون نیتروفورانتوئین",
                "instruction": "ویژگی را به فرمولاسیون صحیح وصل کنید.",
                "items": [
                    {"id": "n1", "text": "دوزینگ ۴ بار در روز"},
                    {"id": "n2", "text": "دوزینگ ۲ بار در روز"},
                    {"id": "n3", "text": "تشکیل ژل و عوارض گوارشی کمتر"}
                ],
                "categories": [
                    {"id": "macro", "text": "ماکروکریستال"},
                    {"id": "mono", "text": "مونوهیدرات ماکروکریستال"}
                ],
                "solution": {
                    "n1": "macro",
                    "n2": "mono",
                    "n3": "mono"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 4: ضد ویروس و ضد قارچ ---
    "dosage_4_av_af": {
        "id": "dosage_4_av_af",
        "title": "ضد ویروس و ضد قارچ",
        "icon": "fungus",
        "description": "اشکال دارویی داروهای ضد ویروس و ضد قارچ",
        "questions": [
            {
                "id": "q_antiviral_feat",
                "type": "drag-drop-match",
                "title": "ویژگی آنتی‌ویروس‌ها",
                "instruction": "هر ویژگی مربوط به کدام دارو است؟",
                "items": [
                    {"id": "av1", "text": "کرم موضعی ۵٪ و پماد چشمی"},
                    {"id": "av2", "text": "قرص ۵۰۰ و ۱۰۰۰ میلی‌گرم"},
                    {"id": "av3", "text": "نیاز به دستکش هنگام آماده‌سازی"},
                    {"id": "av4", "text": "پیش‌داروی خوراکی ضد CMV"}
                ],
                "categories": [
                    {"id": "c1", "text": "آسیکلوویر"},
                    {"id": "c2", "text": "والاسیکلوویر"},
                    {"id": "c3", "text": "گانسیکلوویر"},
                    {"id": "c4", "text": "والگانسیکلوویر"}
                ],
                "solution": {
                    "av1": "c1",
                    "av2": "c2",
                    "av3": "c3",
                    "av4": "c4"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_azole_forms_match",
                "type": "drag-drop-match",
                "title": "اشکال دارویی آزول‌ها",
                "instruction": "شکل دارویی را به داروی آزول وصل کنید.",
                "items": [
                    {"id": "az1", "text": "شامپو ۲٪"},
                    {"id": "az2", "text": "کپسول ۱۵۰ میلی‌گرم"},
                    {"id": "az3", "text": "قرص ۵۰ و ۲۰۰ میلی‌گرم"},
                    {"id": "az4", "text": "آمپول ۳۰۰ میلی‌گرم"},
                    {"id": "az5", "text": "کپسول ۱۰۰ میلی‌گرم"}
                ],
                "categories": [
                    {"id": "keto", "text": "کتوکونازول"},
                    {"id": "fluco", "text": "فلوکونازول"},
                    {"id": "vori", "text": "وریکونازول"},
                    {"id": "posa", "text": "پوساکونازول"},
                    {"id": "itra", "text": "ایتراکونازول"}
                ],
                "solution": {
                    "az1": "keto",
                    "az2": "fluco",
                    "az3": "vori",
                    "az4": "posa",
                    "az5": "itra"
                },
                "points_per_correct": 10
            }
        ]
    },
    
    # ====================================================================
    # UNIT 3: Clinical Application - Basics (کاربردهای بالینی ۱)
    # ====================================================================

    # --- Level 1: طیف اثر و پوشش میکروبی ---
    "clinical_1_coverage": {
        "id": "clinical_1_coverage",
        "title": "پوشش میکروبی",
        "icon": "microscope",
        "description": "شناخت پوشش بی‌هوازی و فلوروکینولون‌های تنفسی",
        "questions": [
            {
                "id": "q_anaerobic_cov",
                "type": "drag-drop-match",
                "title": "پوشش بی‌هوازی",
                "instruction": "آنتی‌بیوتیک‌ها را بر اساس داشتن یا نداشتن پوشش روی باکتری‌های بی‌هوازی دسته‌بندی کنید.",
                "hint": "کلیندامایسین و مترونیدازول پوشش عالی دارند. سفالوسپورین‌ها (مثل سفتازیدیم) معمولاً ندارند.",
                "items": [
                    {"id": "a1", "text": "کلیندامایسین"},
                    {"id": "a2", "text": "مترونیدازول"},
                    {"id": "a3", "text": "پیپراسیلین-تازوباکتام"},
                    {"id": "a4", "text": "مروپنم"},
                    {"id": "a5", "text": "سفتازیدیم"},
                    {"id": "a6", "text": "سیپروفلوکساسین"},
                    {"id": "a7", "text": "موکسی فلوکساسین"}
                ],
                "categories": [
                    {"id": "yes", "text": "دارای پوشش بی‌هوازی"},
                    {"id": "no", "text": "فاقد پوشش بی‌هوازی"}
                ],
                "solution": {
                    "a1": "yes", "a2": "yes", "a3": "yes", "a4": "yes", "a7": "yes",
                    "a5": "no", "a6": "no"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_resp_fq_match",
                "type": "drag-drop-match",
                "title": "فلوروکینولون‌های تنفسی",
                "instruction": "کینولون‌های تنفسی (مؤثر بر پنوموکوک) را جدا کنید.",
                "hint": "سیپروفلوکساسین تنفسی نیست. داروهای جدیدتر (لوو، موکسی، جمی) تنفسی هستند.",
                "items": [
                    {"id": "f1", "text": "لووفلوکساسین"},
                    {"id": "f2", "text": "موکسی فلوکساسین"},
                    {"id": "f3", "text": "جمی فلوکساسین"},
                    {"id": "f4", "text": "سیپروفلوکساسین"},
                    {"id": "f5", "text": "افلوکساسین"},
                    {"id": "f6", "text": "نالیدیکسیک اسید"}
                ],
                "categories": [
                    {"id": "resp", "text": "تنفسی (Respiratory)"},
                    {"id": "non", "text": "غیر تنفسی"}
                ],
                "solution": {
                    "f1": "resp", "f2": "resp", "f3": "resp",
                    "f4": "non", "f5": "non", "f6": "non"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 2: نکات ایمنی در تجویز ---
    "clinical_2_admin": {
        "id": "clinical_2_admin",
        "title": "نکات ایمنی تجویز",
        "icon": "syringe",
        "description": "تست پنی‌سیلین، تزریق وریدی/عضلانی و تداخلات کلسیم",
        "questions": [
            {
                "id": "q_pen_skin_test",
                "type": "drag-drop-match",
                "title": "قطع دارو قبل از تست پوستی",
                "instruction": "کدام داروها باید قبل از تست پوستی پنی‌سیلین قطع شوند؟",
                "hint": "آنتی‌هیستامین‌ها (دیفن‌هیدرامین و...) نتیجه را منفی کاذب می‌کنند. کورتون‌ها و مونتلوکاست تداخلی ندارند.",
                "items": [
                    {"id": "d1", "text": "دیفن هیدرامین"},
                    {"id": "d2", "text": "پرومتازین"},
                    {"id": "d3", "text": "اسپری آزلاستین"},
                    {"id": "d4", "text": "مونتلوکاست"},
                    {"id": "d5", "text": "پردنیزولون"},
                    {"id": "d6", "text": "فاموتیدین"}
                ],
                "categories": [
                    {"id": "stop", "text": "باید قطع شود"},
                    {"id": "cont", "text": "نیازی به قطع نیست"}
                ],
                "solution": {
                    "d1": "stop", "d2": "stop", "d3": "stop",
                    "d4": "cont", "d5": "cont", "d6": "cont"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_iv_im_pen",
                "type": "drag-drop-match",
                "title": "تزریق وریدی vs عضلانی",
                "instruction": "پنی‌سیلین‌ها را بر اساس روش تزریق مجاز دسته‌بندی کنید.",
                "hint": "فرمولاسیون‌های شیری‌رنگ (بنزاتین، پروکائین) هرگز نباید وریدی تزریق شوند (خطر مرگ).",
                "items": [
                    {"id": "p1", "text": "پنی‌سیلین G سدیم"},
                    {"id": "p2", "text": "پنی‌سیلین G پتاسیم"},
                    {"id": "p3", "text": "پنی‌سیلین G بنزاتین"},
                    {"id": "p4", "text": "پنی‌سیلین ۶.۳.۳"},
                    {"id": "p5", "text": "پنی‌سیلین G پروکائین"}
                ],
                "categories": [
                    {"id": "iv", "text": "مجاز به تزریق وریدی (IV)"},
                    {"id": "im", "text": "فقط عضلانی (IM Only)"}
                ],
                "solution": {
                    "p1": "iv", "p2": "iv",
                    "p3": "im", "p4": "im", "p5": "im"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_ceftriaxone_ca",
                "type": "drag-drop-match",
                "title": "سفتریاکسون و کلسیم",
                "instruction": "قوانین تزریق همزمان سفتریاکسون و کلسیم را برای سنین مختلف مشخص کنید.",
                "hint": "در نوزادان زیر ۲۸ روز، خطر رسوب در ریه و کلیه وجود دارد و کاملاً ممنوع است.",
                "items": [
                    {"id": "age1", "text": "نوزادان زیر ۲۸ روز"},
                    {"id": "age2", "text": "کودکان و بزرگسالان"},
                    {"id": "age3", "text": "نوزادان نارس (Premature)"}
                ],
                "categories": [
                    {"id": "ban", "text": "ممنوع (حتی از لاین جدا)"},
                    {"id": "ok", "text": "مجاز (با شستشوی لاین)"}
                ],
                "solution": {
                    "age1": "ban", "age3": "ban",
                    "age2": "ok"
                },
                "points_per_correct": 20
            }
        ]
    },

    # --- Level 3: ریسک‌ها و هشدارهای مهم ---
    "clinical_3_risks": {
        "id": "clinical_3_risks",
        "title": "هشدارهای مهم (Red Flag)",
        "icon": "radiation",
        "description": "عفونت C.difficile، میاستنی گراویس و سندروم مرد قرمز",
        "questions": [
            {
                "id": "q_cdiff_risk",
                "type": "multiple-select",
                "title": "ریسک عفونت C.difficile",
                "instruction": "کدام ۴ دسته دارویی بیشترین ریسک ایجاد کولیت غشای کاذب (C.diff) را دارند؟",
                "explanation": "کلیندامایسین (کلاسیک)، سفالوسپورین‌های نسل ۳ و ۴، فلوروکینولون‌ها و آمپی‌سیلین/آموکسی‌سیلین پرخطرترین‌ها هستند.",
                "options": [
                    "کلیندامایسین",
                    "سفالوسپورین‌ها",
                    "فلوروکینولون‌ها",
                    "آمپی‌سیلین/آموکسی‌سیلین",
                    "آمینوگلیکوزیدها",
                    "تتراسیکلین‌ها",
                    "ونکومایسین"
                ],
                "solution": [
                    "کلیندامایسین",
                    "سفالوسپورین‌ها",
                    "فلوروکینولون‌ها",
                    "آمپی‌سیلین/آموکسی‌سیلین"
                ],
                "points_per_correct": 15
            },
            {
                "id": "q_myasthenia",
                "type": "multiple-select",
                "title": "منع مصرف در میاستنی گراویس",
                "instruction": "کدام داروها می‌توانند باعث ضعف عضلانی شدید در بیماران میاستنی گراویس شوند؟",
                "hint": "داروهایی که اثر بلاک عصبی-عضلانی دارند.",
                "options": [
                    "آمیکاسین (آمینوگلیکوزید)",
                    "سیپروفلوکساسین (کینولون)",
                    "کلیندامایسین",
                    "سفتریاکسون",
                    "نیتروفورانتوئین"
                ],
                "solution": [
                    "آمیکاسین (آمینوگلیکوزید)",
                    "سیپروفلوکساسین (کینولون)",
                    "کلیندامایسین"
                ],
                "points_per_correct": 15
            },
            {
                "id": "q_redman_syndrome",
                "type": "drag-drop-fill",
                "title": "سندروم مرد قرمز",
                "instruction_template": "بیمار حین تزریق _BLANK1_ دچار برافروختگی سر و گردن شده است. نام این عارضه _BLANK2_ است و اقدام صحیح _BLANK3_ می‌باشد.",
                "explanation": "این عارضه حساسیت نیست، بلکه ناشی از آزادسازی هیستامین به دلیل سرعت بالای تزریق ونکومایسین است.",
                "options": [
                    {"id": "o1", "text": "ونکومایسین"},
                    {"id": "o2", "text": "سندروم مرد قرمز (Red Man)"},
                    {"id": "o3", "text": "کاهش سرعت انفوزیون"},
                    {"id": "o4", "text": "مروپنم"},
                    {"id": "o5", "text": "آنافیلاکسی"},
                    {"id": "o6", "text": "قطع کامل دارو و عدم تجویز مجدد"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "o1"},
                    {"id": "_BLANK2_", "solution_id": "o2"},
                    {"id": "_BLANK3_", "solution_id": "o3"}
                ],
                "points_per_correct": 15
            }
        ]
    },

    # ====================================================================
    # UNIT 4: Clinical Application - Advanced (کاربردهای بالینی ۲)
    # ====================================================================

    # --- Level 1: عوارض جانبی اختصاصی ---
    "clinical_4_side_effects": {
        "id": "clinical_4_side_effects",
        "title": "عوارض اختصاصی",
        "icon": "biohazard",
        "description": "عوارض خاص دارویی مثل تندینوپاتی و تداخلات",
        "questions": [
            {
                "id": "q_specific_se",
                "type": "drag-drop-match",
                "title": "عوارض اختصاصی",
                "instruction": "هر عارضه را به داروی مسبب آن وصل کنید.",
                "items": [
                    {"id": "se1", "text": "کاهش سطح سرمی والپروات"},
                    {"id": "se2", "text": "ژنیکوماستی"},
                    {"id": "se3", "text": "هایپوکالمی و هایپومنیزیمی"},
                    {"id": "se4", "text": "اتوتوکسیسیتی و نفروتوکسیسیتی"}
                ],
                "categories": [
                    {"id": "c1", "text": "مروپنم"},
                    {"id": "c2", "text": "کتوکونازول"},
                    {"id": "c3", "text": "آمفوتریسین B"},
                    {"id": "c4", "text": "آمیکاسین"}
                ],
                "solution": {
                    "se1": "c1", "se2": "c2", "se3": "c3", "se4": "c4"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_tendinopathy",
                "type": "drag-drop-fill",
                "title": "تندینوپاتی کینولون‌ها",
                "instruction_template": "عارضه تندینوپاتی با _BLANK1_ شایع‌تر است و معمولاً در _BLANK2_ رخ می‌دهد. ریسک فاکتورهای آن شامل _BLANK3_ و _BLANK4_ است.",
                "options": [
                    {"id": "o1", "text": "سیپروفلوکساسین"},
                    {"id": "o2", "text": "آشیل"},
                    {"id": "o3", "text": "سن بالا"},
                    {"id": "o4", "text": "مصرف کورتون"},
                    {"id": "o5", "text": "مچ دست"},
                    {"id": "o6", "text": "آزیترومایسین"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "o1"},
                    {"id": "_BLANK2_", "solution_id": "o2"},
                    {"id": "_BLANK3_", "solution_id": "o3"},
                    {"id": "_BLANK4_", "solution_id": "o4"}
                ],
                "points_per_correct": 15
            },
            {
                "id": "q_cation_interact",
                "type": "multiple-select",
                "title": "تداخل با کاتیون‌ها",
                "instruction": "کدام داروها با مصرف همزمان لبنیات یا مکمل‌های فلزی (کلسیم، آهن) دچار کاهش جذب شدید می‌شوند؟",
                "options": [
                    "داکسی‌سیکلین", "تتراسیکلین", "سیپروفلوکساسین", "لووفلوکساسین",
                    "آزیترومایسین", "سفیکسیم", "آمپی‌سیلین"
                ],
                "solution": [
                    "داکسی‌سیکلین", "تتراسیکلین", "سیپروفلوکساسین", "لووفلوکساسین"
                ],
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 2: تتراسیکلین‌ها و ضد سل ---
    "clinical_5_tb_tetra": {
        "id": "clinical_5_tb_tetra",
        "title": "تتراسیکلین و سل",
        "icon": "lungs",
        "description": "ویژگی‌های تتراسیکلین‌ها و عوارض داروهای ضد سل",
        "questions": [
            {
                "id": "q_tetra_feat",
                "type": "drag-drop-match",
                "title": "ویژگی تتراسیکلین‌ها",
                "instruction": "ویژگی‌ها را به داروی مربوطه وصل کنید.",
                "items": [
                    {"id": "t1", "text": "مجاز در کودکان < ۸ سال (کوتاه مدت)"},
                    {"id": "t2", "text": "مؤثر بر باکتری‌های مقاوم"},
                    {"id": "t3", "text": "بیشترین ریسک سرگیجه"},
                    {"id": "t4", "text": "بیشترین سمیت نوری"}
                ],
                "categories": [
                    {"id": "c1", "text": "داکسی‌سیکلین"},
                    {"id": "c2", "text": "تیگسیکلین"},
                    {"id": "c3", "text": "مینوسیکلین"},
                    {"id": "c4", "text": "دمکلوسیکلین"}
                ],
                "solution": {
                    "t1": "c1", "t2": "c2", "t3": "c3", "t4": "c4"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_tb_adverse",
                "type": "drag-drop-match",
                "title": "عوارض داروهای سل",
                "instruction": "هر دارو چه عارضه‌ای دارد؟",
                "items": [
                    {"id": "tb1", "text": "ایزونیازید"},
                    {"id": "tb2", "text": "ریفامپین"},
                    {"id": "tb3", "text": "اتامبوتول"},
                    {"id": "tb4", "text": "پیرازینامید"}
                ],
                "categories": [
                    {"id": "e1", "text": "نوروپاتی/کبدی"},
                    {"id": "e2", "text": "ادرار قرمز"},
                    {"id": "e3", "text": "کوررنگی"},
                    {"id": "e4", "text": "نقرس (اسید اوریک)"}
                ],
                "solution": {
                    "tb1": "e1", "tb2": "e2", "tb3": "e3", "tb4": "e4"
                },
                "points_per_correct": 10
            }
        ]
    },

    # --- Level 3: شرایط خاص و مقاومت ---
    "clinical_6_special": {
        "id": "clinical_6_special",
        "title": "شرایط خاص",
        "icon": "baby",
        "description": "بارداری، فیبروز کیستیک و مقاومت آنتی‌بیوتیکی",
        "questions": [
            {
                "id": "q_pregnancy",
                "type": "drag-drop-match",
                "title": "ایمنی در بارداری",
                "instruction": "داروها را بر اساس ایمنی در بارداری دسته‌بندی کنید.",
                "items": [
                    {"id": "p1", "text": "پنی‌سیلین/سفالوسپورین"},
                    {"id": "p2", "text": "کلیندامایسین (تزریقی)"},
                    {"id": "p3", "text": "مترونیدازول (۳ ماهه اول)"},
                    {"id": "p4", "text": "کوتریموکسازول"}
                ],
                "categories": [
                    {"id": "ok", "text": "مجاز"},
                    {"id": "no", "text": "ممنوع/احتیاط"}
                ],
                "solution": {
                    "p1": "ok", "p2": "ok",
                    "p3": "no", "p4": "no"
                },
                "points_per_correct": 10
            },
            {
                "id": "q_cf_order",
                "type": "drag-drop-ordering",
                "title": "ترتیب داروها در CF",
                "instruction": "ترتیب صحیح مصرف داروهای استنشاقی در بیماران سیستیک فیبروزیس را مشخص کنید.",
                "items": [
                    {"id": "s1", "text": "برونکودیلاتور (باز کننده راه هوایی)"},
                    {"id": "s2", "text": "سالین هایپرتونیک (رقیق کننده)"},
                    {"id": "s3", "text": "درناز آلفا (شکننده موکوس)"},
                    {"id": "s4", "text": "توبرامایسین (آنتی‌بیوتیک)"}
                ],
                "solution": ["s1", "s2", "s3", "s4"],
                "points_per_correct": 20
            },
            {
                "id": "q_resistant_bugs",
                "type": "drag-drop-match",
                "title": "درمان باکتری‌های مقاوم",
                "instruction": "داروی مناسب برای هر پاتوژن مقاوم را انتخاب کنید.",
                "items": [
                    {"id": "r1", "text": "استافیلوکوک مقاوم (MRSA)"},
                    {"id": "r2", "text": "سودوموناس مقاوم"}
                ],
                "categories": [
                    {"id": "c1", "text": "ونکومایسین / لینزولید"},
                    {"id": "c2", "text": "کلیستین"}
                ],
                "solution": {
                    "r1": "c1", "r2": "c2"
                },
                "points_per_correct": 10
            }
        ]
    },

    # ====================================================================
    # UNIT 5: Pharmacodynamics (فارماکودینامیک)
    # ====================================================================

    # --- Level 1: مفاهیم PK/PD ---
    "pd_1_concepts": {
        "id": "pd_1_concepts",
        "title": "مفاهیم فارماکودینامیک",
        "icon": "chart-line",
        "description": "شناخت رفتارهای وابسته به غلظت و وابسته به زمان",
        "questions": [
            {
                "id": "q_pd_chart_label",
                "type": "image-labeling",
                "title": "نمودار PK/PD",
                "instruction": "پارامترهای فارماکودینامیک را در جای صحیح روی نمودار قرار دهید.",
                "question_image": "/images/questions/pkpd_chart.png", # عکس باید در پوشه public باشد
                # مختصات حدودی بر اساس نمودار پاورپوینت
                "drop_zones": [
                    {"id": "z_conc", "top": "10%", "left": "60%", "width": "35%", "height": "15%"}, # بالا: Concentration
                    {"id": "z_auc", "top": "40%", "left": "60%", "width": "35%", "height": "15%"},  # وسط: AUC
                    {"id": "z_time", "top": "75%", "left": "60%", "width": "35%", "height": "15%"}  # پایین: Time
                ],
                "options": [
                    {"id": "o1", "text": "وابسته به غلظت (آمینوگلیکوزید)"},
                    {"id": "o2", "text": "وابسته به AUC (ونکومایسین)"},
                    {"id": "o3", "text": "وابسته به زمان (بتا-لاکتام)"}
                ],
                "solution": {
                    "z_conc": "o1",
                    "z_auc": "o2",
                    "z_time": "o3"
                },
                "points_per_correct": 20
            },
            {
                "id": "q_pd_definitions",
                "type": "drag-drop-fill",
                "title": "تعاریف PD",
                "instruction_template": "داروهای Concentration dependent مثل _BLANK1_ وابسته به _BLANK2_ هستند. داروهای Time dependent مثل _BLANK3_ باید _BLANK4_ مصرف شوند.",
                "options": [
                    {"id": "op1", "text": "آمیکاسین"},
                    {"id": "op2", "text": "Cmax / MIC"},
                    {"id": "op3", "text": "مروپنم"},
                    {"id": "op4", "text": "با انفوزیون طولانی"},
                    {"id": "op5", "text": "ونکومایسین"}
                ],
                "blanks": [
                    {"id": "_BLANK1_", "solution_id": "op1"},
                    {"id": "_BLANK2_", "solution_id": "op2"},
                    {"id": "_BLANK3_", "solution_id": "op3"},
                    {"id": "_BLANK4_", "solution_id": "op4"}
                ],
                "points_per_correct": 10
            }
        ]
    }
}

# آپدیت کردن مسیر یادگیری (Learning Path) برای نمایش در داشبورد
LEARNING_PATH = [
    {
        "id": "unit_1",
        "title": "بخش ۱: دسته‌بندی و ساختار",
        "description": "شناخت خانواده‌های اصلی آنتی‌بیوتیک‌ها",
        "color": "#58cc02", # سبز
        "levels": [
            "class_1_penicillins",
            "class_2_ceph_basic",
            "class_3_ceph_adv",
            "class_4_cellwall_others",
            "class_5_protein",
            "class_6_dna"
        ]
    },
    {
        "id": "unit_2",
        "title": "بخش ۲: اشکال دارویی",
        "description": "دوزها، نسبت‌ها و فرمولاسیون‌ها",
        "color": "#ce82ff", # بنفش
        "levels": [
            "dosage_1_betalactams",
            "dosage_2_dosing",
            "dosage_3_abx_forms",
            "dosage_4_av_af"
        ]
    },
    {
        "id": "unit_3",
        "title": "بخش ۳: کاربرد بالینی (پایه)",
        "description": "پوشش میکروبی و نکات ایمنی",
        "color": "#ff9600", # نارنجی
        "levels": [
            "clinical_1_coverage",
            "clinical_2_admin",
            "clinical_3_risks"
        ]
    },
    {
        "id": "unit_4",
        "title": "بخش ۴: کاربرد بالینی (پیشرفته)",
        "description": "عوارض جانبی، تداخلات و مقاومت",
        "color": "#ff4b4b", # قرمز
        "levels": [
            "clinical_4_side_effects",
            "clinical_5_tb_tetra",
            "clinical_6_special"
        ]
    },
    {
        "id": "unit_5",
        "title": "بخش ۵: فارماکودینامیک",
        "description": "مفاهیم تخصصی PK/PD",
        "color": "#1cb0f6", # آبی
        "levels": [
            "pd_1_concepts"
        ]
    }
]