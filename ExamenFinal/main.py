from funciones import crearLista, calcular_raices
import random
import math
def crear_fichero():
    with open("notas.txt", "w") as file:
        file.write("")
def escribir_lista_en_fichero(lista):
    with open("notas.txt", "a") as file:
        for num in lista:
            file.write(str(num) + "\n")
def main():
    crear_fichero()
    tamaño = int(input("Tamaño de la lista: "))
    lista = crearLista(tamaño)
    # Escribir lista en el fichero
    escribir_lista_en_fichero(lista)
    # Calcular raíces y escribir en el fichero
    calcular_raices()
if __name__ == "__main__":
    main()
