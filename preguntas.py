"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import itertools
from collections import Counter
from datetime import datetime
from operator import itemgetter

with open ("data.csv", "r") as file:
        datos = file.readlines()
datos = [line.replace('\t','|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]


def pregunta_01():
 suma = 0
 for lista in datos:
    suma += int(lista[1])

    return suma

def pregunta_02():
    columna = [fila[0] for fila in datos]
    columna_no_duplicadas = sorted(set(columna))
    lista_tupla =[(j, columna.count(j)) for j in columna_no_duplicadas]

    return lista_tupla

def pregunta_03():
    datos_suma=[]
    for i, j in itertools.groupby(sorted(datos), lambda x : x[0]):
        datos_suma.append((i, sum(int(x[1]) for x in j)))

    return datos_suma


def pregunta_04():
    data_by_month = Counter()
    for row in datos:
        date = datetime.strptime(row[2][:7], "%Y-%m")
    data_by_month['{:02d}'.format(date.month)] += 1
    return sorted(list(data_by_month.items()))


def pregunta_05():
        datos_suma = []
        for i, j in itertools.groupby(sorted(datos), lambda x : x[0]):
            valores_list = [x[1] for x in j]
        datos_suma.append((i, int(max(valores_list)), int(min(valores_list))))

        return datos_suma

def pregunta_06():
     nueva_lista_valores = []
     datos_dic = []
     valores = [x[4] for x in datos]
     lista_valores = [x.split(",") for x in valores]
     for x in lista_valores:
        for y in x:
            nueva_lista_valores.append(y.split(":"))
            for i, j in itertools.groupby(sorted(nueva_lista_valores), lambda x : x[0]):
                valores_list = [int(x[1]) for x in j]
            datos_dic.append((i, min(valores_list), max(valores_list)))

            return datos_dic

def pregunta_07():
    columnas = [x[:2] for x in datos]
    new_group = []
    for i, j in itertools.groupby(sorted(columnas, key = lambda x: x[1]), lambda x: x[1]):
        new_group.append((int(i), [x[0] for x in j]))

        return new_group


def pregunta_08():
    columnas = [x[:2] for x in datos]
    new_group = []
    for i, j in itertools.groupby(sorted(columnas, key = lambda x: x[1]), lambda x: x[1]):
        new_group.append((int(i), sorted(list(set([x[0] for x in j])))))

        return new_group 

def pregunta_09():
    nueva_lista_valores = []
    valores = [x[4] for x in datos]
    lista_valores = [x.split(",") for x in valores]
    contador = Counter()
    for x in lista_valores:
        for y in x:
            nueva_lista_valores.append(y.split(":"))

    for dicc in nueva_lista_valores:
        contador[dicc[0]] += 1

    return dict(sorted(contador.items()))



def pregunta_10():
    columnas = [itemgetter(0,3,4)(i) for i in datos]
    conteo = []
    for x in columnas:
        col4 = len(x[1].split(","))
        col5 = len(x[2].split(","))
        conteo.append((x[0],col4,col5))

    return conteo

def pregunta_11():

 col1 = [itemgetter(1)(i) for i in datos]
 col3 = [i[3].split(",") for i in datos]
 new_ = zip(col1,col3)
 new_1 = []
 new_group = []
 for x in list(new_):
        for y in x[1]:
            new_1.append((x[0],y))
            for i, j in itertools.groupby(sorted(new_1, key = lambda x: x[1]), lambda x: x[1]):
                new_group.append((i, sum([int(y[0]) for y in j])))
                
                return dict(new_group)


def pregunta_12():
  col0 = [itemgetter(0)(i) for i in datos]
  col4 = [i[4].split(",") for i in datos]
  valores = []
  a = 0
  for x in col4:
    for y in x:
            a += (int(y[y.index(":")+1:]))
            valores.append(a)
            a = 0
            new_ = zip(col0,valores)
            new_group = []
            for i, j in itertools.groupby(sorted(list(new_), key = lambda x: x[0]), lambda x: x[0]):
                new_group.append((i, sum(y[1] for y in j)))

    return dict(new_group)