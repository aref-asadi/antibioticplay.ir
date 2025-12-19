# backend/app/quiz_data.py

QUIZZES = {
    # =========================================================================
    # MODULE 1: CLASSIFICATION & STRUCTURE
    # =========================================================================
    
    # --- Module 1 - Stage 1: Cell Wall Synthesis Inhibitors ---
    "q_class_stage_1": {
        "id": "q_class_stage_1",
        "title": "دیواره سلولی (Cell Wall)",
        "icon": "fa-shield-virus",
        "description": "مرحله ۱: طبقه بندی آنتی‌بیوتیک‌های موثر بر دیواره سلولی",
        "questions": [
            {
                "id": "q_cws_1",
                "type": "image-labeling",
                "title": "دیواره سلولی",
                "text": "آنتی بیوتیک های زیر همگی بر ساختار دیواره سلولی باکتری موثرند. هر آنتی بیوتیک را در جایگاه درست از نطر طبقه بندی قرار دهید.",
                "hint": "پنی‌سیلین‌ها معمولاً به 'cillin' ختم می‌شوند، سفالوسپورین‌ها با 'cef/ceph' شروع می‌شوند و کارباپنم‌ها به 'penem' ختم می‌شوند.",
                "image": "/images/questions/cws_classification.png",
                "points_per_correct": 10,
                "zones": [
                    {"id": "z_penicillins", "label": "Penicillins", "y": 15, "x": 5, "width": 20, "height": 20},
                    {"id": "z_cephalosporins", "label": "Cephalosporins", "y": 15, "x": 30, "width": 20, "height": 20},
                    {"id": "z_carbapenems", "label": "Carbapenems", "y": 15, "x": 55, "width": 20, "height": 20},
                    {"id": "z_glycopeptides", "label": "Glycopeptides", "y": 45, "x": 15, "width": 20, "height": 20},
                    {"id": "z_others", "label": "Others/Monobactams", "y": 45, "x": 45, "width": 20, "height": 20}
                ],
                "options": [
                    {"id": "ampicillin", "text": "آمپی سیلین"},
                    {"id": "oxacillin", "text": "اگزاسیلین"},
                    {"id": "pen_v", "text": "پنی سیلین V"},
                    {"id": "pen_benz", "text": "پنی سیلین بنزاتین"},
                    {"id": "nafcillin", "text": "نفی سیلین"},
                    {"id": "cefazolin", "text": "سفازولین"},
                    {"id": "cephalexin", "text": "سفالکسین"},
                    {"id": "cephalothin", "text": "سفالوتین"},
                    {"id": "ceftazidime", "text": "سفتازیدیم"},
                    {"id": "cefotaxime", "text": "سفوتاکسیم"},
                    {"id": "ceftriaxone", "text": "سفتریاکسون"},
                    {"id": "cefixime", "text": "سفکسیم"},
                    {"id": "cefepime", "text": "سفپیم"},
                    {"id": "ceftaroline", "text": "سفتارولین"},
                    {"id": "azobactam", "text": "آزوباکتام"}, 
                    {"id": "meropenem", "text": "مروپنم"},
                    {"id": "ertapenem", "text": "ارتاپنم"},
                    {"id": "vancomycin", "text": "ونکومایسین"},
                    {"id": "teicoplanin", "text": "تیکوپلانین"}
                ],
                "solution": {
                    "z_penicillins": ["ampicillin", "oxacillin", "pen_v", "pen_benz", "nafcillin"],
                    "z_cephalosporins": ["cefazolin", "cephalexin", "cephalothin", "ceftazidime", "cefotaxime", "ceftriaxone", "cefixime", "cefepime", "ceftaroline"],
                    "z_carbapenems": ["meropenem", "ertapenem"],
                    "z_glycopeptides": ["vancomycin", "teicoplanin"],
                    "z_others": ["azobactam"] 
                }
            }
        ]
    },

    # --- Module 1 - Stage 2: Other Antibiotics ---
    "q_class_stage_2": {
        "id": "q_class_stage_2",
        "title": "سایر مکانیسم‌ها (Other Mechanisms)",
        "icon": "fa-pills",
        "description": "مرحله ۲: طبقه بندی آنتی‌بیوتیک‌های موثر بر پروتئین و DNA",
        "questions": [
            {
                "id": "q_others_1",
                "type": "image-labeling",
                "title": "سایر طبقه بندی ها",
                "text": "آنتی بیوتیک های زیر را به طبقه بندی درست از جدول انتقال دهید.",
                "hint": "فلوروکینولون‌ها به 'floxacin' ختم می‌شوند. ماکرولیدها معمولاً پسوند 'mycin' دارند اما ساختار حلقه بزرگ لاکتونی دارند (مثل آزیترومایسین).",
                "image": "/images/questions/o_classification.png",
                "points_per_correct": 10,
                "zones": [
                    {"id": "z_aminoglycosides", "label": "Aminoglycosides", "y": 10, "x": 10, "width": 25, "height": 15},
                    {"id": "z_tetracyclines", "label": "Tetracyclines", "y": 10, "x": 40, "width": 25, "height": 15},
                    {"id": "z_macrolides", "label": "Macrolides/Lincosamides", "y": 35, "x": 10, "width": 25, "height": 15},
                    {"id": "z_fluoroquinolones", "label": "Fluoroquinolones", "y": 35, "x": 40, "width": 25, "height": 15},
                    {"id": "z_others_2", "label": "Others (Sulfa/Nitro/etc)", "y": 60, "x": 25, "width": 25, "height": 15}
                ],
                "options": [
                    {"id": "neomycin", "text": "نئومایسین"},
                    {"id": "tobramycin", "text": "توبرامایسین"},
                    {"id": "amikacin", "text": "آمیکاسین"},
                    {"id": "minocycline", "text": "مینوسیکلین"},
                    {"id": "tigecycline", "text": "تیگسیکلین"},
                    {"id": "linezolid", "text": "لینزولید"},
                    {"id": "azithromycin", "text": "آزیترومایسین"},
                    {"id": "clindamycin", "text": "کلیندامایسین"},
                    {"id": "levofloxacin", "text": "لووفلوکساین"},
                    {"id": "ofloxacin", "text": "افلوکساسین"},
                    {"id": "moxifloxacin", "text": "موکسی فلوکساین"},
                    {"id": "nalidixic_acid", "text": "نالیدیکسیک اسید"},
                    {"id": "sulfasalazine", "text": "سولفاسالازین"},
                    {"id": "sulfadiazine", "text": "سولفادیازین"},
                    {"id": "metronidazole", "text": "مترونیدازول"}
                ],
                "solution": {
                    "z_aminoglycosides": ["neomycin", "tobramycin", "amikacin"],
                    "z_tetracyclines": ["minocycline", "tigecycline"],
                    "z_macrolides": ["azithromycin", "clindamycin"], 
                    "z_fluoroquinolones": ["levofloxacin", "ofloxacin", "moxifloxacin", "nalidixic_acid"],
                    "z_others_2": ["sulfasalazine", "sulfadiazine", "linezolid", "metronidazole"]
                }
            }
        ]
    },

    # =========================================================================
    # MODULE 2: DOSAGE FORMS
    # =========================================================================

    # --- Module 2 - Stage 1: Beta-lactams & Combinations ---
    "q_dosage_stage_1": {
        "id": "q_dosage_stage_1",
        "title": "اشکال دارویی - بخش اول",
        "icon": "fa-flask",
        "description": "فرمولاسیون‌های بتالاکتام، نسبت‌ها و دوزینگ",
        "questions": [
            {
                # Q1: Beta-lactam Combinations
                "id": "q_betalactam_combo",
                "type": "drag-drop-match",
                "title": "ترکیب با مهارکننده بتالاکتاماز",
                "text": "هر آنتی‌بیوتیک بتالاکتام را به مهارکننده بتالاکتاماز که با آن فرموله شده وصل کنید.",
                "hint": "آموکسی‌سیلین و کلاوولانات هر دو خوراکی هستند. پیپراسیلین با تازوباکتام (Tazocin) ترکیب می‌شود. ترکیب جدید سفتازیدیم با آویباکتام است.",
                "points_per_correct": 10,
                "items_left": [
                    {"id": "l_amox", "text": "آموکسی سیلین"},
                    {"id": "l_amp", "text": "آمپی سیلین"},
                    {"id": "l_pip", "text": "پیپراسیلین"},
                    {"id": "l_cef", "text": "سفتازیدیم"}
                ],
                "items_right": [
                    {"id": "r_clav", "text": "کلاوولانات"},
                    {"id": "r_sulb", "text": "سولباکتام"},
                    {"id": "r_tazo", "text": "تازوباکتام"},
                    {"id": "r_avi", "text": "آویباکتام"}
                ],
                "solution": {
                    "l_amox": "r_clav",
                    "l_amp": "r_sulb",
                    "l_pip": "r_tazo",
                    "l_cef": "r_avi"
                }
            },
            {
                # Q2: Co-Amoxiclav Ratios
                "id": "q_coamox_ratios",
                "type": "drag-drop-ordering",
                "title": "نسبت‌های کوآموکسی‌کلاو",
                "text": "هر سوسپانسیون کوآموکسی‌کلاو را در دسته مربوط به نسبت (آموکسی‌سیلین به کلاوولانات) صحیح قرار دهید.",
                "hint": "در سوسپانسیون‌های معمول (156 و 312) نسبت 4:1 است. سوسپانسیون 643 غلیظ‌ترین فرم با نسبت 14:1 است.",
                "points_per_correct": 10,
                "buckets": [
                    {"id": "b_1_4", "label": "نسبت 4:1"},
                    {"id": "b_1_7", "label": "نسبت 7:1"},
                    {"id": "b_1_14", "label": "نسبت 14:1"}
                ],
                "items": [
                    {"id": "s_156", "text": "سوسپانسیون 156"},
                    {"id": "s_312", "text": "سوسپانسیون 312"},
                    {"id": "s_228", "text": "سوسپانسیون 228"},
                    {"id": "s_457", "text": "سوسپانسیون 457"},
                    {"id": "s_643", "text": "سوسپانسیون 643"}
                ],
                "solution": {
                    "s_156": "b_1_4",
                    "s_312": "b_1_4",
                    "s_228": "b_1_7",
                    "s_457": "b_1_7",
                    "s_643": "b_1_14"
                }
            },
            {
                # Q3: Ampicillin-Sulbactam Details
                "id": "q_amp_sulb_fill",
                "type": "drag-drop-fill",
                "title": "اطلاعات آمپی‌سیلین-سولباکتام",
                "text": "جاهای خالی را با توجه به اطلاعات دارویی آمپی‌سیلین-سولباکتام در ایران پر کنید.",
                "hint": "نسبت این دارو 2 به 1 است (مثلاً ویال 1.5 گرمی شامل 1 گرم آمپی‌سیلین است). دوزینگ همیشه بر اساس جزء آنتی‌بیوتیک (آمپی‌سیلین) است.",
                "points_per_correct": 10,
                "blanks": [
                    {"id": "b_form1", "text": "این دارو با اشکال دارویی", "solution_id": "opt_1_5"},
                    {"id": "b_form2", "text": "و", "solution_id": "opt_3"},
                    {"id": "b_ratio", "text": "در بازار وجود دارد و نسبت آمپی‌سیلین به سولباکتام", "solution_id": "opt_2_1"},
                    {"id": "b_dosing", "text": "است. دوزینگ بر اساس جزء", "solution_id": "opt_amp_part"},
                    {"id": "b_end", "text": "صورت می‌گیرد.", "solution_id": None}
                ],
                "options": [
                    {"id": "opt_1_5", "text": "1.5 گرم"},
                    {"id": "opt_3", "text": "3 گرم"},
                    {"id": "opt_2_1", "text": "2:1"},
                    {"id": "opt_amp_part", "text": "آمپی‌سیلین"},
                    {"id": "opt_sulb_part", "text": "سولباکتام"},
                    {"id": "opt_total", "text": "مجموع"}
                ]
            },
            {
                # Q4: Pip-Tazo Details
                "id": "q_pip_tazo_fill",
                "type": "drag-drop-fill",
                "title": "اطلاعات پیپراسیلین-تازوباکتام",
                "text": "جاهای خالی را با توجه به اطلاعات دارویی پیپراسیلین-تازوباکتام پر کنید.",
                "hint": "برخلاف آمپی-سولباکتام، دوزینگ این دارو بر اساس **مجموع** هر دو جزء بیان می‌شود. نسبت پیپراسیلین به تازوباکتام 8 به 1 است.",
                "points_per_correct": 10,
                "blanks": [
                    {"id": "b_forms", "text": "این دارو با اشکال دارویی 2.25، 3.375 و", "solution_id": "opt_4_5"},
                    {"id": "b_ratio", "text": "گرم موجود است و نسبت پیپراسیلین به تازوباکتام", "solution_id": "opt_8_1"},
                    {"id": "b_dosing", "text": "است. دوزینگ بر اساس جزء", "solution_id": "opt_total_pip"},
                    {"id": "b_end", "text": "صورت می‌گیرد.", "solution_id": None}
                ],
                "options": [
                    {"id": "opt_4_5", "text": "4.5 گرم"},
                    {"id": "opt_8_1", "text": "8:1"},
                    {"id": "opt_16_1", "text": "16:1"},
                    {"id": "opt_pip_part", "text": "پیپراسیلین"},
                    {"id": "opt_tazo_part", "text": "تازوباکتام"},
                    {"id": "opt_total_pip", "text": "مجموع پیپراسیلین-تازوباکتام"}
                ]
            },
            {
                # Q5: Imipenem Dosing (Multiple Select)
                "id": "q_imipenem_calc",
                "type": "multiple-select",
                "title": "محاسبه دوز ایمی‌پنم",
                "text": "برای بیماری ایمی‌پنم-سیلاستاتین 500 میلی‌گرم تجویز شده است. کدام گزینه‌ها برای هر بار تزریق قابل انتخاب هستند؟",
                "hint": "هر ویال معمولاً به صورت 500/500 (مجموع 1g) یا 250/250 (مجموع 500mg) است. صورت سوال 500mg ایمی‌پنم خواسته است.",
                "points_per_correct": 10,
                "options": [
                    {"id": "opt_1_500", "text": "یک ویال 500/500 میلی گرم"},
                    {"id": "opt_1_250", "text": "یک ویال 250/250 میلی گرم"},
                    {"id": "opt_2_250", "text": "دو ویال 250/250 میلی گرم"},
                    {"id": "opt_half_500", "text": "نصف ویال 500/500 میلی گرم"},
                    {"id": "opt_half_750", "text": "نصف ویال 750/250 میلی گرم"}
                ],
                "solution": ["opt_1_500", "opt_2_250"]
            }
        ]
    },

    # --- Module 2 - Stage 2: Other Classes Formulations ---
    "q_dosage_stage_2": {
        "id": "q_dosage_stage_2",
        "title": "اشکال دارویی - بخش دوم",
        "icon": "fa-pills",
        "description": "فلوروکینولون‌ها، ماکرولیدها و داروهای ضدویروس/ضدقارچ",
        "questions": [
            {
                # Q6: Fluoroquinolone Eye Drops
                "id": "q_fq_eyes",
                "type": "multiple-select",
                "title": "قطره‌های چشمی فلوروکینولون",
                "text": "کدام یک از داروهای زیر در بازار دارویی ایران شکل دارویی قطره چشمی دارند؟",
                "hint": "جمی‌فلوکساسین (Factive) فقط به صورت قرص خوراکی موجود است. بقیه گزینه‌ها قطره چشمی دارند.",
                "points_per_correct": 10,
                "options": [
                    {"id": "cipro", "text": "سیپروفلوکساسین"},
                    {"id": "levo", "text": "لووفلوکساسین"},
                    {"id": "moxi", "text": "موکسی فلوکساسین"},
                    {"id": "gemi", "text": "جمی فلوکساسین"}
                ],
                "solution": ["cipro", "levo", "moxi"]
            },
            {
                # Q7: Macrolides Forms
                "id": "q_macrolide_forms",
                "type": "drag-drop-ordering",
                "title": "اشکال دارویی ماکرولیدها",
                "text": "اشکال دارویی موجود در بازار ایران را به داروی ماکرولید مربوطه وصل کنید.",
                "hint": "اریترومایسین قدیمی‌ترین ماکرولید است و اشکال موضعی و پماد چشمی دارد. آزیترومایسین سوسپانسیون ER و قطره چشمی دارد.",
                "points_per_correct": 10,
                "buckets": [
                    {"id": "b_clari", "label": "کلاریترومایسین"},
                    {"id": "b_azithro", "label": "آزیترومایسین"},
                    {"id": "b_erythro", "label": "اریترومایسین"}
                ],
                "items": [
                    {"id": "i_susp_125", "text": "سوسپانسیون 125"},
                    {"id": "i_susp_250", "text": "سوسپانسیون 250"}, 
                    {"id": "i_susp_er", "text": "سوسپانسیون ER دو گرمی"},
                    {"id": "i_eye_drop", "text": "قطره چشمی 1 درصد"},
                    {"id": "i_topical_4", "text": "محلول موضعی 4 درصد"},
                    {"id": "i_eye_oint", "text": "پماد چشمی"},
                    {"id": "i_inj_500", "text": "پودر تزریقی 500 میلی گرم"},
                    {"id": "i_gel_2", "text": "ژل موضعی 2 درصد"}
                ],
                "solution": {
                    "i_susp_125": "b_clari",
                    "i_susp_250": "b_azithro",
                    "i_susp_er": "b_azithro",
                    "i_eye_drop": "b_azithro", 
                    "i_inj_500": "b_azithro",
                    "i_topical_4": "b_erythro",
                    "i_eye_oint": "b_erythro",
                    "i_gel_2": "b_erythro"
                }
            },
            {
                # Q8: Nitrofurantoin Forms
                "id": "q_nitro_forms",
                "type": "drag-drop-ordering",
                "title": "فرمولاسیون نیتروفورانتوئین",
                "text": "ویژگی‌های هر فرمولاسیون نیتروفورانتوئین را در دسته صحیح قرار دهید.",
                "hint": "فرم 'ماکروکریستال' جذب سریع‌تر و عوارض گوارشی بیشتری دارد (4 بار در روز). فرم 'مونوهیدرات' در معده ژل تشکیل می‌دهد و آهسته‌رهش است (2 بار در روز).",
                "points_per_correct": 10,
                "buckets": [
                    {"id": "b_macro", "label": "ماکروکریستال"},
                    {"id": "b_mono_macro", "label": "مونوهیدرات/ماکروکریستال"}
                ],
                "items": [
                    {"id": "i_dosing_4", "text": "دوزینگ 4 بار در روز"},
                    {"id": "i_dosing_2", "text": "دوزینگ 2 بار در روز"},
                    {"id": "i_slow_diss", "text": "انحلال کند در معده"},
                    {"id": "i_gel_form", "text": "تشکیل ژل و آزادسازی طولانی"},
                    {"id": "i_less_gi", "text": "عوارض گوارشی کمتر"}
                ],
                "solution": {
                    "i_dosing_4": "b_macro",
                    "i_slow_diss": "b_macro", # نکته: ماکروکریستال انحلالش کندتر از میکروکریستال است اما نسبت به مونوهیدرات سریعتر است. طبق اسلایدها، مونوهیدرات ژل تشکیل میدهد.
                    "i_dosing_2": "b_mono_macro",
                    "i_gel_form": "b_mono_macro",
                    "i_less_gi": "b_mono_macro"
                }
            },
            {
                # Q9: Antivirals
                "id": "q_antiviral_feat",
                "type": "drag-drop-match",
                "title": "ویژگی‌های آنتی‌ویروس‌ها",
                "text": "هر ویژگی را به داروی آنتی‌ویروس مربوطه متصل کنید.",
                "hint": "داروهایی که با 'Val' شروع می‌شوند، فرم پیش‌دارو (Prodrug) هستند و معمولاً قرص خوراکی‌اند. گانسیکلوویر داروی اصلی تزریقی برای CMV است.",
                "points_per_correct": 10,
                "items_left": [
                    {"id": "acyclovir", "text": "آسیکلوویر"},
                    {"id": "valacyclovir", "text": "والاسیکلوویر"},
                    {"id": "ganciclovir", "text": "گانسیکلوویر"},
                    {"id": "valganciclovir", "text": "والگانسیلوویر"}
                ],
                "items_right": [
                    {"id": "feat_topical", "text": "کرم موضعی 5% / پماد چشمی 3%"},
                    {"id": "feat_tabs", "text": "قرص های 500 و 1000"},
                    {"id": "feat_inj_glove", "text": "تزریقی (نیاز به دستکش)"},
                    {"id": "feat_cmv", "text": "پیش‌دارو / درمان CMV"}
                ],
                "solution": {
                    "acyclovir": "feat_topical",
                    "valacyclovir": "feat_tabs",
                    "ganciclovir": "feat_inj_glove",
                    "valganciclovir": "feat_cmv"
                }
            },
            {
                # Q10: Antifungals (Azoles)
                "id": "q_azole_forms",
                "type": "drag-drop-match",
                "title": "اشکال دارویی ضدقارچ‌ها",
                "text": "هر داروی آزول را به شکل دارویی رایج آن در بازار ایران وصل کنید.",
                "hint": "فلوکونازول کپسول‌های ۱۵۰ تایی معروف دارد. کتوکونازول تنها آزولی است که شامپو دارد. وریکونازول برای عفونت‌های چشمی و سیستمیک قرص‌های ۲۰۰ دارد.",
                "points_per_correct": 10,
                "items_left": [
                    {"id": "l_keto", "text": "کتوکونازول"},
                    {"id": "l_fluco", "text": "فلوکونازول"},
                    {"id": "l_itra", "text": "ایتراکونازول"},
                    {"id": "l_vori", "text": "وریکونازول"},
                    {"id": "l_posa", "text": "پوساکونازول"}
                ],
                "items_right": [
                    {"id": "r_shampoo", "text": "شامپو 2% / قرص 200"},
                    {"id": "r_cap_150", "text": "کپسول 100 و 150"},
                    {"id": "r_cap_100", "text": "کپسول 100"},
                    {"id": "r_tab_200", "text": "قرص 50 و 200"},
                    {"id": "r_amp_300", "text": "آمپول 300 میلی گرم"}
                ],
                "solution": {
                    "l_keto": "r_shampoo",
                    "l_fluco": "r_cap_150",
                    "l_itra": "r_cap_100",
                    "l_vori": "r_tab_200",
                    "l_posa": "r_amp_300"
                }
            }
        ]
    }
}

# -------------------------------------------------------------------------
# مسیر یادگیری (Learning Path)
# -------------------------------------------------------------------------
LEARNING_PATH = [
    {
        "id": "unit_1",
        "title": "Classification & Structure",
        "description": "شناخت خانواده‌های آنتی‌بیوتیک و ساختار آن‌ها",
        "color": "#4caf50", 
        "levels": ["q_class_stage_1", "q_class_stage_2"]
    },
    {
        "id": "unit_2",
        "title": "Dosage Forms",
        "description": "اشکال دارویی، نسبت‌ها و دوزینگ",
        "color": "#ff9800",
        "levels": ["q_dosage_stage_1", "q_dosage_stage_2"]
    },
    {
        "id": "unit_3",
        "title": "Clinical Application",
        "description": "کاربردهای بالینی",
        "color": "#2196f3",
        "levels": [] 
    }
]