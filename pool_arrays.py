from typing import List

# 📝 Ejercicio 3: Container With Most Water
# Contexto: Se te da un array de enteros height de longitud n. 
# Imagina n líneas verticales dibujadas de tal manera que los dos extremos de la línea i son (i, 0) y (i, height[i]).
# Debes encontrar dos líneas que, junto con el eje X, formen un contenedor tal que contenga la mayor cantidad de agua.

def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # 1. Calcular dimensiones actuales
        current_width = right - left
        # La altura del agua está limitada por la barra más corta
        current_height = min(height[left], height[right])
        
        # 2. Calcular área y actualizar el máximo si es necesario
        current_area = current_width * current_height
        max_water = max(max_water, current_area)
        
        # 3. Mover los punteros (Lógica Greedy)
        # Descartamos la barra más chica porque es la que nos limita.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

if __name__ == "__main__":
    # Caso de prueba del ejemplo
    heights = [1,8,6,2,5,4,8,3,7]
    result = max_area(heights)
    print(f"Max Water: {result}") # Esperado: 49