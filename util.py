from Grupos import Grupo
from Dia import Dia
from Persona import Persona
import pygame
import random
print("Anim anim commodo nisi est sint laboris.")
def calcContagiados(personas = [Persona(0,1)]) -> list[Persona]:
    contagiados = []
    for persona in personas:
        if persona.estado == 1:
            contagiados.append(persona)
    return contagiados

def pintarMalla(ancho, alto, screen) -> None:
    # 2 verticales
    pygame.draw.line(screen, (0, 0, 0), (ancho / 3, 0), (ancho / 3, alto))
    pygame.draw.line(screen, (0, 0, 0), (2 * (ancho / 3), 0), (2 * (ancho / 3), alto))
    # 1 horizontal
    pygame.draw.line(screen, (0, 0, 0), (0, alto / 2), (ancho, alto / 2))


def crearGrupos(ancho, alto, enfermos, screen) -> list[Grupo]:
    grupos = []
    anchoG = 500
    altoG = 500
    columnas = 15
    filas = 15
    periodoRec = 10
    periodoInmune = 60
    # prev = 0.016
    factor = 0.05
    # grupo 1 0.33
    grupos.append(Grupo(1, 0.33*factor, enfermos, columnas, filas, (0, 0), anchoG, altoG, periodoRec, periodoInmune, screen))
    # grupo 2 0.58
    grupos.append(Grupo(2, 0.58*factor, enfermos, columnas, filas, (ancho / 3, 0), anchoG, altoG, periodoRec, periodoInmune, screen))
    # grupo 3 0.78
    grupos.append(Grupo(3, 0.78*factor, enfermos, columnas, filas, (2 * (ancho / 3), 0), anchoG, altoG, periodoRec, periodoInmune, screen))
    # grupo 4 0.89
    grupos.append(Grupo(4, 0.89*factor, enfermos, columnas, filas, (0, alto / 2), anchoG, altoG, periodoRec, periodoInmune, screen))
    # grupo 5 0.95
    grupos.append(Grupo(5, 0.95*factor, enfermos, columnas, filas, (ancho / 3, alto / 2), anchoG, altoG, periodoRec, periodoInmune, screen))
    # grupo 6 1
    grupos.append(Grupo(6, 1.00*factor, enfermos, columnas, filas, (2 * (ancho / 3), alto / 2), anchoG, altoG, periodoRec, periodoInmune, screen))
    return grupos


def crearPersonas(n) -> list[Persona]:
    personas = []
    for i in range(0, n):
        # cada persona se le asigana un número aleatorio de dosis
        personas.append(Persona(random.randrange(1, 4), i))
    return personas

