# -*- coding: utf-8 -*-
"""
Programa de Inventario
---------------------

Este programa gestiona un inventario de productos. Permite agregar, eliminar,
actualizar y consultar productos.

Funciones:
---------
* `agregar_producto(inventario, nombre, cantidad, precio)`: Agrega un producto al inventario.
* `eliminar_producto(inventario, nombre)`: Elimina un producto del inventario.
* `actualizar_producto(inventario, nombre, cantidad=None, precio=None)`: Actualiza la cantidad y/o el precio de un producto.
* `consultar_producto(inventario, nombre)`: Consulta un producto en el inventario.
* `listar_inventario(inventario)`: Lista todos los productos en el inventario.
* `calcular_valor_total(inventario)`: Calcula el valor total del inventario.
* `main()`: Función principal que ejecuta el programa.

Variables:
---------
* `inventario`: Un diccionario que almacena los productos. La clave es el nombre del producto y el valor es un diccionario con la cantidad y el precio.
"""

def agregar_producto(inventario, nombre, cantidad, precio):
    """
    Agrega un producto al inventario.

    Args:
        inventario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto.
        cantidad (int): La cantidad del producto.
        precio (float): El precio del producto.

    Raises:
        ValueError: Si la cantidad o el precio son inválidos.
        KeyError: Si el producto ya existe en el inventario.
    """
    if cantidad < 0 or precio < 0:
        raise ValueError("La cantidad y el precio deben ser valores no negativos.")
    if nombre in inventario:
        raise KeyError(f"El producto '{nombre}' ya existe en el inventario.")
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print(f"Producto '{nombre}' agregado al inventario.")

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Args:
        inventario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto a eliminar.

    Raises:
        KeyError: Si el producto no existe en el inventario.
    """
    if nombre not in inventario:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
    del inventario[nombre]
    print(f"Producto '{nombre}' eliminado del inventario.")

def actualizar_producto(inventario, nombre, cantidad=None, precio=None):
    """
    Actualiza la cantidad y/o el precio de un producto.

    Args:
        inventario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto a actualizar.
        cantidad (int, opcional): La nueva cantidad del producto. Si es None, no se actualiza.
        precio (float, opcional): El nuevo precio del producto. Si es None, no se actualiza.

    Raises:
        ValueError: Si la cantidad o el precio son inválidos.
        KeyError: Si el producto no existe en el inventario.
    """
    if nombre not in inventario:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
    if cantidad is not None:
        if cantidad < 0:
            raise ValueError("La cantidad debe ser un valor no negativo.")
        inventario[nombre]['cantidad'] = cantidad
    if precio is not None:
        if precio < 0:
            raise ValueError("El precio debe ser un valor no negativo.")
        inventario[nombre]['precio'] = precio
    print(f"Producto '{nombre}' actualizado en el inventario.")

def consultar_producto(inventario, nombre):
    """
    Consulta un producto en el inventario.

    Args:
        inventario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto a consultar.

    Returns:
        dict: Un diccionario con la cantidad y el precio del producto.

    Raises:
        KeyError: Si el producto no existe en el inventario.
    """
    if nombre not in inventario:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
    return inventario[nombre]

def listar_inventario(inventario):
    """
    Lista todos los productos en el inventario.

    Args:
        inventario (dict): El diccionario que representa el inventario.

    Returns:
        None: Imprime la lista de productos en el inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")
    for nombre, detalles in inventario.items():
        cantidad = detalles['cantidad']
        precio = detalles['precio']
        print(f"- {nombre}: Cantidad = {cantidad}, Precio = ${precio:.2f}")

def calcular_valor_total(inventario):
    """
    Calcula el valor total del inventario.

    Args:
        inventario (dict): El diccionario que representa el inventario.

    Returns:
        float: El valor total del inventario.
    """
    valor_total = 0
    for detalles in inventario.values():
        valor_total += detalles['cantidad'] * detalles['precio']
    return valor_total

def main():
    """
    Función principal que ejecuta el programa.
    """
    inventario = {}
    while True:
        print("\n--- Programa de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Consultar producto")
        print("5. Listar inventario")
        print("6. Calcular valor total del inventario")
        print("7. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        try:
            if opcion == '1':
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                agregar_producto(inventario, nombre, cantidad, precio)
            elif opcion == '2':
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                eliminar_producto(inventario, nombre)
            elif opcion == '3':
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                cantidad_str = input("Ingrese la nueva cantidad (o deje en blanco para no cambiar): ")
                precio_str = input("Ingrese el nuevo precio (o deje en blanco para no cambiar): ")
                cantidad = int(cantidad_str) if cantidad_str else None
                precio = float(precio_str) if precio_str else None
                actualizar_producto(inventario, nombre, cantidad, precio)
            elif opcion == '4':
                nombre = input("Ingrese el nombre del producto a consultar: ")
                producto = consultar_producto(inventario, nombre)
                print(f"Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
            elif opcion == '5':
                listar_inventario(inventario)
            elif opcion == '6':
                valor_total = calcular_valor_total(inventario)
                print(f"El valor total del inventario es: ${valor_total:.2f}")
            elif opcion == '7':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 7.")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
