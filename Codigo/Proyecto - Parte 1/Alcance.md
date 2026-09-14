# Alcance del proyecto(Funcional)

## Dominio

Sistema de simulación y gestión de torneos de Counter-Strike en formato competitivo MR5, donde la economía individual de cada jugador determina su equipamiento, la probabilidad de victoria del equipo, y se registran estadísticas consolidadas del torneo completo.

## Elementos que administra

- Lista de equipos con sus jugadores (5 integrantes por equipo)
- Matriz de estadísticas por jugador: Kills, Deaths, Assists, Dinero, Rondas Jugadas, MVPs
- Economía del juego: saldos individuales, costos de compra de equipamiento, premios por ronda
- Historial de partidas disputadas y resultados consolidados
- Torneos almacenados en memoria con su estructura y datos

## porcentajes,promedios,máximos,etc

Porcentajes de probabilidad de victoria según equipamiento (20%, 35%, 50%, 80%), saldo promedio del equipo para evaluar estabilidad o quiebra, determinación del mejor jugador por promedio de kills por ronda (K/R), ranking de jugadores ordenado por kills totales, límite monetario de $1500 por jugador.

## Procesamiento

Inicialización de matriz con saldo pistol de $800 por ronda, validación y descuento de compras de equipamiento ($600 full, $400 económico) sin generar saldo negativo, generación aleatoria de kills por ronda con cálculo de premios (+$50 por kill), asignación de MVP por ronda (jugador con más kills), liquidación de dinero con tope máximo de $1500, y generación de 5 informes consolidados de rendimiento tras cada partida.

# Tecnico
> **¡Atención!** Límite de la etapa: No se exige persistencia. Al cerrar el programa, los datos pueden perderse. Archivos diccionarios y conjuntos se incorporarán en la segunda iteración.

## Estructura de datos

## Lista

- Lista de equipos con sus nombres
- Lista de jugadores por equipo
- Historial de matrices de partidas disputadas
- Torneos creados almacenados en memoria

## Matriz

Matriz matrizStats como una estructura homogénea de 5x6 enteros con las métricas completas del equipo.

## Tupla

Estructura constante CONFIG_ECONOMIA que almacena los precios, las recompensas y los topes financieros (600, 400, 50, 200, 0, 1500, 800).

## Cadena

Cadenas para los nombres de los jugadores, los estados de compra del equipo y el texto de las opciones del menú.

## Diseño Modular

El módulo datos.py almacena las constantes, la configuración inicial y la creación de la matriz. El módulo operaciones.py contiene la lógica de simulación, la economía, los cálculos, las búsquedas, la expresión lambda y los informes. El módulo main.py ejecuta el menú en bucle, la captura de datos y las llamadas al sistema.

## Validaciones

Control de opciones del menú para que sean numéricas dentro del rango del 1 al 6, validación de búsqueda por ID numérica de 0 a 4 mediante .isdigit(), verificación de saldo suficiente antes de aplicar las compras y bloqueo de consultas si no se simuló una partida previa.

## Procesamientos

Se realizan 2 acumulaciones para el total de Kills y el total de dinero del equipo. Se realiza 1 conteo para los jugadores con al menos 1 MVP. Se realiza 1 búsqueda para consultar estadísticas de un jugador por ID. Se calcula 1 máximo para determinar al Top Fragger. Se realiza 1 detección de condición para la alerta por promedio bancario en estado de quiebra. Se genera 1 ranking de anotadores ordenado de mayor a menor mediante lambda.

## Flujo de Torneos

El sistema permite crear múltiples torneos personalizados con nombre, cantidad de equipos (2/4/8) y jugadores. Cada torneo ejecuta una llave de eliminación directa: Semifinal 1, Semifinal 2 y Gran Final. Cada partida simula todas sus rondas hasta que un equipo gane 3 rondas (MR5). Las estadísticas de todas las partidas se acumulan en una matriz global del torneo.
