'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.'''

dolares = float(input("Ingrese la cantidad de dólares: "))
tasa_de_cambio = 0.85
euros = dolares * tasa_de_cambio
print(dolares, "dólares equivalen a", euros, "euros.")