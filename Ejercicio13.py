#Ejercicio 13: Verificación de Número Primo
#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

# Solicitar al usuario que ingrese un número
num = int(input("Por favor, ingresa un número: "))

# Verificar si el número es primo
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"El número {num} no es primo.")
            break
    else:
        print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")
