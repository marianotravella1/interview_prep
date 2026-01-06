# 📝 Ejercicio 5: Search Insert Position
# Contexto: Dado un array de enteros distintos ordenados y un valor objetivo (target), devuelve el índice si el objetivo se encuentra. 
# Si no, devuelve el índice donde debería insertarse para mantener el orden.

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid  
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

if __name__ == '__main__':
    print(search_insert([1, 3, 5, 6], 5)) 
    
    print(search_insert([1, 3, 5, 6], 2)) 
    
    print(search_insert([1, 3, 5, 6], 7))
    
    print(search_insert([1, 3, 5, 6], 0))