#Ejercicio 20: Suma de Números en una Lista
#Crea un programa que sume todos los números en una lista ingresada por el usuario.
numeros = [int(num) for num in input("Ingrese los números separados por comas: ").split(',')]
print("La suma es:", sum(numeros))