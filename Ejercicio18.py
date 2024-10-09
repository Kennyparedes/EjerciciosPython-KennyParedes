# Ejercicio 18: Contador de Palabras
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
# Solicitar al usuario que ingrese una oración
oracion = input("Por favor, ingresa una oración: ")

# Dividir la oración en palabras usando el método split()
palabras = oracion.split()

# Contar el número de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")

