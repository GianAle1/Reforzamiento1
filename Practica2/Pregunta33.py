def ingresar_dato(mensaje):
    for _ in range(10):
        try:
            dato = float(input(mensaje))
            return dato
        except ValueError:
            print("¡Error! Debe ingresar un número válido.")


def division_entre_cero():
    numerador = ingresar_dato("Ingrese el numerador: ")
    denominador = ingresar_dato("Ingrese el denominador: ")
    while denominador == 0:
        print("No puede ser cero.")
        denominador = ingresar_dato("Ingrese el denominador: ")

    resultado = numerador / denominador
    print("la división es:", resultado)

division_entre_cero()

