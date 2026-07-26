import os

header = """<div class="header-container">
  <img src="icon.png" width="200" height="200" style="border-radius: 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.15);" alt="Ableton AI Assistant Logo" />
  <h1>Ableton AI Assistant V1.0.0</h1>
  <h2>Official User Manual / Manual de Usuario Maestro</h2>
</div>

<p align="center">
  <img src="screenshot-UI.png" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.6);" alt="Ableton AI Assistant Console" />
</p>

<div class="page-break"></div>
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
        content = f.read()
    
    # Fix paths
    content = content.replace("docs/screenshot-UI.png", "screenshot-UI.png")
    content = content.replace("docs/USER_MANUAL.pdf", "USER_MANUAL.pdf")
    
    # Limpiar el header de los READMEs para no duplicar logos ni badges
    # Buscamos la primera línea "---"
    parts = content.split("---", 1)
    if len(parts) >= 2:
        # El cuerpo real empieza en el índice 1
        body = parts[1].strip()
    else:
        body = content
        
    manual_content += f"### {title} ({code})\n\n"
    manual_content += body
    
    if idx < len(languages) - 1:
        manual_content += "\n\n<div class=\"page-break\"></div>\n\n"
        
with open("USER_MANUAL.md", "w", encoding="utf-8") as f:
    f.write(manual_content)
