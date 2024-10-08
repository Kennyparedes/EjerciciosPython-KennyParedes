#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
# Pedimos al usuario su peso en kilogramos y su altura en metros
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calculamos el IMC directamente
imc = peso / (altura ** 2)

# Mostramos el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

