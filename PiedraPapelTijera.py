#juego
import random

print("BIENVENIDO AL JUEGO: PIEDRA PAPEL O TIJERA")
opciones = ("piedra", "papel", "tijera")


round = 1                                                  # contador de rounds
bot_wins = 0                                               # contador de la veces que gano el bot
user_wins = 0                                              # contador de las veces que gano el user

while True:                                                # se repite
    print("*" * 10)
    print(round, "ROUND")  
    print("*" * 10)
    print("EL BOT GANO:", bot_wins) 
    print("EL USUARIO GANO:", user_wins)                                                 

    user = input("Elige piedra, papel o tijera: ")
    user = user.lower()

    bot = random.choice(opciones)

    round += 1

    print("El bot eligio: ", bot)
    if not user in opciones:
        print("Elige una opcion correcta: PIEDRA, PAPEL O TIJERA")
        continue                                            # ignorar todo el codigo de abajo ya que se introdujo una opcion incorrecta
        
    if user == bot:
        print("Empate!!")
        
    elif user == "papel":
        if bot == "piedra":
            print("Papel le gana a piedra")
            print("El user gano")
            user_wins += 1                                   # suma 1 a user_wins
        else:
            print("Tijera gana a papel")
            print("El bot gano")
            bot_wins += 1                                   # suma 1 bot_wins
            
    elif user == "piedra":
        if bot == "tijera":
            print("Piedra le gana a tijera")
            print("El user gano")
            user_wins += 1                                  # suma 1 a user_wins
        else:
            print("Papel le gana a piedra")
            print("El bot gano")
            bot_wins += 1                                   # suma 1 bot_wins
            
    elif user == "tijera":
        if bot == "papel":
            print("Tijera le gana al papel")
            print("El user gano")
            user_wins += 1                                  # suma 1 a user_wins
        else:
            print("Piedra gana a tijera")
            print("El bot gano")
            bot_wins +=1                                    # suma 1 bot_wins
    


    if  bot_wins == 2:
        print("EL GANADOR DEFINITIVO ES EL BOT")
        break                                            # rompe el ciclo while si el bot gana 2 veces
    if  user_wins == 2:
        print("EL GANADOR DEFINITIVO ES EL USUARIO")
        break                                            # rompe el ciclo while si el user gana 2 veces

