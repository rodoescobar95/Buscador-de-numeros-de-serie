import os
from datetime import datetime
import re
import time
import math

def fecha():
    dia = datetime.now().day
    mes = datetime.now().month
    anio = datetime.now().year
    print(f'Fecha de busqueda: {dia}/{mes}/{anio}')


def recorrer():
    ruta = 'C:\\Users\\rodoe\\Desktop\\pythonProject\\Dia 9\\Mi_Gran_Directorio'
    ocurrencias = 0
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arc in archivo:

            nuevaruta = carpeta + f'\\{arc}'
            abrir = open(nuevaruta, 'r')
            contenido = abrir.read()
            patron = re.compile(r'N\D{3}-\d{5}')

            buscar = re.search(patron, contenido)

            if buscar:
                print(f"\t{arc}\t{buscar.group(0)}")
                ocurrencias += 1
    print(f"\nNumeros encontrados: {ocurrencias}")


def inicio():
    print("----------------------------------------------------")
    fecha()
    print("\n")
    print("\tARCHIVO\t\tNRO.SERIE")
    print("\t-------\t\t----------")
    comienza = time.time()
    recorrer()
    final = time.time()
    tiempo = math.ceil(final - comienza)
    print(f"Duracion de la busqueda: {tiempo} segundos")
    print("----------------------------------------------------")


inicio()