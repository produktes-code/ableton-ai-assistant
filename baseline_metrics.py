import os
import ast
from collections import defaultdict

def analyze_codebase(directory):
    stats = defaultdict(int)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    stats['python_files'] += 1
                    stats['total_lines'] += len(content.splitlines())
                    
                    try:
                        tree = ast.parse(content)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                stats['functions'] += 1
                            elif isinstance(node, ast.ClassDef):
                                stats['classes'] += 1
                    except Exception as e:
                        print(f"Error parseando {file}: {e}")
    
    print("\n📊 MÉTRICAS BASE V1.0.0 (Python)")
    for k, v in stats.items():
        print(f"  - {k.capitalize()}: {v}")

if __name__ == "__main__":
    analyze_codebase("./remote-script")
