from clases import (Jugador, Personaje, Medico, Inteligencia, Francotirador, Artillero)
from utils import (limpiar_terminal, eliminar_personajes_muertos)

def main():

    print('')

    print(' -- Bienvenidos a TACTICAL BATTLE -- \n')

    input('Turno del Jugador 1. Pulsa intro para comenzar\n ')
    j1 = Jugador()
    j1.crear_equipo()
    j1.posicionar_equipo()
    print('')
    input('Jugador 1, pulsa intro para terminar tu turno\n ')
    limpiar_terminal()

    input('Turno del Jugador 2. Pulsa intro para comenzar\n ')
    j2 = Jugador()
    j2.crear_equipo()
    j2.posicionar_equipo()
    print('')
    input('Jugador 2, pulsa intro para terminar tu turno\n ')
    limpiar_terminal()

    j1.oponente = j2
    j2.oponente = j1

    final = False

    input('Turno del Jugador 1. Pulsa intro para comenzar\n ')

    while not final:

        #-- TURNO JUGADOR 1

        str1 = j1.realizar_accion()
        print('')
        j2.recibir_accion(str1)

        input('Jugador 1, pulsa intro para terminar tu turno\n ')
        limpiar_terminal()

        #-- TURNO JUGADOR 2

        eliminar_personajes_muertos(j2.equipo)
        final = j1.turno()
        if final:
            print(" ----- EL JUGADOR 1 HA GANADO LA PARTIDA! ----- ")
            return 0

        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar\n ')
        print(j2.informe)


        str2 = j2.realizar_accion()
        print('')
        j1.recibir_accion(str2)

        input('Jugador 2, pulsa intro para terminar tu turno\n ')

        limpiar_terminal()

        eliminar_personajes_muertos(j1.equipo)
        final = j2.turno()
        if final:
            print(' ----- EL JUGADOR 1 HA GANADO LA PARTIDA! ----- ')
            return 0

        #-- TURNO JUGADOR 1

        limpiar_terminal()
        input('Turno del Jugador 1. Pulsa intro para comenzar\n ')
        print(j1.informe)

if __name__ == '__main__':

    main()













