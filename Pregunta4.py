"""Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe
estar en una variable. Mostrar el volumen por pantalla."""
import math
radio = float(input("Ingrese radio: "))
volumen = 4/3 * math.pi * radio**3
print("El volumen es:", volumen)