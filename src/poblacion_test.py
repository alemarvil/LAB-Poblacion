from poblacion import *
ruta = 'data/population.csv'

if __name__ == "__main__":
    a = lee_poblaciones(ruta)
    paises = calcula_paises(a)
    w = filtra_por_paises_y_anyo(a,2019,["Croatia"])
    m = muestra_evolucion_poblacion(a,"Croatia")
    print(m)