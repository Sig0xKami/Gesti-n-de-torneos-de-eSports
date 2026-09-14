import datos
import interfaz
import torneo


def main():
    # Lista para guardar torneos
    torneos_creados = []
    listaEquipos = ["Luminosity", "Fnatic", "Navi", "Astralis"]
    matrizPlanteles = [
        ["Coldzera", "FalleN", "Fer", "Taco", "Fnx"],
        ["Olofmeister", "Flusha", "JW", "Krimz", "Dennis"],
        ["Simple", "Flamie", "Edward", "Zeus", "Guardian"],
        ["Device", "Dupreeh", "Xyp9x", "Kjaerbye", "Gla1ve"],
    ]

    miEquipo = matrizPlanteles[0]
    matrizGeneralTorneo = datos.crearMatrizGeneral(len(miEquipo))
    historialPartidas = []
    nombresPartidas = [
        f"Semifinal 1 ({listaEquipos[0]} vs {listaEquipos[1]})",
        f"Semifinal 2 ({listaEquipos[2]} vs {listaEquipos[3]})",
        f"Gran Final",
    ]
    torneoJugado = False

    continuarMenu = True
    while continuarMenu:
        print("")
        interfaz.mostrarMenuCuadro()
        entrada = input("Seleccione una opcion (1-6): ")

        try:
            opcion = int(entrada)
        except ValueError:
            opcion = 0

        if opcion == 1:
            nombre_torneo = input("Nombre del torneo: ")
            try:
                cantidad_equipos = int(input("Equipos (2/4/8): "))
            except ValueError:
                print("Error: Debe ingresar un número\n")
                continue

            equipos_input = []
            for e in range(cantidad_equipos):
                nombre_eq = input(f"Nombre equipo {e+1}: ")
                jugadores = []
                for j in range(5):
                    nombre_jug = input(f"  Jugador {j+1}: ")
                    jugadores.append(nombre_jug)
                equipos_input.append(
                    {"nombre": nombre_eq, "jugadores": jugadores}
                )

            torneos_creados.append(
                {"nombre": nombre_torneo, "equipos": equipos_input}
            )
            print(f"✓ Torneo '{nombre_torneo}' creado\n")

        elif opcion == 2:
            if not torneos_creados:
                print("No hay torneos creados\n")
            else:
                print("\nTorneos disponibles:")
                for i in range(len(torneos_creados)):
                    print(f"{i+1}. {torneos_creados[i]['nombre']}")
                print()

        elif opcion == 3:
            if not torneos_creados:
                print("Cree un torneo primero\n")
            else:
                print("\nTorneos disponibles:")
                for i in range(len(torneos_creados)):
                    print(f"{i+1}. {torneos_creados[i]['nombre']}")

                idx = int(input("Seleccione torneo (número): ")) - 1
                torneo_sel = torneos_creados[idx]

                matriz_torneo = datos.crearMatrizGeneral(5)
                historial = []
                equipos_torneo = [e["nombre"] for e in torneo_sel["equipos"]]

                print(f"\nEjecutando: {torneo_sel['nombre']}")
                torneo.ejecutarTorneoCompleto(
                    equipos_torneo,
                    [e["jugadores"] for e in torneo_sel["equipos"]],
                    matriz_torneo,
                    historial,
                )
                interfaz.mostrarReportesGlobales(
                    matriz_torneo, torneo_sel["equipos"][0]["jugadores"]
                )

        elif opcion == 4:
            if not torneos_creados:
                print("Cree y ejecute un torneo primero\n")
            else:
                print("Opción para ver resultados en desarrollo\n")

        elif opcion == 5:
            print("\n[SIMULACIÓN RÁPIDA - Testing]")
            listaEquipos = ["TestA", "TestB", "TestC", "TestD"]
            matrizPlanteles = [
                ["J1", "J2", "J3", "J4", "J5"],
                ["J6", "J7", "J8", "J9", "J10"],
                ["J11", "J12", "J13", "J14", "J15"],
                ["J16", "J17", "J18", "J19", "J20"],
            ]
            matrizGeneralTorneo = datos.crearMatrizGeneral(5)
            historialPartidas = []

            torneo.ejecutarTorneoCompleto(
                listaEquipos,
                matrizPlanteles,
                matrizGeneralTorneo,
                historialPartidas,
            )
            interfaz.mostrarReportesGlobales(
                matrizGeneralTorneo, matrizPlanteles[0]
            )
            print("✓ Simulación completada\n")

        elif opcion == 6:
            print("Cerrando el simulador de torneos.")
            continuarMenu = False

        else:
            print("Opcion incorrecta. Ingrese un valor del 1 al 6.\n")


if __name__ == "__main__":
    main()