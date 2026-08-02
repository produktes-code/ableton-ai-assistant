import os
import re

header = """![Ableton AI Assistant Logo](../build/icon.png)

# Ableton AI Assistant - Manual de Usuario / User Manual

*Official Documentation & Technical Guide*

---

![Ableton AI Assistant UI](../docs/screenshot-UI.png)

### Keywords de Seguridad

`CERTIFIED`, `RETAIL-READY`, `Rate limiting`, `Magic Bytes`, `2 GB`, `7 idiomas`, `CC BY-NC-SA 4.0`

"""

# country codes for flagcdn (lowercase)
languages = [
    ("ES", "es", "Español", "README_es.md"),
    ("EN", "gb", "English", "README.md"),
    ("DE", "de", "Deutsch", "README_de.md"),
    ("RU", "ru", "Русский", "README_ru.md"),
    ("JA", "jp", "日本語", "README_ja.md"),
    ("UK", "ua", "Українська", "README_uk.md"),
    ("ZH", "cn", "中文", "README_zh.md")
]

manual_content = header

for idx, (code, flag_code, title, filename) in enumerate(languages):
    with open(f"../{filename}", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Encontrar dónde empieza el contenido real usando la diana (## 🎯)
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("## 🎯"):
            start_idx = i
            break
            
    body = "".join(lines[start_idx:]).strip()
    
    # Limpiar las URLs locales a los archivos de github o pdfs (las quitamos del manual)
    body = re.sub(r'\[(.*?)\]\([^)]+\.md\)', r'\1', body) # quita links a otros md
    body = re.sub(r'\[(.*?)\]\([^)]+\.pdf\)', r'\1', body) # quita links a pdfs
    
    # Reemplazar encabezados H2 por H4 para que no choquen con el CSS, excepto los que queremos como H3 o H4
    # En el CSS H3 es el bloque purpura. H4 es texto normal negrita.
    body = body.replace("## ", "#### ")
    
    # Inject flag image using flagcdn
    flag_md = f"![{code}](https://flagcdn.com/h24/{flag_code}.png)"
    
    manual_content += f"\n\n### {flag_md} {title} ({code})\n\n"
    manual_content += body
    
    if idx < len(languages) - 1:
        manual_content += "\n\n---\n\n"
        
with open("USER_MANUAL.md", "w", encoding="utf-8") as f:
    f.write(manual_content)
