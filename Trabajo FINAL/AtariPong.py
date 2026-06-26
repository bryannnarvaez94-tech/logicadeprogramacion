puntaje_player1 = 0
puntaje_rival = 0
puntaje_maximo = 10 

print ("Inicio de partida")

#bucle principal del juego
while puntaje_player1 < 10 and puntaje_rival < 10:
    print("Saque del player1")
    bloqueo_rival = input("se bloqueo el saque del player1? "
    "(s/n): ")
    if bloqueo_rival == "s":
        #el rival bloqueó el saque, ahora player1 tiene que bloquear
        bloqueo_player1 = input("se bloqueo el saque del rival? "
        "(s/n): ")
        if bloqueo_player1 == "n":
            #player1 no bloqueó, punto para rival
            puntaje_rival += 1
            print(f"Punto para el rival: {puntaje_rival}")
        else: 
            #player1 bloqueó el saque del rival, sigue el juego
            print("Bloqueaste el saque del rival, sigue el juego")
    elif bloqueo_rival == "n":
        #el rival no bloqueó el saque, punto para player1
        puntaje_player1 += 1
        print(f"Punto para player1: {puntaje_player1}")
    else:
        print("Opción inválida, por favor ingrese 's' o 'n'.")
#fin del bucle principal del juego y declaración del ganador
print("Fin de partida")
if puntaje_player1 == puntaje_maximo:
    print("¡Felicidades, player1! Ganaste la partida.")
elif puntaje_rival == puntaje_maximo:
    print("¡El rival ganó la partida! Mejor suerte la próxima vez.")



