# logicadeprogramacion
25-06-2026 Bryan Narváez Arias
Atari Pong
El programa que escogimos fue el popular video juego que simula un tenis de mesa, Atari Pong
Problema: crear un sistema que gestione partidas,lleve el puntaje y compruebe la habilidad de los jugadores. 
Este proyecto pretende crear una lógica eficaz y simple para saber como deberia comportase el programa cuando este siendo usado por el usuario final, no es bajo ningun caso la creacion de un juego real, motor de video juego o algun script para alguna mecánica en concreto sino una manera de entender el flujo de datos, lógica del programa y sobre todo un ejercicio en Python para reforzar lo aprendido en clase. A continuación, el programa
El programa esta diseñado para que el jugador interactue con la interzas visual del juego, en donde podrá:iniciar partida, mover la raquera, bloquear jugadas del rival, incrementar su puntaje, ver el puntaje y ganar la partida
La arquitectura del programa debe tomar en cuenta al usuario (player1) que es quien va a interactuar con la interfaz visual del programa por medio de un controlador de entrada que puede ser un teclado, momuse o gamepad, esto ocacionará que el motor del juago ejecute las graficas y calculos necesarios para mover la pelota y hacer rebotes coherentes para una partida fluida. También será este motor el que llevará a cabo la suma de puntos y muestre en panatalla todo lo que haga falta
CODIGO: 
Se estableció primero las variables que vamos a usar,como puntajes y puntaje maximo
Se creo un bucle while que revise si el puntaje de ambos jugadores no es mayor a 10 pues el que llegue a 10 gana y termina lapartida
Se crearon variables de tipo string para usarlas en las condiciones que vamos a usar dentro del condicional if para saber si los jugadores bloquearon el saque del rival
Si la respuesta es no para alguno, será punto para su rival y se imprime en la pantalla de quien es el punto ganado y su puntaje actual
Se saca de nuevo la pelota y retomamos el condicional if hasta que alguno de los jugadores llegue a 10 puntos
Se declara un ganador
