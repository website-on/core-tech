import os
import glob
import re

schema_script = """    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "https://yourdomain.com/#website",
          "url": "https://yourdomain.com/",
          "name": "كورتك لخدمات الخرسانة والكور | إدارة كمال حسن",
          "description": "شركة Core-Tech للخدمات الخرسانية بمصر، متخصصون في تخريم الكور، قص الخرسانة بالمنشار الماسي، تزريع الأشاير، وتأسيس الشفاطات بأعلى جودة وبدون اهتزاز.",
          "publisher": {
            "@id": "https://yourdomain.com/#organization"
          }
        },
        {
          "@type": "Organization",
          "@id": "https://yourdomain.com/#organization",
          "name": "كورتك للخدمات الخرسانية",
          "alternateName": "Core-Tech",
          "url": "https://yourdomain.com/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://yourdomain.com/images/favicon.jpg"
          },
          "contactPoint": [
            {
              "@type": "ContactPoint",
              "telephone": "+201018452092",
              "contactType": "customer service",
              "availableLanguage": "Arabic"
            },
            {
              "@type": "ContactPoint",
              "telephone": "+201129114377",
              "contactType": "WhatsApp",
              "availableLanguage": "Arabic"
            }
          ]
        },
        {
          "@type": "Service",
          "name": "تخريم الكور",
          "provider": {
            "@id": "https://yourdomain.com/#organization"
          },
          "description": "عمل فتحات الخرسانة بالكور بأسطوانات الماس."
        },
        {
          "@type": "Service",
          "name": "قص الخرسانة",
          "provider": {
            "@id": "https://yourdomain.com/#organization"
          },
          "description": "قص الخرسانة وتفتيحها بالمنشار الجداري الماسي."
        },
        {
          "@type": "Service",
          "name": "تأسيس وتركيب الشفاطات",
          "provider": {
            "@id": "https://yourdomain.com/#organization"
          },
          "description": "حلول التهوية المعمارية وعمل الفتحات للشفاطات."
        },
        {
          "@type": "Service",
          "name": "تخريم وتزريع الأشاير",
          "provider": {
            "@id": "https://yourdomain.com/#organization"
          },
          "description": "تخريم وتزريع الأشاير الايبوكسية لربط العناصر الإنشائية بكفاءة عظمى."
        }
      ]
    }
    </script>
</head>"""

html_files = glob.glob('*.html')
for file in html_files:
    if "google" in file:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "<!-- Schema Markup -->" not in content:
        content = content.replace("</head>", schema_script)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added schema to {file}")
    else:
        print(f"Schema already in {file}")
