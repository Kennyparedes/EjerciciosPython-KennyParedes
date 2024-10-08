"""Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta."""

# Pedimos al usuario que ingrese el total de la cuenta
total_cuenta = float(input("Introduce el total de la cuenta (sin propina): $"))

# Calculamos la propina del 15% y el total a pagar
total_a_pagar = total_cuenta * 1.15

# Mostramos el resultado
print(f"El total a pagar, incluyendo la propina del 15%, es: ${total_a_pagar:.2f}")
