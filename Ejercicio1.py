"""Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit."""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Ingresa Temperatura en celsius
celsius = float(input("Ingresa la Temperatura en grados Celsius: "))

#Se ejecuta la funcion para hacer la conversion de grados celsius a fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

#Se imprimen resultados
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
