def has_valid_bracing(s: str) -> bool:
    # Stack para guardar los caracteres de apertura
    stack = []
    
    # Mapeo: Llave = Cierre, Valor = Apertura correspondiente
    # Esto elimina la necesidad de múltiples ifs o switch
    close_to_open = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    
    # string = '[][{}}{})()]'
    
    # stack = ['[']
    
    for char in s:
        # 1. Si el caracter es un cierre (está en las llaves del dict)
        if char in close_to_open:
            # Verificamos dos cosas:
            # a) Que la pila no esté vacía (hay algo que cerrar?)
            # b) Que el tope de la pila sea la apertura correcta
            if stack and stack[-1] == close_to_open[char]:
                stack.pop() # Coinciden, sacamos el de apertura de la pila
            else:
                return False # No coinciden o pila vacía
        
        # 2. Si es una apertura, simplemente lo guardamos
        else:
            stack.append(char)
            
    # 3. Al final, True solo si la pila quedó vacía (todo se cerró)
    return stack == []

if __name__ == '__main__':
    # Caso Falso
    test_fail = "([)]" 
    print(f"Test '{test_fail}': {has_valid_bracing(test_fail)}")
    
    # Caso correcto
    test_ok = "{[][()]}"
    
    print(f"Test '{test_ok}': {has_valid_bracing(test_ok)}") # Debería ser True