from datetime import datetime, date
class Persona:
    nacionalidad = "peruana"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1

try:
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa una edad: "))
    tiempo = datetime.now()
    print("Su dato fue ingresado correctamente :)")
except ValueError:
    print("La edad tiene que ser un número entero.")


persona = Persona(nombre, edad)
persona.cumpleaños()
persona.cumpleaños()
print("La edad que tiene después de 2 cumpleaños es: {}".format(persona.edad))
print("El tiempo de registro es: {}".format(tiempo))
