# Tupla con las reglas economicas de la partida

configEconomia = (600, 400, 50, 200, 0, 1500, 800)
#                 600  400  50  200  0  1500  800




colKills = 0
colDeaths = 1
colAssists = 2
colDinero = 3
colRondas = 4
colMvps = 5


def crearMatrizLimpia(cantJugadores):
    """Crea una matriz con ceros y el saldo inicial para una partida."""
    matriz = []
    for i in range(cantJugadores):
        fila = [0, 0, 0, configEconomia[6], 0, 0]
        matriz.append(fila)
    return matriz


def crearMatrizGeneral(cantJugadores):
    """Crea la matriz acumuladora del torneo llena de ceros."""
    matriz = []
    for i in range(cantJugadores):
        fila = [0, 0, 0, 0, 0, 0]
        matriz.append(fila)
    return matriz