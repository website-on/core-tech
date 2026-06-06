import re
import os

BASE_DIR = r"d:\ا كمال"

def get_template():
    with open(os.path.join(BASE_DIR, "coring.html"), "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split the file into Header, Main Content, and Footer
    header_split = content.split('<!-- Inner Hero Modern -->')
    footer_split = header_split[1].split('<!-- Dark Call-to-action Action -->')
    
    header = header_split[0]
    footer = '<!-- Dark Call-to-action Action -->' + footer_split[1]
    
    return header, footer

def save_page(filename, title, content_html, active_nav=""):
    header, footer = get_template()
    # update title
    header = re.sub(r'<title>.*?</title>', f'<title>{title} | Core-Tech مصر</title>', header, flags=re.DOTALL)
    # inject the content
    full_html = header + content_html + footer
    with open(os.path.join(BASE_DIR, filename), "w", encoding="utf-8") as f:
        f.write(full_html)
        
content_html_coring = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">خدمات الكور والتخريم</span>
            <h1>صنايعي كور وتخريم خرسانة بأقل سعر وأعلى جودة في مصر</h1>
            <p>لو بدور على صنايعي كور وتخريم خرسانة شاطر وسعره على الإيد، Core-Tech بتوفرلك أسرع وأدق خدمات عمل الفتحات الدائرية في الخرسانة المسلحة والطوب بأحدث ماكينات الكور الألمانية، من غير تكسير، ومن غير أي اهتزاز أو شروخ في السقف أو الحيطة، وبأقل تكلفة في السوق.</p>
        </div>
    </section>

    <!-- Service Overview -->
    <section class="service-overview">
        <div class="container overview-grid">
            <div class="overview-text">
                <h2>تطبيقات الخدمة (بنعمل إيه؟):</h2>
                <ul class="features-list">
                    <li><strong>فتحات التهوية والشفاطات:</strong> عمل فتحات بمقاسات مظبوطة ع الشعرة لشفاطات المطابخ والحمامات (الشفاط الطارد أو المروحة) وفتحات تهوية الغاز الطبيعي والمداخن.</li>
                    <li><strong>تأسيس السباكة والتكييف:</strong> عمل فتحات مواسير الصرف الصحي، التغذية، وتمديدات التكييف المركزي والـ Split.</li>
                    <li><strong>الكهرباء والحريق:</strong> فتح مسارات خراطيم الكهرباء وكابلات الباور وأنظمة إطفاء الحريق.</li>
                    <li><strong>اختبارات الخرسانة:</strong> أخذ عينات الكور (Concrete Cores) للمكاتب الاستشارية ومعامل اختبار جودة الخرسانة.</li>
                </ul>
            </div>
            <div class="overview-img">
                <img src="images/core_drilling.png" alt="آلة كور تخريم الخرسانة">
            </div>
        </div>
    </section>

    <!-- Service Features Cards -->
    <section class="service-features-cards">
        <div class="container">
            <div class="section-header">
                <h2>ليه تشتغل معانا؟</h2>
            </div>
            <div class="cards-grid">
                <div class="feature-card">
                    <i class="fas fa-money-bill-wave"></i>
                    <h3>أقل سعر في مصر</h3>
                    <p>بنقدم عروض أسعار تنافسية ومناسبة للمقاولين وأصحاب الشقق والمحلات.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-check-circle"></i>
                    <h3>شغل نضيف وع السكين</h3>
                    <p>الفتحة بتطلع دائرية ومستوية تماماً مش محتاجة ترميم وراها، وبنستخدم المية لمنع العفرة والتراب.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-ruler-combined"></i>
                    <h3>كل المقاسات موجودة</h3>
                    <p>فتحات بأقطار تبدأ من 1 بوصة وحتى الأقطار الكبيرة جداً للمشروعات، وبأي عمق مطلوب في أعتى خرسانة مسلحة.</p>
                </div>
            </div>
        </div>
    </section>
"""

content_html_sawing = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">خدمات القص بالمنشار</span>
            <h1>مقاول قص خرسانة بالمنشار الماسي بأقل تكلفة وأعلى دقة</h1>
            <p>لو محتاج تعديل في بيتك أو موقعك وتعبت من التكسير التقليدي، Core-Tech بتقدم لك الحل الأنظف والأسرع: قص الخرسانة المسلحة بالمنشار الماسي (القرص والسلك). بنقص لك الحوائط والأسقف والكمرات كأنك بتقطع بالمشرط، بدون أي اهتزازات خطيرة، وبسعر يناسب ميزانيتك.</p>
        </div>
    </section>

    <!-- Service Overview -->
    <section class="service-overview">
        <div class="container overview-grid">
            <div class="overview-text">
                <h2>تطبيقات الخدمة (بنعمل إيه بالمنشار؟):</h2>
                <ul class="features-list">
                    <li><strong>فتحات الأبواب والشبابيك:</strong> توسيع أو عمل فتحات جديدة للأبواب والنوافذ في الحوائط الخرسانية بسرعة وبشكل متساوي تماماً.</li>
                    <li><strong>فتحات المصاعد والسلم (الأسانسير):</strong> قص وتفريغ بلاطات الأسقف الخرسانية لعمل مسارات الأسانسير أو السلالم الداخلية.</li>
                    <li><strong>هدم وإزالة أجزاء إنشائية:</strong> إزالة وتقطيع الكمرات، الأعمدة، الكوابيل، والقواعد الخرسانية المخالفة.</li>
                    <li><strong>فواصل التمدد:</strong> عمل فواصل التمدد والهبوط في الأرضيات الخرسانية للمصانع، والمخازن بخطوط مستقيمة.</li>
                </ul>
            </div>
            <div class="overview-img">
                <img src="images/concrete_saw.png" alt="المنشار الخرساني">
            </div>
        </div>
    </section>

    <!-- Service Features Cards -->
    <section class="service-features-cards">
        <div class="container">
            <div class="section-header">
                <h2>مميزات الشغل معانا</h2>
            </div>
            <div class="cards-grid">
                <div class="feature-card">
                    <i class="fas fa-tags"></i>
                    <h3>أقل سعر للمتر</h3>
                    <p>بنوفر تكلفة الترميم والمحارة لأن السطح بيطلع ناعم ومستوي تماماً ومش محتاج تصليح وراه.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-shield-alt"></i>
                    <h3>أمان مطلق على المنشأ</h3>
                    <p>زيرو اهتزاز (Zero Vibration)، يعني مفيش أي خطورة من حدوث تصدعات أو شروخ في السقف.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-tachometer-alt"></i>
                    <h3>سرعة ونظافة في الموقع</h3>
                    <p>المنشار بيشتغل بتبريد المية، وده بيمنع غبار الخرسانة والتراب تماماً.</p>
                </div>
            </div>
        </div>
    </section>
"""

content_html_planting = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">خدمات تزريع الأشاير</span>
            <h1>متخصص تخريم وتزريع أشاير حديد الخرسانة اعلى جودة وأفضل سعر</h1>
            <p>في Core-Tech، بنوفر لك خدمة تخريم وتزريع أشاير الحديد والجاكيتات الخرسانية باستخدام أقوى المواد الكيميائية والإيبوكسية المعتمدة عالمياً عشان نضمن لك تماسك أقوى من الخرسانة نفسها، وبأسعار منافسة جداً.</p>
        </div>
    </section>

    <!-- Service Overview -->
    <section class="service-overview">
        <div class="container overview-grid">
            <div class="overview-text">
                <h2>تطبيقات الخدمة (بنعمل إيه في التزريع؟):</h2>
                <ul class="features-list">
                    <li><strong>تعلية الأدوار والتوسعات:</strong> زراعة أشاير الأعمدة والحوائط الخرسانية لاستكمال المباني وتعلية الأدوار بأمان.</li>
                    <li><strong>توسيع البلاطات والكمرات:</strong> تزريع حديد لتمديد السقف، عمل كوابيل، أو زيادة مساحة الغرف.</li>
                    <li><strong>تثبيت الجوايط والأنكورز:</strong> تثبيت الجوايط لتركيب الهناجر، المنشآت المعدنية، والماكينات والمعدات.</li>
                    <li><strong>قمصان الأعمدة والتدعيم:</strong> تخريم وتزريع أشاير لعمل جاكيتات لتقوية الأعمدة والقواعد الضعيفة.</li>
                </ul>
            </div>
            <div class="overview-img">
                <img src="https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg?auto=compress&cs=tinysrgb&w=800" alt="تزريع الأشاير">
            </div>
        </div>
    </section>

    <!-- Service Features Cards -->
    <section class="service-features-cards">
        <div class="container">
            <div class="section-header">
                <h2>خطوات الشغل المظبوطة عندنا و ليه تختارنا؟</h2>
            </div>
            <div class="cards-grid">
                <div class="feature-card">
                    <i class="fas fa-drafting-compass"></i>
                    <h3>التخريم بالعمق الهندسي</h3>
                    <p>بنخرم بالقطر والعمق المناسب لقطر السيخ بكفاءة عالية، حتى الأقطار الكبيرة 25 مم وأكتر.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-broom"></i>
                    <h3>نظافة الثقب ع الشعرة</h3>
                    <p>بننظف الحفرة تماماً بالبلاور والفرشاة السلكية من أي بودرة أو تراب عشان الإيبوكسي يمسك صح.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-syringe"></i>
                    <h3>حقن المادة الإيبوكسية</h3>
                    <p>بنحقن المادة المعتمدة بنسب مظبوطة ونثبت السيخ مع الالتزام بزمن الجفاف التام.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-thumbs-up"></i>
                    <h3>أقل تكلفة وأعلى جودة</h3>
                    <p>خبرة في اختيار المادة المناسبة للعمل (Hilti وغيرها) وبنوفر لك هدر في السعر للمتر أو لعدد الأشاير.</p>
                </div>
            </div>
        </div>
    </section>
"""

content_html_ventilation = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">خدمات الشفاطات والتهوية</span>
            <h1>تأسيس وتوريد وتركيب الشفاطات وأنظمة التهوية أعلى جودة وأفضل سعر</h1>
            <p>في Core-Tech، بنريحك من دوخة الصنايعية واللف على محلات المعدات. بنقدم لك خدمة متكاملة بنستلم منك المكان و بنسلمهولك في أفضل حالة تهوية وأعلى كفاءة سحب. بنبدأ معاك من أول خرم الكور في الخرسانة لحد ما تجرب الشفاط بنفسك.</p>
        </div>
    </section>

    <!-- Service Overview -->
    <section class="service-overview">
        <div class="container overview-grid">
            <div class="overview-text">
                <h2>خطوات الخدمة المتكاملة:</h2>
                <ul class="features-list">
                    <li><strong>المعاينة وتحديد المكان:</strong> بنيجي نعاين المكان ونحدد الأماكن الصح هندسياً لعمل الفتحات.</li>
                    <li><strong>عمل فتحة الكور النظيفة:</strong> بنخرم الفتحة بمقاس مظبوط ع الشعرة ومناسب لقطر المروحة.</li>
                    <li><strong>توريد أفضل خامات الشفاطات:</strong> بنوفر لك الشفاطات من أفضل الماركات الموثوقة وبأقوى محركات سحب.</li>
                    <li><strong>التركيب والتقفيل:</strong> بنركب الشفاط مع التثبيت المتين وعزل الفتحات كويس جداً لمنع تسريب المطر والحشرات.</li>
                </ul>
            </div>
            <div class="overview-img">
                <img src="https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=800" alt="تركيب شفاطات">
            </div>
        </div>
    </section>

    <!-- Service Features Cards -->
    <section class="service-features-cards">
        <div class="container">
            <div class="section-header">
                <h2>تطبيقات الخدمة و ليه تختارنا؟</h2>
            </div>
            <div class="cards-grid">
                <div class="feature-card">
                    <i class="fas fa-home"></i>
                    <h3>المنازل والفيلات والمطاعم</h3>
                    <p>تأسيس شفاطات المطابخ، الحمامات، وهود المطاعم وخطوط سحب الدخان والزيوت.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-industry"></i>
                    <h3>المصانع والمخازن</h3>
                    <p>عمل أنظمة تهوية للمساحات المغلقة لطرد الرطوبة وتجديد الهواء.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-key"></i>
                    <h3>خدمة على المفتاح</h3>
                    <p>مش هتحتاج تجيب صنايعي كور، وبعدين كهربائي، إنت بتتعامل مع جهة واحدة مسؤولة عن كل حاجة.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-percent"></i>
                    <h3>أسعار ملهاش منافس</h3>
                    <p>عشان بنوفر الخامات ونعمل الشغل بمعداتنا، بنقدم لك باقة سعرية شاملة أوفر بكتير من السوق.</p>
                </div>
            </div>
        </div>
    </section>
"""

content_html_about = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">من نحن</span>
            <h1>Core-Tech | رواد حلول التعديل الإنشائي وقص وتخريم الخرسانة في مصر</h1>
            <p>رؤيتنا: أن نكون الخيار الأول والـشريك الأكثر أماناً وموثوقية لكل من يبحث عن الجودة الفنية والسعر العادل في مجال التعديل الإنشائي وتأسيس التهوية في مصر.</p>
        </div>
    </section>

    <section class="service-overview">
        <div class="container">
            <div class="overview-text" style="max-width: 1000px; margin: 0 auto; text-align: center;">
                <h2>مهمتنا</h2>
                <p>Core-Tech هي منصة هندسية رائدة ومستقلة، متخصصة في تقديم أحدث الحلول والخدمات التقنية لقص وتخريم الخرسانة المسلحة وتزريع الأشاير وتأسيس أنظمة التهوية في مصر. تأسسنا برؤية واضحة هدفها استبدال طرق التكسير التقليدية (التي تشكل خطراً على سلامة المباني) بتقنيات حديثة وعالمية تضمن أعلى دقة هندسية، وأمان مطلق للمنشأ، وبأقل تكلفة في السوق.</p>
                <p>تحت إشراف إدارة كمال حسن، نجحنا في كسب ثقة مئات العملاء من أصحاب المنازل، والمقاولين، والمكاتب الاستشارية، بفضل التزامنا بتقديم شغل نظيف ع السكين، والتزامنا الصارم بالمواعيد.</p>
                <br>
                <h2>نطاق عملنا</h2>
                <p>نتشرف بخدمة عملائنا وتلبية طلباتهم بمعداتنا الحديثة في مختلف محافظات مصر، وجاهزون للمشروعات الكبيرة والصغيرة بنفس مستوى الاحترافية.</p>
            </div>
        </div>
    </section>
"""

content_html_projects = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">من أعمالنا</span>
            <h1>فخورون بخدمة كبرى المشروعات والمجتمعات العمرانية الجديدة في مصر</h1>
            <p>في Core-Tech، تخطت خدماتنا مجرد العمل التقليدي لنكون جزءاً من حركة البناء والتطوير في كبرى المدن والمشروعات القومية والسياحية في مصر.</p>
        </div>
    </section>

    <section class="service-features-cards">
        <div class="container">
            <div class="cards-grid">
                <div class="feature-card">
                    <i class="fas fa-city"></i>
                    <h3>مدينة الشيخ زايد و6 أكتوبر</h3>
                    <p>تنفيذ فتحات كور لتأسيس السباكة والتكييفات وقص حوائط بالمنشار الماسي לتعديلات معمارية في الفيلات بدون أي اهتزاز.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-building"></i>
                    <h3>التجمع الخامس والشروق والقاهرة الجديدة</h3>
                    <p>تخريم لعمل فتحات الشفاطات وتأسيس خطوط السحب وتزريع أشاير حديد للتعلية بمواد إيبوكسية معتمدة.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-landmark"></i>
                    <h3>العاصمة الإدارية الجديدة</h3>
                    <p>التعاون في تنفيذ أعمال قص وتخريم بالمنشار والكور في الأبراج الإدارية وأخذ عينات كور لاختبارات جودة الخرسانة.</p>
                </div>
                <div class="feature-card">
                    <i class="fas fa-umbrella-beach"></i>
                    <h3>العين السخنة</h3>
                    <p>أعمال تزريع الجوايط والأنكورز وتأسيس كامل لأنظمة التهوية للمطابخ بالفنادق والمطاعم الساحلية.</p>
                </div>
            </div>
        </div>
    </section>
"""

content_html_pricing = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">أسعار الخدمات</span>
            <h1>أسعار خدمات قص وتخريم الخرسانة وتزريع الأشاير في مصر | أقل تكلفة وأعلى جودة</h1>
            <p>في Core-Tech، بنحطم معادلة الأسعار المبالغ فيها. بنقدم لك أفضل أسعار لخدمات الكور والمنشار الماسي وتزريع الأشاير في مصر، مع الالتزام بمعايير الدقة والأمان الإنشائي.</p>
        </div>
    </section>

    <section class="service-overview">
        <div class="container">
            <div style="max-width: 1000px; margin: 0 auto;">
                <h2 style="text-align:center; margin-bottom:30px;">جدول الأسعار الاسترشادية</h2>
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; margin-bottom: 30px; text-align: right; background: #fff; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                        <thead>
                            <tr style="background: var(--dark-navy); color: #fff;">
                                <th style="padding: 15px; border: 1px solid #ddd;">الخدمة</th>
                                <th style="padding: 15px; border: 1px solid #ddd;">طريقة الحساب</th>
                                <th style="padding: 15px; border: 1px solid #ddd;">متوسط السعر</th>
                                <th style="padding: 15px; border: 1px solid #ddd;">ملاحظات</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 15px; border: 1px solid #ddd; font-weight: bold;">تخريم الخرسانة بالكور</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">بالفتحة (حسب القطر والسمك)</td>
                                <td style="padding: 15px; border: 1px solid #ddd; color: var(--primary); font-weight: bold;">تبدأ من أقل سعر للفتحة</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">تشمل فتحات الشفاطات، الغاز، السباكة، والتكييف.</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px; border: 1px solid #ddd; font-weight: bold;">قص الخرسانة بالمنشار الماسي</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">بالمتر الطولي</td>
                                <td style="padding: 15px; border: 1px solid #ddd; color: var(--primary); font-weight: bold;">أسعار تنافسية للمتر</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">لعمل فتحات الأبواب، الشبابيك، ومسارات الأسانسير.</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px; border: 1px solid #ddd; font-weight: bold;">تخريم وتزريع الأشاير</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">بالأشارة (حسب القطر ونوع المادة)</td>
                                <td style="padding: 15px; border: 1px solid #ddd; color: var(--primary); font-weight: bold;">أوفر سعر في مصر</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">نستخدم مواد إيبوكسية معتمدة (Hilti / كيماويات البناء).</td>
                            </tr>
                            <tr>
                                <td style="padding: 15px; border: 1px solid #ddd; font-weight: bold;">تأسيس وتركيب الشفاطات</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">باقة متكاملة</td>
                                <td style="padding: 15px; border: 1px solid #ddd; color: var(--primary); font-weight: bold;">على المفتاح</td>
                                <td style="padding: 15px; border: 1px solid #ddd;">باقة شاملة التوريد والتركيب والفنش.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div style="background: var(--light-grey); padding: 30px; border-radius: 8px;">
                    <h3>مميزات وعروض حصرية من Core-Tech:</h3>
                    <ul class="features-list">
                        <li><strong>خصومات للمشروعات الكبيرة:</strong> بنقدم أسعار خاصة جداً لشركات المقاولات والمشروعات التي تحتوي على كميات كبيرة.</li>
                        <li><strong>معاينة مجانية:</strong> للمشروعات الكبيرة في التجمع، زايد، أكتوبر، الشروق، العاصمة الإدارية، والسخنة.</li>
                        <li><strong>بدون تكاليف ترميم:</strong> بنوفر عليك الفلوس اللي كنت هتدفعها للمحارة والترميم ورا التكسير التقليدي لأن شغلنا "ع السكين".</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

content_html_blog = """
    <!-- Inner Hero Modern -->
    <section class="inner-hero-modern"
        style="background-image: url('https://images.pexels.com/photos/159306/construction-site-build-construction-work-159306.jpeg?auto=compress&cs=tinysrgb&w=1920');">
        <div class="container">
            <span class="badge">المدونة الهندسية</span>
            <h1>مقالات هندسية ونصائح في مجالات القص والتخريم</h1>
        </div>
    </section>

    <section class="service-overview blog-section">
        <div class="container">
            <div class="article-box" style="margin-bottom: 50px; padding-bottom: 30px; border-bottom: 1px solid #ddd;">
                <h2 style="color: var(--primary); margin-bottom: 15px;">ليه التكسير بالهيلتي خطر على بيتك؟ ومميزات قص وتخريم الخرسانة</h2>
                <h3>الخطر الخفي للتكسير التقليدي</h3>
                <p>التكسير التقليدي يعتمد على الصدمات المتتالية (Impact Loads). هذه الصدمات تولد موجات اهتزازية تنتقل عبر الخرسانة المسلحة، مما يؤدي إلى تفتيت قوى التماسك (Bond Slip) وتخلخل تماسك حديد التسليح وظهور الشروخ الدقيقة (Micro-cracks).</p>
                <h3>البديل الحديث</h3>
                <p>في Core-Tech، نعتمد على مفهوم زيرو اهتزاز (Zero Vibration) باستخدام الأسلحة الماسية (Diamond segments) التي تقطع الخرسانة والحديد معاً كالمشرط. نستخدم معدات كور لعمل ثقوب دائرية دقيقة بدون أي تأثير على القوة الإنشائية.</p>
            </div>

            <div class="article-box" style="margin-bottom: 50px; padding-bottom: 30px; border-bottom: 1px solid #ddd;">
                <h2 style="color: var(--primary); margin-bottom: 15px;">الأخطاء الكارثية في تزريع أشاير الحديد (كيف تضمن عدم ملوص السيخ؟)</h2>
                <h3>الخطوات القياسية للتزريع الصحيح</h3>
                <p>لتجنب فشل الإشارة (Pull-out failure)، نلتزم بالعمق الأدنى للتزريع (10d to 12d). نظافة الثقب خطوة حرجة جداً ونستخدم طريقة البلاور والفرشاة السلكية. نستخدم مواد معتمدة مثل Hilti RE 500 تُحقن من قاع الثقب لطرد أي هواء محبوس.</p>
            </div>

            <div class="article-box" style="margin-bottom: 50px; padding-bottom: 30px; border-bottom: 1px solid #ddd;">
                <h2 style="color: var(--primary); margin-bottom: 15px;">دليلك الشامل لتأسيس وتوريد وتركيب الشفاطات وأنظمة التهوية</h2>
                <h3>كيف تصمم منظومة تهوية احترافية؟</h3>
                <p>التهوية منظومة تكاملية. نعتمد على حسابات التهوية وتحديد قدرة السحب (CFM) وتغيير الهواء في الساعة (ACH). نستخدم الكور لعمل فتحات مطابقة لقطر الماسورة (Duct) وتأمين الفنش النهائي لمنع دخول المطر أو الحشرات باستخدام عزل الفوم والسيليكون.</p>
            </div>

            <div class="article-box">
                <h2 style="color: var(--primary); margin-bottom: 15px;">السلامة المهنية ونظافة الموقع في عمليات قص وتخريم الخرسانة</h2>
                <ul>
                    <li><strong>التدعيم الإنشائي πριν التعديل (Shoring):</strong> استخدام دعامات مؤقتة قبل القص بالمنشار لتجنب الانهيار أو الصدمة الديناميكية.</li>
                    <li><strong>التحكم في مياه التبريد (Slurry Control):</strong> استخدام أنظمة تجميع المياه لمنع تسربها للأدوار السفلية والمحافظة على النظافة.</li>
                    <li><strong>أدوات حماية الأفراد (PPE):</strong> التزام الفريق بالكامل بارتداء الخوذات ونظارات الأمان وسدادات الأذن وأحذية السلامة.</li>
                </ul>
            </div>
        </div>
    </section>
"""

save_page("coring.html", "تخريم الخرسانة بالكور", content_html_coring)
save_page("sawing.html", "قص الخرسانة بالمنشار", content_html_sawing)
save_page("planting.html", "تخريم وتزريع الأشاير", content_html_planting)
save_page("ventilation.html", "تأسيس الشفاطات والتهوية", content_html_ventilation)
save_page("about.html", "من نحن", content_html_about)
save_page("projects.html", "من أعمالنا", content_html_projects)
save_page("pricing.html", "أسعار الخدمات", content_html_pricing)
save_page("blog.html", "المدونة", content_html_blog)

print("HTML files successfully generated.")
