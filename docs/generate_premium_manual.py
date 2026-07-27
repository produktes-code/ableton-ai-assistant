import os
import re

header = """<div style="text-align: center; margin-bottom: 2em;">

![Ableton AI Assistant Logo](screenshot-UI.png)

</div>

<h1>Ableton AI Assistant - Manual de Usuario / User Manual</h1>
<h5>Official Documentation & Technical Guide</h5>
<hr/>

### Keywords de Seguridad

`CERTIFIED`, `RETAIL-READY`, `Rate limiting`, `Magic Bytes`, `2 GB`, `7 idiomas`, `CC BY-NC-SA 4.0`

"""

languages = [
    ("ES", "🇪🇸 Español", "README_es.md"),
    ("EN", "🇬🇧 English", "README.md"),
    ("DE", "🇩🇪 Deutsch", "README_de.md"),
    ("RU", "🇷🇺 Русский", "README_ru.md"),
    ("JA", "🇯🇵 日本語", "README_ja.md"),
    ("UK", "🇺🇦 Українська", "README_uk.md"),
    ("ZH", "🇨🇳 中文", "README_zh.md")
]

manual_content = header

for idx, (code, title, filename) in enumerate(languages):
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
    
    # Arreglar paths
    body = body.replace("docs/screenshot-UI.png", "screenshot-UI.png")
    
    # Reemplazar encabezados H2 por H4 para que no choquen con el CSS, excepto los que queremos como H3 o H4
    # En el CSS H3 es el bloque purpura. H4 es texto normal negrita.
    body = body.replace("## ", "#### ")
    
    manual_content += f"\n\n### {title} ({code})\n\n"
    manual_content += body
    
    if idx < len(languages) - 1:
        manual_content += "\n\n<div class=\"page-break\"></div>\n\n"
        
with open("USER_MANUAL.md", "w", encoding="utf-8") as f:
    f.write(manual_content)
