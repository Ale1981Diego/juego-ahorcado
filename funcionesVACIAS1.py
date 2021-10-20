#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import pygame, sys
from configuracion import *
from principal1 import *
import math
import random


def unaAlAzar(lista):
    letra=random.choice(lista)
    return letra

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    i=0
    for elem in items:
        if elem==item:
            if palabraUsuario=="":
                return -10
            if (palabraUsuario[0]==unaAlAzar(letra) and palabraUsuario in listaDeTodo[i]):
                return 10
            return -5
        i=i+1

def juegaCompu(letra, listaDeTodo):
    salida=[]
    posibles=[]
    aleatorio=""
    vacio=" "
    for lista in listaDeTodo:
        for elemento in lista:
            if elemento[0]==unaAlAzar(letra):
                posibles.append(elemento)
        if len(posibles) == 0:
            salida.append(vacio)
        else:
            aleatorio=random.choice(posibles)
            salida.append(aleatorio)
        posibles=[]
    return salida

def abrirArchivos(lista):
    listaNueva=[]
    for i in lista:
        listaNueva.append(i[:-2])
    return listaNueva

def puntosExtras(usuario,compu):
    if usuario == compu:
        return 15
    if (compu==" " and usuario==""):
        return 10
    return 0
