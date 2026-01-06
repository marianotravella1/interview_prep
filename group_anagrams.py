from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Usaremos un defaultdict para evitar verificar si la clave existe
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Paso crucial: Ordenar la palabra. 
        # sorted(word) devuelve una lista ['a', 'e', 't'], 
        # así que uso join para volver a hacerlo string o tupla para que sea hashable.
        sorted_word = "".join(sorted(word))
        
        # Agrego la palabra original a la lista correspondiente a esa clave
        anagram_map[sorted_word].append(word)
    
    # Retornamos solo los grupos (los valores del diccionario)
    return list(anagram_map.values())

if __name__ == "__main__":
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    resultado = group_anagrams(input_data)
    
    print("Input:", input_data)
    print("Resultado:", resultado)