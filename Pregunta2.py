from datetime import datetime, date
class Persona:
    nacionalidad = "peruana"

    def __init__(self, nombre, edad,saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
    def cumpleaños(self):
        self.edad += 1

    def transferencia(self, destino, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            destino.saldo += monto
            print("Transferencia realizada")
        else:
            print("No hay saldo")

    def mostrar_saldo(self):
        print("Saldo actual:", self._saldo)
try:
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa una edad: "))
    tiempo = datetime.now()
    print("Su dato fue ingresado correctamente :)")
except ValueError:
    print("La edad tiene que ser un número entero.")


persona1 = Persona(nombre, edad,100)
persona1.transferencia(persona1, 30)
persona1.cumpleaños()
persona1.cumpleaños()
print("La edad que tiene después de 2 cumpleaños es: {}".format(persona1.edad))
print("El tiempo de registro es: {}".format(tiempo))
