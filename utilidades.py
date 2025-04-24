#mi idea de utilidades.py es crear funciones de utildad donde el jugador ingrese 1 2 3 ( piedra papel o tijera) y otra donde valide los inputs y evite errores

def mostrar_elemento(eleccion: int) -> str:
    """convierte 1, 2 o 3 en piedra papel o tijera xd."""
    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"
        case _:
            return "Desconocido"


def pedir_eleccion() -> int:
    """Pide al usuario 1, 2 o 3 validando sin usar try-except."""
    while True:
        entrada = input("Elegí una opción (1 = Piedra, 2 = Papel, 3 = Tijera): ")
        
        if entrada.isdigit():
            eleccion = int(entrada)
            if eleccion in (1, 2, 3):
                return eleccion
            else:
                print("X Entrada inválida. Debes elegir 1, 2 o 3.")
        else:
            print("X Por favor ingresá un número.")
