#Ejercicio 15: Conversor de Tiempo
#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
# Solicitar al usuario que ingrese el número de minutos
minutos_totales = int(input("Por favor, ingresa el número de minutos: "))

# Calcular horas y minutos
horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

# Mostrar el resultado
print(f"{minutos_totales} minutos son {horas} horas y {minutos_restantes} minutos.")
