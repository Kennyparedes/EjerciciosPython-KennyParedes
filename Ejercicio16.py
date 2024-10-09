#Ejercicio 16: Contador de Números Pares e Impares
#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
# Solicitar al usuario que ingrese una lista de números separados por espacios
numeros = input("Por favor, ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, numeros.split()))

# Inicializar contadores
pares = 0
impares = 0

# Recorrer la lista y contar pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar los resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

