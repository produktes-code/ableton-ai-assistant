from pathlib import Path
import os

STRANGE = Path("/Volumes/Strange/repositorios/ableton-ai-assistant")
REPO = Path("/Users/jesusferrer/.gemini/antigravity-ide/scratch/ableton-ai-assistant")

archivos_repo = list(REPO.rglob("*.py")) + \
                list(REPO.rglob("*.js")) + \
                list(REPO.rglob("*.html")) + \
                list(REPO.rglob("*.css")) + \
                list(REPO.rglob("*.yml")) + \
                list(REPO.rglob("*.md"))

archivos_repo = [f for f in archivos_repo
                 if '.git' not in str(f)
                 and 'node_modules' not in str(f)
                 and 'dist' not in str(f)]

total = len(archivos_repo)
sincronizados = 0
diferentes = []

for f in archivos_repo:
    rel = f.relative_to(REPO)
    strange_f = STRANGE / rel
    if strange_f.exists():
        if f.stat().st_size == strange_f.stat().st_size:
            sincronizados += 1
        else:
            diferentes.append(str(rel))
    else:
        diferentes.append(f"FALTA: {rel}")

print(f"Total archivos repo: {total}")
print(f"Sincronizados 1:1: {sincronizados}")
print(f"Diferencias: {len(diferentes)}")
if diferentes:
    for d in diferentes[:10]:
        print(f"  - {d}")

if len(diferentes) > 0:
    print("EJECUTAR rsync para sincronizar")
else:
    print("STRANGE: PERFECTO 1:1")
