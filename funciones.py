# funciones para quien gana la ronda si sigue o q pasaxd

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """
    Devuelve 'Jugador', 'Máquina' o 'Empate'
    según las reglas clásicas: Piedra> Tijera, Tijera> Papel, Papel> Piedra.
    """
    if jugador == maquina:
        return "Empate"
    # casos en que gana el jugador (tupla de pares, preguntar en clase si esta correcto, lo lei en reddit de un random)
    if (jugador, maquina) in ((1, 3), (2, 1), (3, 2)):
        return "Jugador"
    return "Máquina"


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """
    True  -> si debe continuar el mejor de 3 (ronda < 3 o empate tras 3).
    False -> si ya se cumplió el mejor de 3 sin empate.
    """
    if ronda_actual < 3:
        return True
    # tras 3 rondas, si hay empate en victorias, seguimos; si no, terminamos
    return aciertos_jugador == aciertos_maquina


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """Compara aciertos finales y devuelve 'Jugador' o 'Máquina'."""
    return "Jugador" if aciertos_jugador > aciertos_maquina else "Máquina"