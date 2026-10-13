from matplotlib import pyplot as plt
from collections import namedtuple
import csv
from typing import List,Tuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')


def lee_poblaciones (ruta:str):

    tupla = []
    with open (ruta,encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for pais,codigo,año,censo in lector:
            tupla.append(RegistroPoblacion(
                pais.strip(),
                codigo.strip(),
                int(año),
                int(censo)
            ))
    return tupla

""" tambien se puede poner asi : 

def lee_poblaciones (ruta:str):
    poblaciones = []
    with open (ruta,encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fila in lector:
            pais = fila[0]
            codigo = fila[1]
            año = int(fila[2])
            censo = int(fila[3])
            poblacion = RegistroPoblacion(pais,codigo,año,censo)
            poblaciones.append(poblacion)
            
    return poblaciones 
"""

"""
def calcula_paises(poblaciones:List[RegistroPoblacion])-> List[str]:
    lista = []
    for p in poblaciones:
        for w in p: # bucle anidado = MAL ; recorro las palabras letra por letra
            lista.append(w[0])
    return sorted(lista)

"""
def calcula_paises(poblaciones:List[RegistroPoblacion])-> List[str]:
    paises = set()
    for p in poblaciones:
        paises.add(p.pais)
    return sorted(paises)


def filtra_por_pais(poblaciones:List[RegistroPoblacion],nombre_o_codigo:str)->List[RegistroPoblacion]:
    lista = []
    for p in poblaciones:
        if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo:
            lista.append((p.año,p.censo)) # NO SE PONE TUPLE(p.año,p.censo) PORQUE TUPLE SOLO RECIBE UN ARGUMENTO.
    return lista



def filtra_por_paises_y_anyo(poblaciones:List[RegistroPoblacion], anyo:int, paises:List[str])->List[Tuple[str,int]]:
    lista = []
    for p in poblaciones:
        if p.año == anyo and p.pais in paises:
            print(p)
            lista.append((p.pais,p.censo)) # NO SE PONE TUPLE(p.año,p.censo) PORQUE TUPLE SOLO RECIBE UN ARGUMENTO.
    return lista
"""
def muestra_evolucion_poblacion(poblaciones:List, nombre_o_codigo:str):
    lista = []
    for p in poblaciones:
        if p[0] == nombre_o_codigo or p[1] == nombre_o_codigo:
            lista_años = [p[2]]
            lista_habitantes = [p[3]]
                
            plt.title("evolucion de poblacion")
            plt.plot(lista_años, lista_habitantes)
            plt.show()
        else:
            return print("no hay datos que coincidan con los parámetros")
"""
def muestra_evolucion_poblacion(poblaciones:List, nombre_o_codigo:str):
    pfil = filtra_por_pais(poblaciones,nombre_o_codigo)
    lista_años = []
    lista_censo = []
    
    for p in pfil:
        lista_años.append(p[0])
        lista_censo.append(p[1])
    
    plt.title("evolucion de poblacion")
    plt.plot(lista_años,lista_censo)
    plt.show()



 # def muestra_comparativa_paises_anyo(poblaciones:List, anyo:int, paises:set):

