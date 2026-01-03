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
                "hint": "/images/questions/cws_classification_hint.jpg",
                "image": "/images/questions/cws_classification.png",
                "points_per_correct": 10,
                "zones": [
                    {"id": "z_natural_penicillins", "label": "Natural Penicillins", "y": 5, "x": 5, "width": 30, "height": 5},
                    {"id": "z_amino_penicillins", "label": "Amino Penicillins", "y": 5, "x": 12.5, "width": 30, "height": 5},
                    {"id": "z_penicillinase_resistant", "label": "Penicillinase Resistant", "y": 5, "x": 21, "width": 50, "height": 5},
                    {"id": "z_cephalosporins1", "label": "Cephalosporins 1", "y": 5, "x": 27.5, "width": 35, "height": 7.5},
                    {"id": "z_cephalosporins2", "label": "Cephalosporins 2", "y": 5, "x": 37.5, "width": 35, "height": 7.5},
                    {"id": "z_cephalosporins3", "label": "Cephalosporins 3", "y": 5, "x": 47.5, "width": 35, "height": 20},
                    {"id": "z_cephalosporins4", "label": "Cephalosporins 4", "y": 5, "x": 67.5, "width": 35, "height": 4},
                    {"id": "z_cephalosporins5", "label": "Cephalosporins 5", "y": 5, "x": 72.5, "width": 35, "height": 4},
                    {"id": "z_carbapenems", "label": "Carbapenems", "y": 5, "x": 77.5, "width": 50, "height": 4},
                    {"id": "z_monobactams", "label": "Monobactams", "y": 5, "x": 82, "width": 50, "height": 4},
                    {"id": "z_beta_lactamsase_inhibitors", "label": "Beta Lactamsase Inhibitors", "y": 5, "x": 86.5, "width": 50, "height": 4},
                    {"id": "z_glycopeptides", "label": "Glycopeptides", "y": 5, "x": 92, "width": 50, "height": 6}
                ],
                "options": [
                    {"id": "ampicillin", "text": "آمپی سیلین"},
                    {"id": "oxacillin", "text": "اگزاسیلین"},
                    {"id": "pen_v", "text": "پنی سیلین V"},
                    {"id": "pen_benz", "text": "پنی سیلین بنزاتین"},
                    {"id": "nafcillin", "text": "نفی سیلین"},
                    {"id": "cefazolin", "text": "سفازولین"},
                    {"id": "cephalexin", "text": "سفالکسین"},
                    {"id": "cefuroxime", "text": "سفوروکسیم"},
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
                    "z_natural_penicillins": ["pen_v", "pen_benz"],
                    "z_amino_penicillins": ["ampicillin"],
                    "z_penicillinase_resistant": ["oxacillin", "nafcillin"],
                    "z_cephalosporins1": ["cefazolin", "cephalexin", "cephalothin"],
                    "z_cephalosporins2": ["cefuroxime"],
                    "z_cephalosporins3": ["cefixime", "ceftazidime", "cefotaxime", "ceftriaxone"],
                    "z_cephalosporins4": ["cefepime"],
                    "z_cephalosporins5": ["ceftaroline"],
                    "z_monobactams": ["azobactam"],
                    "z_carbapenems": ["meropenem", "ertapenem"],
                    "z_beta_lactamsase_inhibitors": [],
                    "z_glycopeptides": ["vancomycin", "teicoplanin"]
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
                "hint": "/images/questions/o_classification_hint.jpg",
                "image": "/images/questions/o_classification.png",
                "points_per_correct": 10,
                "zones": [
                    {"id": "z_aminoglycosides", "label": "Aminoglycosides", "y": 2.5, "x": 2.5, "width": 57.5, "height": 7.5},
                    {"id": "z_tetracyclines", "label": "Tetracyclines", "y": 2.5, "x": 15, "width": 57.5, "height": 7.5},
                    {"id": "z_oxazolidonones", "label": "Oxazolidonones", "y": 2.5, "x": 26, "width": 57.5, "height": 5},
                    {"id": "z_streptogramins", "label": "Streptogramins", "y": 2.5, "x": 32, "width": 57.5, "height": 5},
                    {"id": "z_chloramphenicol", "label": "Chloramphenicol", "y": 2.5, "x": 39, "width": 70, "height": 5},
                    {"id": "z_macrolides", "label": "Macrolides", "y": 2.5, "x": 45, "width": 57.5, "height": 5},
                    {"id": "z_lincosamides", "label": "Lincosamides", "y": 2.5, "x": 50, "width": 57.5, "height": 5},
                    {"id": "z_fluoroquinolones", "label": "Fluoroquinolones", "y": 2.5, "x": 57.5, "width": 57.5, "height": 10},
                    {"id": "z_quinolones", "label": "Quinolones", "y": 2.5, "x": 70, "width": 57.5, "height": 5},
                    {"id": "z_sulfonamides", "label": "Sulfonamides", "y": 2.5, "x": 76, "width": 57.5, "height": 5},
                    {"id": "z_dhfr_inhibitors", "label": "DHFR Inhibitors", "y": 2.5, "x": 82, "width": 57.5, "height": 5},
                    {"id": "z_dna_damage", "label": "DNA Damage", "y": 2.5, "x": 88, "width": 80, "height": 5},
                    {"id": "z_mrna_synthesis", "label": "mRNA Synthesis", "y": 2.5, "x": 94, "width": 80, "height": 5}
                ],
                "options": [
                    {"id": "neomycin", "text": "نئومایسین"},
                    {"id": "tobramycin", "text": "توبرامایسین"},
                    {"id": "amikacin", "text": "آمیکاسین"},
                    {"id": "minocycline", "text": "مینوسیکلین"},
                    {"id": "tigecycline", "text": "تیگسیکلین"},
                    {"id": "linezolid", "text": "لینزولید"},
                    {"id": "azithromycin", "text": "آزیترومایسین"},
                    {"id": "quinopristin/dalfopristin", "text": "کیناپریستین/دالفاپریستین"},
                    {"id": "clindamycin", "text": "کلیندامایسین"},
                    {"id": "levofloxacin", "text": "لووفلوکساین"},
                    {"id": "chloramphenicol", "text":"کلرامفنیکل"},
                    {"id": "ofloxacin", "text": "افلوکساسین"},
                    {"id": "moxifloxacin", "text": "موکسی فلوکساین"},
                    {"id": "trimethoprim", "text": "تریمتوپریم"},
                    {"id": "nalidixic_acid", "text": "نالیدیکسیک اسید"},
                    {"id": "sulfasalazine", "text": "سولفاسالازین"},
                    {"id": "rifampin", "text": "ریفامپین"},
                    {"id": "sulfadiazine", "text": "سولفادیازین"},
                    {"id": "metronidazole", "text": "مترونیدازول"}
                ],
                "solution": {
                    "z_aminoglycosides": ["neomycin", "tobramycin", "amikacin"],
                    "z_tetracyclines": ["minocycline", "tigecycline"],
                    "z_oxazolidonones": ["linezolid"],
                    "z_streptogramins": ["quinopristin/dalfopristin"],
                    "z_chloramphenicol": ["chloramphenicol"],
                    "z_macrolides": ["azithromycin"],
                    "z_lincosamides": ["clindamycin"],
                    "z_fluoroquinolones": ["levofloxacin", "ofloxacin", "moxifloxacin"],
                    "z_quinolones": ["nalidixic_acid"],
                    "z_sulfonamides": ["sulfasalazine", "sulfadiazine"],
                    "z_dhfr_inhibitors": ["trimethoprim"],
                    "z_dna_damage": ["metronidazole"],
                    "z_mrna_synthesis": ["rifampin"]
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
        "title": "اشکال دارویی - بتالاکتام‌ها",
        "icon": "fa-flask",
        "description": "ترکیبات بتالاکتام، نسبت‌های کوآموکسی‌کلاو و دوزینگ‌های خاص",
        "questions": [
            {
                # Page 2: Beta-lactam Combinations
                "id": "q_betalactam_combo",
                "type": "drag-drop-match", # Using match component for pairing
                "title": "ترکیب با مهارکننده بتالاکتاماز",
                "instruction": "هر آنتی بیوتیک بتالاکتام موجود در بازار دارویی ایران در ترکیب با کدام مهارکننده بتالاکتاماز فرموله شده است؟",
                "hint": "کلاوولانات (کلاوولانیک اسید)، سولباکتام، تازوباکتام و آویباکتام مهارکننده‌های بتالاکتاماز هستند. این ترکیبات ذاتاً فعالیت ضدمیکروبی کمی دارند اما می‌توانند فعالیت تعداد زیادی از بتالاکتامازها را مهار ‌کنند. ترکیب این داروها با آنتی‌بیوتیک‌هایی مانند آموکسی‌سیلین، آمپی‌سیلین، پیپراسیلین و سفتازیدیم باعث افزایش قابل توجه اثربخشی آنها در برابر باکتری‌های تولید کننده بتالاکتاماز می‌شود. مهارکننده‌های بتالاکتاماز از طریق کلیوی از بدن دفع می‌شوند و متابولیسک کبدی قابل توجهی ندارند.",
                "categories": [
                    {"id": "cat_clav", "text": "کلاوولانات"},
                    {"id": "cat_sulb", "text": "سولباکتام"},
                    {"id": "cat_tazo", "text": "تازوباکتام"},
                    {"id": "cat_avi", "text": "آویباکتام"}
                ],
                "items": [
                    {"id": "item_amox", "text": "آموکسی سیلین"},
                    {"id": "item_amp", "text": "آمپی سیلین"},
                    {"id": "item_pip", "text": "پیپراسیلین"},
                    {"id": "item_cef", "text": "سفتازیدیم"}
                ],
                "solution": {
                    "cat_clav": ["item_amox"],
                    "cat_sulb": ["item_amp"],
                    "cat_tazo": ["item_pip"],
                    "cat_avi": ["item_cef"]
                },
                "explanation": "آموکسی سیلین- کلاوولانات / پیپراسیلین-تازوباکتام / سفتازیدیم-آویباکتام / آمپی سیلین-سولباکتام"
            },
            {
                # Page 3: Co-Amoxiclav Ratios
                "id": "q_coamox_ratios",
                "type": "drag-drop-match", # Bucket sorting
                "title": "نسبت‌های کوآموکسی‌کلاو",
                "instruction": "در خصوص سوسپانسیون‌های کوآموکسی کلاو موجود در بازار ایران، هر فرآورده را به نسبت صحیح (آموکسی سیلین به کلاوولانات) وصل کنید.",
                "hint": "آموکسی‌سیلین-کلاوولانات که به طور رایج‌تر به نام «کوآموکسی‌کلاو» شناخته می‌شود، به صورت خوراکی و تزریقی قابل استفاده است. علاوه بر ارگانیسم‌هایی که به طور معمول توسط آموکسی‌سیلین مهار می‌شوند، اغلب سویه‌های استافیلوکوک اورئوس حساس به اگزاسیلین و هموفیلوس آنفلوانزا تولیدکننده بتالاکتاماز نیز توسط این ترکیب مهار می‌شوند. آموکسی‌سیلین-کلاوولانات می‌تواند به عنوان درمان خوراکی برای بیماران مبتلا به اوتیت مدیا، سینوزیت، عفونت‌های دستگاه تنفس تحتانی، زخم گازگرفتگی و عفونت‌های مجاری ادراری به کار رود. شیوع اسهال با این فرآورده بیشتر از آموکسی‌سیلین به تنهایی است. همچنین عوارضی مانند زردی کلستاتیک، هپاتیت و سمیت کبدی نیز با این ترکیب گزارش شده است. \br محاسبه دوز روزانه (mg/kg) مورد نیاز در کودکان، بر اساس جزء آموکسی‌سیلین این فرآورده صورت می‌گیرد، نه مجموع میلی‌گرم آموکسی‌سیلین و کلاوولانات. از سوی دیگر، حداکثر دوز روزانه توصیه شده از کلاوولانات برابر با mg/kg/d 4/6 است و دریافت مقادیر بیشتر از این، منجر به بروز اسهال و تشنج می‌شود. رعایت حداکثر دوز کلاوولانات خصوصاً در اندیکاسیون‌هایی مانند اوتیت مدیا که نیاز به دوز بالای آموکسی‌سیلین وجود دارد، ضروری است، زیرا همانطور که اشاره شد، دوزینگ آموکسی‌سیلین-کلاوولانات فقط بر اساس جزء آموکسی‌سیلین آن محاسبه می‌شود و در چنین شرایطی ممکن است دوز کلاوولانات بیشتر از حداکثر دوز توصیه شده آن شود. \br در فرمولاسیون‌های ابتدایی سوسپانسیون‌ آموکسی‌سیلین-کلاوولانات، نسبت میلی‌گرم آموکسی‌سیلین به کلاوولانات برابر با 4 به 1 بود. در اندیکاسیون‌های نیازمند دوز بالای دارو، استفاده از این فرمولاسیون‌ها در بسیاری از بیماران موجب دریافت کلاوولانات بیشتر از حداکثر دوز روزانه آن می‌شد. لذا در فرمولاسیون‌های جدیدتر این نسبت به 7:1 و سپس به 14:1 تغییر یافت؛ بدین ترتیب، امکان دریافت دوزهای بالاتر روزانه از آموکسی‌سیلین بدون عبور از حداکثر دوز روزانه کلاوولانات فراهم شد. کاهش مقدار کلاوولانات در این فرآورده‌ها منجر به کاهش اثربخشی دارو نمی‌شود و همین مقدار نیز به طور مؤثری می‌تواند بتالاکتاماز باکتریایی را مهار کند.",
                "categories": [
                    {"id": "cat_1_4", "text": "نسبت 1:4"},
                    {"id": "cat_1_7", "text": "نسبت 1:7"},
                    {"id": "cat_1_14", "text": "نسبت 1:14"}
                ],
                "items": [
                    {"id": "s_156", "text": "سوسپانسیون 156"},
                    {"id": "s_312", "text": "سوسپانسیون 312"},
                    {"id": "s_228", "text": "سوسپانسیون 228"},
                    {"id": "s_457", "text": "سوسپانسیون 457"},
                    {"id": "s_643", "text": "سوسپانسیون 643"}
                ],
                "solution": {
                    "cat_1_4": ["s_156", "s_312"],
                    "cat_1_7": ["s_228", "s_457"],
                    "cat_1_14": ["s_643"]
                },
                "explanation": "سوسپانسیون‌های 156 و 312 با نسبت 1:4 / سوسپانسیون‌های 228 و 457 با نسبت 1:7 / سوسپانسیون 643 با نسبت 1:14"
            },
            {
                # Page 4: Ampicillin-Sulbactam Fill in the blanks
                "id": "q_amp_sulb_fill",
                "type": "drag-drop-fill",
                "title": "آمپی‌سیلین - سولباکتام",
                "instruction_template": "داروی آمپی سیلین سولباکتام با اشکال دارویی _BLANK1_ و _BLANK2_ در بازار دارویی ایران وجود دارد و نسبت آمپی سیلین به سولباکتام در این فرآورده‌ها _BLANK3_ است. دوزینگ این دارو بر اساس جزء _BLANK4_ صورت می‌گیرد.",
                "instruction": "جاهای خالی را با توجه به اطلاعات دارویی آمپی‌سیلین-سولباکتام پر کنید.",
                "hint": "آمپی‌سیلین-سولباکتام یک فرآورده تزریقی‌ است که علاوه بر طیف اثر آمپی‌سیلین، روی بیشتر سویه‌های استافیلوکوک اورئوس و هموفیلوس آنفلوانزا تولیدکننده بتالاکتاماز، برخی باکتری‌های خانواده انتروباکتریاسه و بی‌هوازی‌ها (شامل باکتروئیدس فراژیلیس) نیز اثر می‌گذارد. جزء سولباکتام بر روی آسینتوباکتر اثر مهاری دارد. با این حال، مقاومت میکروبی در بین گونه‌های انتروباکتریاسه و بی‌هوازی‌ها در مقابل این آنتی‌بیوتیک رو به افزایش است. \br اشکال دارویی موجود در ایران به شرح ذیل است: \br Injection powder 3 g (2 g ampicillin + 1 g sulbactam), 1.5 g  (1 g ampicillin + 0.5 g sulbactam)",
                "options": [
                    {"id": "opt_1_5", "text": "1.5 گرم"},
                    {"id": "opt_3", "text": "3 گرم"},
                    {"id": "opt_4_5", "text": "4.5 گرم"},
                    {"id": "opt_2_1", "text": "2:1"},
                    {"id": "opt_8_1", "text": "8:1"},
                    {"id": "opt_amp", "text": "آمپی سیلین"},
                    {"id": "opt_total", "text": "مجموع آمپی سیلین و سولباکتام"}
                ],
                "solution": {
                    "_BLANK1_": "opt_1_5",
                    "_BLANK2_": "opt_3",
                    "_BLANK3_": "opt_2_1",
                    "_BLANK4_": "opt_total"
                },
                "explanation": "داروی آمپی سیلین-سولباکتام با اشکال دارویی 3 گرم و 1.5 گرم در بازار دارویی ایران وجود دارد و نسبت آمپی سیلین به سولباکتام در این فرآورده‌ها 2 به 1 است. دوزینگ این دارو بر اساس مجموع آمپی سیلین-سولباکتام صورت می گیرد."
            },
            {
                # Page 5: Pip-Tazo Fill in the blanks
                "id": "q_pip_tazo_fill",
                "type": "drag-drop-fill",
                "title": "پیپراسیلین - تازوباکتام",
                "instruction_template": "داروی پیپراسیلین تازوباکتام با اشکال دارویی 2.25، 3.375 و _BLANK1_ در بازار دارویی ایران وجود دارد و نسبت پیپراسیلین به تازوباکتام در این فرآورده‌ها _BLANK2_ است. دوزینگ این دارو بر اساس جزء _BLANK3_ صورت می‌گیرد.",
                "instruction": "جاهای خالی را با گزینه‌های صحیح پر کنید.",
                "hint": "پیپراسیلین-تازوباکتام نیز طیف اثر پیپراسیلین را با اثرگذاری روی استافیلوکوک اورئوس و هموفیلوس آنفلوانزا تولیدکننده بتالاکتاماز، گونوکوک، برخی باکتری‌های انتروباکتریاسه و بی‌هوازی‌ها (شامل باکتروئیدس فراژیلیس) گسترش می‌دهد. طیف اثر و اندیکاسیون‌های این ترکیب مشابه آمپی‌سیلین-سولباکتام است. اشکال دارویی موجود در ایران به شرح ذیل است:\brInjection powder 2.25 g (2 g piperacillin + 250 mg tazobactam), 3.375 g (3 g piperacillin + 375 mg tazobactam), 4.5 g (4 g piperacillin + 500 mg tazobactam)",
                "options": [
                    {"id": "opt_4_5", "text": "4.5 گرم"},
                    {"id": "opt_5", "text": "5 گرم"},
                    {"id": "opt_8_1", "text": "8:1"},
                    {"id": "opt_4_1", "text": "4:1"},
                    {"id": "opt_pip", "text": "پیپراسیلین"},
                    {"id": "opt_total_pip", "text": "مجموع پیپراسیلین تازوباکتام"}
                ],
                "solution": {
                    "_BLANK1_": "opt_4_5",
                    "_BLANK2_": "opt_8_1",
                    "_BLANK3_": "opt_total_pip"
                },
                "explanation": "داروی پیپراسیلین-تازوباکتام با اشکال دارویی 250/2 و 750/3 و 5/4 در بازار دارویی ایران وجود دارد و نسبت پیپراسیلین به تازوباکتام در این فرآورده ها 8 به 1 است . دوزینگ این دارو بر اساس جزء مجموع پیپراسیلین-تازوباکتام صورت می گیرد. "
            },
            {
                # Page 6: Imipenem Dosing Scenario
                "id": "q_imipenem_calc",
                "type": "multiple-select",
                "title": "محاسبه دوز ایمی‌پنم",
                "instruction": "برای بیماری داروی ایمی پنم سیلاستاتین با دوز 500 میلی گرم هر 6 ساعت تجویز شده است. کدام یک از گزینه‌های زیر را می‌توان در هر بار تزریق دارو برای بیمار انتخاب کرد؟ (ممکن است بیش از یک گزینه صحیح باشد)",
                "hint": "ایمی‌پنم در توبول پروکزیمال کلیه توسط آنزیم کلیوی دهیدروپپتیداز-1 غیرفعال‌ می‌شود. سیلاستاتین مهارکننده این آنزیم است و مصرف همزمان آن با ایمی‌پنم از غیرفعال شدن ایمی‌پنم جلوگیری می‌کند. دوز معمول ایمی‌پنم-سیلاستاتین 500 میلی‌گرم وریدی هر 6 ساعت است. مواردی از سمیت CNS مانند تغییر سطح هشیاری، میوکلونوس و تشنج طی درمان با ایمی‌پنم دیده شده است. این سمیت خصوصاً در بیماران مبتلا به بیماری زمینه‌ای CNS یا کاهش عملکرد کلیوی بیشتر بروز می‌کند. ایمی‌پنم نباید در درمان مننژیت به کار رود. طیف فعالیت مروپنم مشابه با ایمی‌پنم است. برخلاف ایمی‌پنم، مروپنم در برابر آنزیم کلیوی دهیدروپپتیداز-1 پایدار است و نیازی به تجویز همزمان سیلاستاتین ندارد. ریسک بروز تشنج با مروپنم ممکن است تا حدی کمتر از ایمی‌پنم باشد. اشکال دارویی موجود در ایران به شرح ذیل است:\brایمی پنم-سیلاستاتین Powder for injection 250 mg/250 mg, 500 mg/500 mg, 750 mg/750 mg\brمروپنم Powder for injection 500 mg, 1 g",
                "options": [
                    "یک ویال 500/500 میلی گرم",
                    "یک ویال 250/250 میلی گرم",
                    "دو ویال 250/250 میلی گرم",
                    "نصف ویال 500/500 میلی گرم",
                    "نصف ویال 750/250 میلی گرم"
                ],
                "solution": [
                    "یک ویال 500/500 میلی گرم",
                    "دو ویال 250/250 میلی گرم"
                ],
                "explanation": "دوز ذکر شده برای ایمی‌پنم-سیلاستاتین در اندیکاسیون‌های درمانی آن، بر اساس جزء ایمی‌پنم تعریف شده است، نه مجموع ایمی‌پنم و سیلاستاتین. بنابراین، منظور از ایمی‌پنم 500 میلی‌گرم، ویال تزریقی ایمی‌پنم-سیلاستاتین mg 500/ mg 500 است. در صورت موجود نبودن این دوز، می توان از دو ویال mg250/mg250 ایمی پنم سیلاستاتین استفاده نمود."
            }
        ]
    },

    # --- Module 2 - Stage 2: Other Classes Formulations ---
    "q_dosage_stage_2": {
        "id": "q_dosage_stage_2",
        "title": "اشکال دارویی - سایر کلاس‌ها",
        "icon": "fa-pills",
        "description": "فلوروکینولون‌ها، ماکرولیدها، ضد ویروس‌ها و ضد قارچ‌ها",
        "questions": [
            {
                # Page 7: FQ Eye Drops
                "id": "q_fq_eyes",
                "type": "multiple-select",
                "title": "قطره‌های چشمی فلوروکینولون",
                "instruction": "کدام یک از داروهای فلوروکینولون زیر در بازار دارویی ایران شکل دارویی قطره چشمی دارند؟",
                "hint": "/images/questions/q_fq_table.jpg",
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
                "explanation":"سیپروفلوکساسین، لووفلوکساسین، موکسی فلوکساسین"
            },
            {
                # Page 8: Macrolides Forms
                "id": "q_macrolide_forms",
                "type": "drag-drop-match",
                "title": "اشکال دارویی ماکرولیدها",
                "instruction": "هر دارو را به شکل دارویی متناسب آن که در بازار دارویی ایران وجود دارد وصل کنید.",
                "hint": "/images/questions/m_table.jpg",
                "categories": [
                    {"id": "cat_clarith", "text": "کلاریترومایسین"},
                    {"id": "cat_azith", "text": "آزیترومایسین"},
                    {"id": "cat_eryth", "text": "اریترومایسین"}
                ],
                "items": [
                    {"id": "item_susp_125", "text": "سوسپانسیون 125mg/5ml"},
                    {"id": "item_susp_er", "text": "سوسپانسیون ER دو گرمی"},
                    {"id": "item_eye_drop", "text": "قطره چشمی 1 درصد"},
                    {"id": "item_inj_500", "text": "پودر تزریقی 500 میلی گرم"},
                    {"id": "item_topical", "text": "محلول موضعی 4 درصد"},
                    {"id": "item_eye_oint", "text": "پماد چشمی"},
                    {"id": "item_gel", "text": "ژل موضعی 2 درصد"}
                ],
                "solution": {
                    "cat_clarith": ["item_susp_125"],
                    "cat_azith": ["item_susp_er", "item_eye_drop", "item_inj_500"],
                    "cat_eryth": ["item_topical", "item_eye_oint", "item_gel"]
                },
                "explanation": "کلاریترومایسین - سوسپانسیون 125mg/5ml / آزیترومایسین - سوسپانسیون ER دو گرمی، قطره چشمی 1 درصد، پودر تزریقی 500 میلی گرم / اریترومایسین - محلول موضعی 4 درصد، پماد چشمی، ژل موضعی 2 درصد"
            },
            {
                # Page 9: Nitrofurantoin
                "id": "q_nitro_forms",
                "type": "drag-drop-match",
                "title": "فرمولاسیون‌های نیتروفورانتوئین",
                "instruction": "هر خصوصیت را به فرمولاسیون مربوطه (ماکروکریستال یا مونوهیدرات ماکروکریستال) وصل کنید.",
                "hint": "از نیتروفورانتوئین برای درمان و پروفیلاکسی عفونت‌های ادراری غیرعارضه‌دار استفاده می‌شود. این آنتی‌بیوتیک بر علیه بسیاری از میکروارگانیسم‌های گرم-مثبت و گرم-منفی مؤثر است. نیتروفورانتوئین در ادرار تغلیظ می‌شود، اما غلظت سرمی پایینی دارد و بر فلور نرمال روده تأثیر منفی قابل توجهی ندارد. دوزینگ بهینه این دارو در درمان عفونت‌های ادراری مشخص نیست، زیرا این دارو زمانی مورد تأیید قرار گرفت که روش‌ها و مقررات کنونی توسعه داروهای جدید مورد استفاده قرار نمی‌گرفتند. نیتروفورانتوئین در نارسایی کبدی نیازی به تعدیل دوز ندارد، اما بر اساس توصیه شرکت سازنده، استفاده از این دارو در نارسایی کلیوی با کلیرانس کراتینین کمتر از ml/min 60 ممنوع است. با این وجود، اطلاعات محدودی در دسترس است که نشان دهنده ایمنی استفاده از آن در کلیرانیس کراتینین ml/min 30-60 است.",
                "categories": [
                    {"id": "cat_macro", "text": "ماکروکریستال"},
                    {"id": "cat_mono", "text": "مونوهیدرات ماکروکریستال"}
                ],
                "items": [
                    {"id": "i_dose_4", "text": "دوزینگ چهار بار در روز"},
                    {"id": "i_slow_diss", "text": "انحلال کند در معده"},
                    {"id": "i_dose_2", "text": "دوزینگ دو بار در روز"},
                    {"id": "i_gel", "text": "تشکیل ژل در معده و آزادسازی طولانی"},
                    {"id": "i_less_gi", "text": "عوارض گوارشی کمتر"}
                ],
                "solution": {
                    "cat_macro": ["i_dose_4", "i_slow_diss"],
                    "cat_mono": ["i_dose_2", "i_gel", "i_less_gi"]
                },
                "explanation": "دو نوع فرآورده از نیتروفورانتوئین در بازار دارویی دنیا وجود دارد. فرمولاسیون اول، صرفاً از ماکروکریستال‌های نیتروفورانتوئین تشکیل شده است که با دوز 100-50 میلی‌گرم 4 بار در روز استفاده می‌شود. قرص نیتروفورانتوئین که در حال حاضر در بازار دارویی ایران وجود دارد، از این نوع است. فرمولاسیون دوم، به صورت کپسول‌های 100 میلی‌گرمی نیتروفورانتوئین مونوهیدرات/ماکروکریستال است، که هر کپسول حاوی 25 میلی‌گرم نیتروفورانتوئین ماکروکریستال و 75 میلی‌گرم نیتروفورانتوئین مونوهیدرات است. از نظر مولکولی، انحلال و جذب فرم ماکروکریستال‌ کندتر از فرم مونوهیدرات است، اما فرم مونوهیدرات در تماس با اسید معده و محتویات روده، یک ماتریکس ژلی تشکیل می‌دهد که نیتروفورانتوئین را به مرور زمان و در بازه زمانی طولانی آزاد می‌کند. این فرمولاسیون با دوز 100 میلی‌گرم 2 بار در روز استفاده می‌شود. به منظور افزایش جذب و کاهش عوارض جانبی، نیتروفورانتوئین باید همراه با غذا استفاده شود."
            },
            {
                # Page 10: Antivirals
                "id": "q_antiviral_feat",
                "type": "drag-drop-match",
                "title": "ویژگی‌های آنتی ویروس‌ها",
                "instruction": "هر ویژگی را به داروی آنتی ویروس مربوطه موجود در بازار ایران وصل کنید.",
                "hint": "/images/questions/av_table.jpg",
                "categories": [
                    {"id": "cat_acy", "text": "اسیکلوویر"},
                    {"id": "cat_val", "text": "والاسیکلوویر"},
                    {"id": "cat_gan", "text": "گانسیکلوویر"},
                    {"id": "cat_valgan", "text": "والگانسیلوویر"}
                ],
                "items": [
                    {"id": "i_topical", "text": "کرم موضعی 5% و پماد چشمی 3%"},
                    {"id": "i_tabs", "text": "قرص های 500 و 1000 میلی گرم"},
                    {"id": "i_inj", "text": "تزریقی (استفاده از دستکش)"},
                    {"id": "i_prodrug", "text": "پیش دارو / درمان CMV"}
                ],
                "solution": {
                    "cat_acy": ["i_topical"],
                    "cat_val": ["i_tabs"],
                    "cat_gan": ["i_inj"],
                    "cat_valgan": ["i_prodrug"]
                },
                "explanation": "آمپول گانسیکلوویر فقط به صورت وریدی (طی 1 ساعت) قابل تجویز است. از آنجایی که pH محلول تهیه شده بالاست (حدود 11)، تزریق عضلانی یا زیرجلدی آن منجر به آسیب شدید بافتی می‌شود. همچنین در زمان آماده‌سازی و تزریق این فرآورده، باید از دستکش یکبار مصرف استفاده گردد تا محلول آماده‌سازی شده، تماسی با پوست یا غشاهای مخاطی نداشته باشد. در صورت تماس ناخواسته این محلول با پوست، موضع باید با آب و صابون به خوبی شسته شود و در صورت تماس با چشم، از آب شیر برای شستن چشم‌ها استفاده گردد."
            },
            {
                # Page 11: Antifungals
                "id": "q_azole_forms",
                "type": "drag-drop-match",
                "title": "اشکال دارویی ضدقارچ‌ها",
                "instruction": "هر داروی آزول ضد قارچ را به شکل دارویی خود در بازار دارویی ایران وصل کنید.",
                "hint": "/image/questions/af_table.jpg",
                "categories": [
                    {"id": "cat_keto", "text": "کتوکونازول"},
                    {"id": "cat_fluco", "text": "فلوکونازول"},
                    {"id": "cat_itra", "text": "ایتراکونازول"},
                    {"id": "cat_vori", "text": "وریکونازول"},
                    {"id": "cat_posa", "text": "پوساکونازول"}
                ],
                "items": [
                    {"id": "i_sham", "text": "شامپو 2 درصد و قرص 200"},
                    {"id": "i_caps", "text": "کپسول 100 و 150 میلی گرم"},
                    {"id": "i_cap100", "text": "کپسول 100 میلی گرم"},
                    {"id": "i_tab50", "text": "قرص 50 و 200 میلی گرم"},
                    {"id": "i_amp", "text": "آمپول 300 میلی گرم"}
                ],
                "solution": {
                    "cat_keto": ["i_sham"],
                    "cat_fluco": ["i_caps"],
                    "cat_itra": ["i_cap100"],
                    "cat_vori": ["i_tab50"],
                    "cat_posa": ["i_amp"]
                },
                "explanation": "ایتراکونازول - کپسول 100 میلی گرم / کتوکونازول - شامپو 2 درصد و قرص 200 میلی گرم / فلوکونازول - کپسول 100 و 150 میلی گرم / وریکونازول - قرص 50 و 200 میلی گرم / پوساکونازول - آمپول 300 میلی گرم"
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
        "color": "#0288d1", 
        "levels": ["q_class_stage_1", "q_class_stage_2"]
    },
    {
        "id": "unit_2",
        "title": "Dosage Forms & Formulations",
        "description": "آشنایی با اشکال دارویی، دوزینگ و نکات فرمولاسیون آنتی‌بیوتیک‌ها در ایران",
        "color": "#009688",
        "levels": ["q_dosage_stage_1", "q_dosage_stage_2"]
    },
    {
        "id": "unit_3",
        "title": "Clinical Application",
        "description": "کاربردهای بالینی",
        "color": "#5e35b1",
        "levels": [] 
    }
]