#modulo principal del fokin jueguito

import random       #modulo para generar eleccion aleatoria
from funciones import (
    verificar_ganador_ronda,        #funcion que determina quien gano la ronda
    verificar_estado_partida,       #funcion que revisa si la partida continua o sigue
    verificar_ganador_partida,      #funcion que determina quien gano la partida comparando aciertos del juegador y maquina
)
from utilidades import (
    mostrar_elemento,       #convierte 1 2 3 en cuarzo papiro navaja xd
    pedir_eleccion,         #pide al jugador que pickee 1 2 3 y valida lo ingresado
)

def jugar_piedra_papel_tijera() -> str:        #retorna un str pq devuelve al ganador final
    """
    bucle principal:
     - controla rondas
     - detecta racha de 2 victorias seguidas
     - aplica mejor de 3 (continua si hay empate en 3)
    """
    ronda = 1
    aciertos_jugador = 0
    aciertos_maquina = 0
    ultimo_ganador = None
    racha = 0

    while True:                                 #bucle principal, se ejecuta hasta que se cumpla la condicion de salida
        print(f"\n--- Ronda {ronda} ---")
        jugador = pedir_eleccion()
        maquina = random.randint(1, 3)

        print(f" Jugador eligió: {mostrar_elemento(jugador)}")
        print(f" Máquina eligió: {mostrar_elemento(maquina)}")

        resultado = verificar_ganador_ronda(jugador, maquina)
        if resultado == "Jugador":
            aciertos_jugador += 1
            print(" Ganaste la ronda!")
        elif resultado == "Máquina":
            aciertos_maquina += 1
            print(" Perdiste la ronda.")
        else:
            print(" Empate.")

        # actualizar racha
        if resultado in ("Jugador", "Máquina"):
            if resultado == ultimo_ganador:
                racha += 1
            else:
                racha = 1
                ultimo_ganador = resultado
        else:
            # si hay empate, rompemos racha
            racha = 0
            ultimo_ganador = None

        # condicion de salida: dos victorias seguidas
        if racha == 2:
            print(f"\n {ultimo_ganador} logra dos victorias seguidas. ¡Fin de la partida!")
            break

        # condicion de mejor de 3
        if not verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda):
            break

        ronda += 1

    ganador_final = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"\n ¡{ganador_final} gana la partida con {aciertos_jugador}-{aciertos_maquina}!")
    return ganador_final