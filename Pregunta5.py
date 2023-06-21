"""Crear un programa que partiendo de un sueldo en una variable, sepamos si es par o
impar. Utilizar módulo y condicional."""
sueldo = int(input("Ingrese sueldo: "))
if sueldo % 2 == 0:
    print("El sueldo es par")
else:
    print("El sueldo es impar")