#Ejercicio 14: Calculadora de Descuento
#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

# Solicitar el precio original del artículo al usuario
precio_original = float(input("Por favor, ingresa el precio del artículo: "))

# Calcular el descuento (20%)
descuento = precio_original * 0.20

# Calcular el precio final después del descuento
precio_final = precio_original - descuento

# Mostrar el precio final
print(f"El precio final después de aplicar el 20% de descuento es: {precio_final}")
