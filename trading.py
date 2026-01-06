
# 📝 Ejercicio 6: Best Time to Buy and Sell Stock
# Contexto: Se te da un array prices donde prices[i] es el precio de una acción dada en el día i. 
# Quieres maximizar tu ganancia eligiendo un solo día para comprar una acción y elegir un día diferente en el futuro para venderla.

from typing import List

def max_profit(prices: List[int]) -> int:
    # Inicializamos el precio mínimo en infinito para asegurar 
    # que el primer precio del array lo reemplace.
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Caso 1: Encontramos un precio de compra más barato
        if price < min_price:
            min_price = price
        
        # Caso 2: Vemos si vendiendo hoy obtenemos mejor ganancia
        # que nuestro récord anterior
        elif (price - min_price) > max_profit:
            max_profit = price - min_price
            
    return max_profit

if __name__ == "__main__":
    # Ejemplo 1: Caso normal
    prices = [7, 1, 5, 3, 6, 4,9]
    print(f"Ganancia: {max_profit(prices)}") 
    # Esperado: 5 (Compra a 1, Vende a 6)

    # Ejemplo 2: Mercado en bajada
    prices_down = [7, 6, 4, 3, 1]
    print(f"Ganancia: {max_profit(prices_down)}") 
    # Esperado: 0 (No conviene comprar nunca)