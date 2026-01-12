import os
import sys

def create_problem(problem_name):
    # Convertimos "Two Sum" a "two_sum" y limpiamos caracteres
    folder_name = problem_name.strip().lower().replace(" ", "_").replace("-", "_")
    
    # Ruta base (ajusta si tu estructura es diferente)
    base_path = os.path.join(os.getcwd(), "problems", folder_name)
    
    if os.path.exists(base_path):
        print(f"⚠️  El problema '{folder_name}' ya existe.")
        return

    # Crear carpeta
    os.makedirs(base_path)
    
    # Crear archivo solution.py con un template básico
    file_path = os.path.join(base_path, "solution.py")
    template = f'''"""
LeetCode Problem: {problem_name}
Link: [Pegar link aquí]
"""


class Solution:
    def {folder_name}(self) -> :
'''
    
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(template)
        
    print(f"✅ Carpeta y archivo creados en: problems/{folder_name}/solution.py")
    print("🚀 ¡A codear!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/new.py \"Nombre Del Problema\"")
    else:
        create_problem(sys.argv[1])