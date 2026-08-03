import os
import subprocess
import sys

def main():
    docs_dir = os.path.dirname(os.path.abspath(__file__))
    manual_md = os.path.join(docs_dir, "USER_MANUAL.md")
    manual_pdf = os.path.join(docs_dir, "USER_MANUAL.pdf")
    css_file = os.path.join(docs_dir, "style.css")

    if not os.path.exists(manual_md):
        print(f"Error: {manual_md} no existe.")
        sys.exit(1)

    print("📄 Generando USER_MANUAL.pdf con markdown-pdf...")
    cmd = ["markdown-pdf", "--css-path", css_file, manual_md]
    
    try:
        res = subprocess.run(cmd, cwd=docs_dir, check=True, capture_output=True, text=True)
        print("✅ USER_MANUAL.pdf generado exitosamente.")
    except Exception as e:
        print(f"❌ Error al compilar el PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
