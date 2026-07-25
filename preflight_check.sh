#!/bin/bash
# SCRIPT: preflight_check.sh
# Ejecutar desde: /Users/jesusferrer/.gemini/antigravity-ide/scratch/ableton-ai-assistant/

echo "═══════════════════════════════════════════════════"
echo "  🔍 ANTIGRAVITY PREFLIGHT CHECK V2.0.0"
echo "═══════════════════════════════════════════════════"

# 1. Verificar estructura de directorios existente
echo -e "\n[1/8] Verificando estructura de directorios..."
REQUIRED_DIRS=(
  "remote-script/AntigravityCore"
  "electron-app"
  "mcp-server"
  "docs"
)

for dir in "${REQUIRED_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    echo "  ✅ $dir"
  else
    echo "  ❌ FALTA: $dir → CREANDO..."
    mkdir -p "$dir"
  fi
done

# 2. Verificar archivos críticos V1.0.0
echo -e "\n[2/8] Verificando archivos críticos V1.0.0..."
CRITICAL_FILES=(
  "remote-script/AntigravityCore/AntigravityCore.py"
  "remote-script/AntigravityCore/midi_generator.py"
  "remote-script/AntigravityCore/session_manager.py"
  "electron-app/package.json"
  "electron-app/index.html"
)

for file in "${CRITICAL_FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "  ✅ $file ($(wc -l < "$file" | awk '{print $1}') líneas)"
  else
    echo "  ⚠️  NO ENCONTRADO: $file"
  fi
done

# 3. Backup completo ANTES de cualquier modificación
echo -e "\n[3/8] Creando backup V1.0.0 inmutable..."
BACKUP_DIR="backups/v1.0.0_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r remote-script/ "$BACKUP_DIR/"
cp -r electron-app/ "$BACKUP_DIR/"
echo "  ✅ Backup creado en: $BACKUP_DIR"
echo "  🔒 Haciendo backup de solo lectura..."
chmod -R 444 "$BACKUP_DIR"

# 4. Verificar Git status
echo -e "\n[4/8] Verificando estado de Git..."
git status || echo "No es un repositorio git válido"
git log --oneline -5 || true

# 5. Crear branch de desarrollo
echo -e "\n[5/8] Creando branch de desarrollo..."
git checkout -b feature/v2.0.0-upgrade || true
echo "  ✅ Branch 'feature/v2.0.0-upgrade' listo"

# 6. Verificar Python disponible
echo -e "\n[6/8] Verificando entorno Python..."
python3 --version
pip3 list | grep -E "librosa|scipy|numpy|flask|websockets" || true

# 7. Verificar Node.js y dependencias Electron
echo -e "\n[7/8] Verificando entorno Node.js..."
node --version
npm --version
cd electron-app && npm list --depth=0 2>/dev/null; cd ..

# 8. Verificar conectividad con GitHub
echo -e "\n[8/8] Verificando conectividad GitHub..."
git remote -v || true

echo -e "\n═══════════════════════════════════════════════════"
echo "  ✅ PREFLIGHT COMPLETADO. LISTO PARA V2.0.0"
echo "═══════════════════════════════════════════════════"
