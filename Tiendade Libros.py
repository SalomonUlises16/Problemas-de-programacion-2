# Lista de libros y precios como tuplas
catalogo = [
    ("El Principito", 150),
    ("1984", 200),
    ("Cien años de soledad", 250),
    ("Fahrenheit 451", 180),
    ("Matar a un ruiseñor", 220)
]

# Bucle para repetir la compra si el usuario lo desea
continuar_compra = "sí"

while continuar_compra.lower() == "sí":
    print("\nBienvenido a la tienda de libros. Aquí está nuestro catálogo:\n")
    
    # Mostrar el catálogo de libros
    for i, libro in enumerate(catalogo, 1):
        print(f"{i}. {libro[0]} - ${libro[1]}")

    # Inicializa el total de la compra
    total = 0

    # Bucle para seleccionar libros
    while True:
        seleccion = int(input("\nSelecciona el número del libro que deseas comprar (o escribe '0' para finalizar): "))
        
        if seleccion == 0:
            break  # Salir del bucle si el usuario escribe '0'
        
        if 1 <= seleccion <= len(catalogo):
            libro_seleccionado = catalogo[seleccion - 1]  # Obtener la tupla correspondiente al libro
            total += libro_seleccionado[1]  # Sumar el precio del libro al total
            print(f"Has añadido '{libro_seleccionado[0]}' a tu carrito. Precio: ${libro_seleccionado[1]}")
        else:
            print("Selección no válida. Por favor, elige un número de la lista.")

    # Aplicar descuento si el total es mayor a $500
    if total > 500:
        total *= 0.9  # Aplica un 10% de descuento
        print(f"\n¡Se te ha aplicado un descuento del 10%!")

    # Mostrar el total de la compra
    print(f"\nEl total de tu compra es: ${total:.2f}")

    # Preguntar si desea realizar otra compra
    continuar_compra = input("\n¿Deseas realizar otra compra? (sí/no): ").lower()

    # Validar respuesta
    while continuar_compra not in ["sí", "no"]:
        continuar_compra = input("Por favor, responde con 'sí' o 'no': ").lower()

print("\nGracias por comprar en nuestra tienda de libros. ¡Hasta luego!")
