# Alcance del proyecto(Funcional)

## Dominio

Simulación de partidas competitivas de Counter-Strike en formato reducido MR5, donde la economía individual de cada jugador determina su equipamiento y la probabilidad de victoria de su equipo.

## Elementos que administra

Lista de jugadores identificados por su ID posicional, matriz de juego con sus métricas de Kills, Deaths, Assists, Dinero, Kills por Ronda y MVPs, y la economía con sus saldos individuales, costos de compra y premios por ronda o bajas.

## porcentajes,promedios,máximos,etc

Porcentajes de probabilidad de victoria según el equipamiento (20%, 35%, 50% u 80%), saldo promedio del equipo para evaluar estabilidad o quiebra, determinación del jugador con más bajas como mejor jugador (Top Fragger) y límite monetario permitido de $12000.

## Procesamiento

Inicialización de la matriz con el saldo de ronda pistol de $800, validación y descuento de compras sin generar saldo negativo, generación aleatoria de 5 bajas por ronda con liquidación de premios (+$300 kill, +$3250 victoria, +$1400 derrota) y generación de 5 informes consolidados de rendimiento. Al acabar las 5 rondas los jugadores pierden el dinero acumulado. 

# Tecnico
> **¡Atención!** Límite de la etapa: No se exige persistencia. Al cerrar el programa, los datos pueden perderse. Archivos diccionarios y conjuntos se incorporarán en la segunda iteración.

## Estructura de datos

## Lista

Lista JUGADORES como una estructura homogénea con los nombres de los 5 integrantes del equipo.

## Matriz

Matriz matrizStats como una estructura homogénea de 5x6 enteros con las métricas completas del equipo.

## Tupla

Estructura constante CONFIG_ECONOMIA que almacena los precios, las recompensas y los topes financieros.

## Cadena

Cadenas para los nombres de los jugadores, los estados de compra del equipo y el texto de las opciones del menú.

## Diseño Modular

El módulo datos.py almacena las constantes, la configuración inicial y la creación de la matriz. El módulo operaciones.py contiene la lógica de simulación, la economía, los cálculos, las búsquedas, la expresión lambda y los informes. El módulo main.py ejecuta el menú en bucle, la captura de datos y las llamadas al sistema.

## Validaciones

Control de opciones del menú para que sean numéricas dentro del rango del 1 al 6, validación de búsqueda por ID numérica de 0 a 4 mediante .isdigit(), verificación de saldo suficiente antes de aplicar las compras y bloqueo de consultas si no se simuló una partida previa.

## Procesamientos

Se realizan 2 acumulaciones para el total de Kills y el total de dinero del equipo. Se realiza 1 conteo para los jugadores con al menos 1 MVP. Se realiza 1 búsqueda para consultar estadísticas de un jugador por ID. Se calcula 1 máximo para determinar al Top Fragger. Se realiza 1 detección de condición para la alerta por promedio bancario en estado de quiebra. Se genera 1 ranking de anotadores ordenado de mayor a menor mediante lambda.
