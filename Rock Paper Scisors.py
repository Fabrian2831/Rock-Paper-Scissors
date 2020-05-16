"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Create a two player script that plays "rock-paper-scissors". 
The input from the users should not be seen on screen.
Rules:

>Paper beats rock
>Rock beats scissors
>Scissors beats paper
The player wins with 3 of 5 games.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
options = "123" #1=Rock, 2=Paper, 3=Scissors
countP1 = 0 #Lleva la cuenta de los puntos del player 1
countP2 = 0 #Lleva la cuenta de los puntos del player 3
pround = 0 #Lleva la cuenta de los rounds jugados
seguirJugando = "1"
while seguirJugando == "1":
    while countP1 < 3 or countP2 < 3:
        print ("Round number:",pround)
        print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
        print ("Player 1 turn")
        print ("Enter a number to pick an option:","1. Rock","2. Paper","3. Scissors",sep="\n")
        #Se asegura que el usuario escoga una de la 1 opciones
        while True:
            player1 = input ()
            if player1 in options:
                break
            else:
                print ("\n"*100)
                print ("Round number:",pround)
                print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
                print ("Player 1 turn")
                print ("Please choose from the following options","1. Rock","2. Paper","3. Scissors",sep="\n")
        print ("\n"*100)
        print ("Round number:",pround)
        print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
        print ("Player 2 turn")
        print ("Enter a number to pick an option:","1. Rock","2. Paper","3. Scissors",sep="\n")
        #Se asegura que el usuario escoga una de la 1 opciones
        while True:
            player2 = input ()
            if player2 in options:
                break
            else:
                print ("\n"*100)
                print ("\n"*100)
                print ("Round number:",pround)
                print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
                print ("Player 2 turn")
                print ("Please choose from the following options:","1. Rock","2. Paper","3. Scissors",sep="\n")        
        print ("\n"*100)
        if player1 in options and player2 in options:
            if player1 == player2:
                print ("Tie!")
                pround = pround + 1     
            elif player1 == "2" and player2 == "1":
                print ("Player 1 wins!!")
                countP1 = countP1 + 1
                pround = pround + 1
            elif player2 == "2" and player1 == "1":
                print ("Player 2 wins!!")
                countP2 = countP2 + 1
                pround = pround + 1
            elif player1 == "1" and player2 == "3":
                print ("Player 1 wins!!")
                countP1 = countP1 + 1
                pround = pround + 1
            elif player2 == "1" and player1 == "3":
                print ("Player 2 wins!!")
                countP2 = countP2 + 1
                pround = pround + 1
            elif player1 == "3" and player2 == "2":
                print ("Player 1 wins!!")
                countP1 = countP1 + 1
                pround = pround + 1
            elif player2 == "3" and player1 == "2":
                print ("Player 2 wins!!")
                countP2 = countP2 + 1
                pround = pround + 1
            if countP1 == 3:
                print ("Round number:",pround)
                print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
                print ("Plyer 1 wins the match!!")
                break
            elif countP2 == 3:
                print ("Round number:",pround)
                print (" Score\n","Player 1:",countP1,"Player 2:",countP2)
                print ("Player 2 wins the match!!")
                break
        else:
            print ("Choose a valid option")
    
    print ("Choose a number to pick an option","1. Play another round","2. Exit",sep="\n")
    seguirJugando = input()
    if (seguirJugando == "1"):
        pround = 0
        countP1 = 0
        countP2 = 0
        print ("\n"*100)
    elif (seguirJugando == "2"):
        break