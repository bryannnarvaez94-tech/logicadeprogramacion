# Declaración de variables
puntos_jugador = 0
puntos_rival = 0
limite_puntos = 10
ronda = 1

print("El primero en llegar a {limite_puntos} puntos gana.\n")

# Bucle principal del juego
while puntos_jugador < limite_puntos and puntos_rival < limite_puntos:

    print("Ronda {ronda} ---")
    print("Marcador | Jugador: {puntos_jugador}  -  Rival: {puntos_rival}")

    # El jugador intenta bloquear la pelota (ingresa s o n)
    bloqueo_jugador = input("¿Bloqueaste la pelota? (s/n): ").strip().lower()

    if bloqueo_jugador == "s":
        # Si el jugador bloqueó, la pelota va al rival
        bloqueo_rival = input("¿El rival bloqueó la pelota? (s/n): ").strip().lower()

        if bloqueo_rival == "n":
            # El rival falló: punto para el jugador
            puntos_jugador = puntos_jugador + 1
            print("¡Punto para el jugador! ({puntos_jugador} pts)\n")
        else:
            # El rival bloqueó: rally continúa, nadie anota
            print("El rival bloqueó. ¡Sigue el rally!\n")

    elif bloqueo_jugador == "n":
        # El jugador falló: punto para el rival
        puntos_rival = puntos_rival + 1
        print(f"Punto para el rival. ({puntos_rival} pts)\n")

