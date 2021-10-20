#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import pygame, sys
from collections import namedtuple

TAMANO_LETRA = 20
TAMANO_LETRA_GRANDE = 25
TAMANO_LETRA_MUYGRANDE = 60
FPS_INICIAL = 3

ANCHO = 800
ALTO = 600
COLOR_LETRA = (162, 0, 0)  # letra al azar (color rojo)
COLOR_LETRAS = (1, 75, 32) # color de la palabra juegaCompu (color verde)
COLOR_FONDO = (255, 255, 255)      # color fondo (color blanco)
COLOR_TEXTO = (0, 0, 0)      # color texto tiempo, puntos e items (color negro)
COLOR_TIEMPO_FINAL = (200, 10, 10) # color tiempo final (a partir de los 60" cambia a color rojo)
COLOR_USUARIO = (162, 0, 0) # color palabraUsuario final (color naranja)


