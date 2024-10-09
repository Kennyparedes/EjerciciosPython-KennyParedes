'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
numero = int(input("Ingresa un número del 1 al 7: "))
print("El día es:", dias[numero-1])