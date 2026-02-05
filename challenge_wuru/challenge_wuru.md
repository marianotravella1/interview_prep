# Challenge Técnico - Sistema de Inventario
 
## Tiempo: 45 minutos
 
### Contexto
Una tienda online necesita un sistema para gestionar su inventario de productos. El sistema debe permitir controlar stock, procesar ventas y generar reportes básicos.
 
## Requerimientos
 
### Funcionalidades Básicas
El sistema debe permitir:
 
1. ✅ **Agregar productos** con código, nombre, precio y cantidad inicial
2. ✅ **Actualizar stock** cuando llegue mercadería
3. ✅ **Procesar ventas** (reducir stock)
4. ✅ **Consultar disponibilidad** de productos
5. ✅ **Generar reporte** de productos con bajo stock
6. ✅ **Calcular valor total** del inventario
 
### Estructura Inicial
 
Implementa las siguientes clases:
 
```python
class Product:
    def __init__(self, code: str, name: str, price: float, initial_stock: int = 0):
        # Tu código aquí
        pass
    def add_stock(self, quantity: int):
        # Tu código aquí
        pass
    def remove_stock(self, quantity: int) -> bool:
        # Tu código aquí
        pass
    def is_available(self) -> bool:
        # Tu código aquí
        pass
    def get_total_value(self) -> float:
        # Tu código aquí
        pass
 
class Inventory:
    def __init__(self):
        # Tu código aquí
        pass
    def add_product(self, product: Product):
        # Tu código aquí
        pass
    def get_product(self, code: str) -> Product:
        # Tu código aquí
        pass
    def process_sale(self, code: str, quantity: int) -> bool:
        # Tu código aquí
        pass
    def get_low_stock_products(self, threshold: int = 5) -> list:
        # Tu código aquí
        pass
    def get_available_products(self) -> list:
        # Tu código aquí
        pass
```
 
## Validaciones Esperadas
 
- Los códigos de productos deben ser únicos
- No se puede tener stock negativo
- Los precios deben ser positivos
- No se pueden procesar ventas de productos inexistentes
- Las cantidades deben ser números enteros positivos
 
## Reglas de Negocio
 
1. **Stock mínimo**: Un producto se considera "bajo stock" si tiene 5 o menos unidades (configurable)
2. **Ventas**: Solo se puede vender si hay stock suficiente
3. **Disponibilidad**: Un producto está disponible si stock > 0
4. **Valor**: El valor de un producto es precio × stock actual