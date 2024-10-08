'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''

suma_pares = 0

# Usamos un bucle para recorrer los números del 1 al 100
for numero in range(1, 101):
    if numero % 2 == 0:  # Verificamos si  es par
        suma_pares += numero  # Sumamos si es par

# Mostramos el resultado
print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")
