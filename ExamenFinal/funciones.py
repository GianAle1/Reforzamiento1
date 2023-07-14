import random
import math
def crearLista(tamaño):
    lista = [random.randint(1, 100) for _ in range(tamaño)]
    return lista
def calcular_raices():
    with open("notas.txt", "a") as file:
        file.write("\nRaíces cuadradas:\n")
        with open("notas.txt", "r") as original_file:
            lineas = original_file.readlines()
            for linea in lineas:
                try:
                    num = float(linea.strip())
                    raiz = math.sqrt(num)
                    file.write(str(raiz) + "\n")
                except ValueError:
                    continue