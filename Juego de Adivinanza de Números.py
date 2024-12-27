import random 
num = random.randint(1,100)
print("He elegido un número entre 1 y 100. Tienes 5 intentos para adivinarlo.")
# Bucle para 5 intentos
for intento in range(1, 6):
    num1 = int(input(f"Intento {intento}: "))  # Pedir al usuario que ingrese un número
    
    # Comparar el número ingresado con el número aleatorio
    if num1 > num:
        print("El número es menor.")
    elif num1 < num:
        print("El número es mayor.")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intento} intentos.")
        break  # Salir del bucle si el usuario adivina el número
else:
    # Este bloque se ejecuta si el usuario no adivina el número en 5 intentos
    print(f"Lo siento, no has adivinado el número. Era {num}.")

