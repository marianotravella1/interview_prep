"""
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

ej de producto:

prod1: Product = {
    code = 'SP20035'
    name = 'Samsung S25'
    price = 1250000.00
    stock = 35
}

"""


class Product:
    def __init__(self, code: str, name: str, price: float, initial_stock: int = 0):
        if price < 0: raise ValueError("El precio no puede ser negativo")
        if initial_stock < 0: raise ValueError("El stock inicial no puede ser negativo")
        
        self.code = code
        self.name = name
        self.price = price
        self.stock = initial_stock

    def add_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva")
        self.stock += quantity

    def remove_stock(self, quantity: int) -> bool:
        if quantity <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def is_available(self) -> bool:
        return self.stock > 0

    def get_total_value(self) -> float:
        return self.stock * self.price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if product.code in self.products:
            raise ValueError(f"El producto {product.code} ya existe")
        self.products[product.code] = product

    def get_product(self, code: str) -> Product:
        if code not in self.products:
            raise KeyError(f"Producto {code} no encontrado")
        return self.products[code]

    def process_sale(self, code: str, quantity: int) -> bool:
        product = self.products.get(code)
        if not product:
            print(f"Error: Producto {code} no encontrado") 
            return False

        success = product.remove_stock(quantity)
        
        if success:
            print(f"Venta exitosa: {quantity} unidades de {product.name}")
        else:
            print(f"Error: Stock insuficiente de {product.name} (Stock: {product.stock})")
            
        return success

    def get_low_stock_products(self, threshold: int = 5) -> list[Product]:
        return [p for p in self.products.values() if p.stock <= threshold]

    def get_total_inventory_value(self) -> float:
        return sum(p.get_total_value() for p in self.products.values())


if __name__ == "__main__":
    try:
        inventory = Inventory()

        p1 = Product("P001", "Laptop", 1000.0, 10)
        p2 = Product("P002", "Mouse", 25.0, 50)
        p3 = Product("P003", "Keyboard", 45.0, 3)

        inventory.add_product(p1)
        inventory.add_product(p2)
        inventory.add_product(p3)

        inventory.process_sale("P001", 2)
        
        inventory.process_sale("P003", 5) 

        print("\n--- Productos con stock bajo ---")
        for p in inventory.get_low_stock_products(5):
            print(f"- {p.name}: {p.stock}")

        print(f"\nValor total: ${inventory.get_total_inventory_value():.2f}")

    except ValueError as e:
        print(f"Error de validación: {e}")


if __name__ == "__main__":
    inventory = Inventory()

    p1 = Product(code="P001", name="Laptop", price=1000.0, initial_stock=10)
    p2 = Product(code="P002", name="Mouse", price=25.0, initial_stock=50)
    p3 = Product(code="P003", name="Keyboard", price=45.0, initial_stock=3)

    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    inventory.process_sale("P001", 2)
    inventory.process_sale("P003", 1)

    low_stock = inventory.get_low_stock_products()
    print("Low stock products:")
    for product in low_stock:
        print(f"{product.name} (Code: {product.code}, Stock: {product.stock})")

    total_value = inventory.get_total_inventory_value()
    print(f"Total inventory value: ${total_value:.2f}")
