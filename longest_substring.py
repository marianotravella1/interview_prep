# 📝 Ejercicio 4: Longest Substring Without Repeating Characters
# Contexto: Dada una cadena s, encuentra la longitud de la subcadena más larga que no tenga caracteres repetidos.

def longest_substring_optimized(s: str) -> int:
    # Usamos un Set para búsquedas O(1) instantáneas
    char_set = set()
    left = 0
    max_len = 0
    
    # 'right' se mueve automáticamente paso a paso
    for right in range(len(s)):
        # Si encontramos un duplicado, NO reiniciamos 'right'.
        # En su lugar, encogemos la ventana desde la IZQUIERDA
        # hasta eliminar el culpable.
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Ahora que es seguro (no hay duplicados), agregamos el nuevo char
        char_set.add(s[right])
        
        # Calculamos el tamaño actual de la ventana
        current_len = right - left + 1
        max_len = max(max_len, current_len)
        
    return max_len

if __name__ == "__main__":
    string = "aaawefwfwefadiedaaak"
    result = longest_substring_optimized(string)
    print(f"Longitud máxima: {result}") 
    # Debería dar 5 (por "adied" -> "adiek" no, espera... "fadied" tiene 6? 
    # Veamos: "aaa"->1, "wef"->3, "wfw"->2...
    # En "fadied", la d se repite.
    # El string "wefadiedaaak": "wefad" (5).