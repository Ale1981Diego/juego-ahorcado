#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Materia: Introduccion a la programación
    Comisión: 07
    Profesores: Luis Varonesi
                Cinthya Cardozo
    Alumnos: Agustin Quiroga
             Sebastian Aranda
             Alejandro Mancilla
    Universidad Nacional de General Sarmiento
'''
import codecs
import math, os, random, sys # El módulo provee acceso a funciones y objetos mantenidos por del intérprete.
import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS1 import *
from extras import *

def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # pygame.mixer.init()

    # musica del juego
    pygame.mixer.music.load("ImagenSonido/musica.ogg")
    pygame.mixer.music.play()

    # sonido acierto
    acierto = pygame.mixer.Sound("ImagenSonido/aciertos.ogg")
    puntoExtraCompu = pygame.mixer.Sound("ImagenSonido/ExtraCompu.ogg")

    # Juego terminado antes de los 60 segundos
    super = pygame.mixer.Sound("ImagenSonido/super.ogg")

    #sonido item vacio
    vacio = pygame.mixer.Sound("ImagenSonido/pop.ogg")

    # sonido error
    error = pygame.mixer.Sound("ImagenSonido/error.ogg")

    # terminar juego despues de los 60 segundos
    sonidoFinal = pygame.mixer.Sound("ImagenSonido/MarioGameOver.ogg")

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # imagen de fondo
    fondoPresentacion = pygame.image.load("ImagenSonido/Python1.png").convert()

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    candidata = ""
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    items=["colores","paises", "animales","nombres","frutas","verduras","marcas"]
    colores = codecs.open("listas/colores.txt","r","utf-8")
    paises = codecs.open("listas/paises.txt","r","utf-8")
    animales = codecs.open("listas/animales.txt","r","utf-8")
    nombres = codecs.open("listas/nombres.txt","r","utf-8")
    frutas = codecs.open("listas/frutas.txt","r","utf-8")
    verduras = codecs.open("listas/verduras.txt","r","utf-8")
    marcas = codecs.open("listas/marcas2.txt","r","utf-8")
    listaDeTodo=[abrirArchivos(colores),abrirArchivos(paises),abrirArchivos(animales),abrirArchivos(nombres),abrirArchivos(frutas),abrirArchivos(verduras),abrirArchivos(marcas)]
    colores.close()
    paises.close()
    animales.close()
    nombres.close()
    frutas.close()
    verduras.close()
    marcas.close()
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]
    puntos=0
    puntosPorItem=[]
    puntosParciales=[]
    i=0

    #eleccion de la computadora
    eleccionCompu=juegaCompu(letraAzar, listaDeTodo)

    while i < len(items):
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)

        totaltime += gameClock.get_time()
        fps = 3

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)
                        sumaExtras=puntosExtras(palabraUsuario,eleccionCompu[i])
                        puntos+=sumaExtras+sumar
                        puntosPorItem.append(str(sumaExtras+sumar)) # muestra en pantalla los puntos
                        puntosParciales.append(puntos) # muestra en pantalla las sumas parciales
                        palabraUsuario=""
                        i=i+1
                        if sumar==10 and sumaExtras==15: # acierto palabraUsuario + juegacompu
                            puntoExtraCompu.play()
                        else:
                            if sumar==10:                # Inicia Sonido al sumar puntos
                                acierto.play()
                            else:
                                if sumaExtras == 10: # Indica si no existe palabra
                                    vacio.play()
                                else:
                                    error.play() # Error

        if i==len(items):
            # finaliza la musica del juego al finalizar el juego
            pygame.mixer.music.stop()
        segundos = pygame.time.get_ticks() / 1000

        # limpiar pantalla anterior

        screen.blit(fondoPresentacion,[0,0])

        # screen.fill(COLOR_FONDO)
        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
        else:
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, puntosPorItem, puntosParciales, segundos)

            if segundos > 30 or punto < 50:
                sonidoFinal.play() # Si supera los 60 segundos
            else:
                super.play() # Si contesta antes de que el juego llegue a los 60 segundos

        pygame.display.flip()




    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
