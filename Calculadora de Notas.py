# Bucle para repetir el programa si el usuario lo desea
continuar = "sí"  # Inicializamos la variable

while continuar.lower() == "sí":  # El programa seguirá si el usuario introduce "sí"
    # Inicializa una variable para almacenar la suma de las calificaciones
    suma_calificaciones = 0

    # Bucle para ingresar las 5 calificaciones
    for intento in range(1, 6):
        num1 = int(input(f"Introduce la calificación de la materia {intento}: "))
        suma_calificaciones += num1  # Suma la calificación a la suma total

    # Calcula el promedio
    promedio = suma_calificaciones / 5

    # Muestra el promedio
    print(f"Tu promedio es: {promedio}")

    # Clasificación del promedio
    if promedio >= 90:
        print("Calificación: Excelente")
    elif 80 <= promedio < 90:
        print("Calificación: Muy bueno")
    elif 70 <= promedio < 80:
        print("Calificación: Bueno") 
    elif 60 <= promedio < 70:
        print("Calificación: Suficiente")      
    else:
        print("Calificación: Insuficiente")

    # Pregunta si el usuario desea continuar
    continuar = input("¿Deseas ingresar otras calificaciones? (sí/no): ").lower()

    # Validamos que la respuesta sea correcta
    while continuar not in ["sí", "no"]:
        continuar = input("Por favor, responde con 'sí' o 'no': ").lower()

print("Gracias por usar la calculadora de notas. ¡Hasta luego!")
