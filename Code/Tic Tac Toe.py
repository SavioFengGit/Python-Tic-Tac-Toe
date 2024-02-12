# Python Tic Tac Toe game
# Importo il modulo tkinter per creare l'interfaccia grafica
from tkinter import *
# Importo il modulo random per scegliere il giocatore iniziale
import random

# Definisco una funzione che gestisce il turno successivo
def next_turn(row, column):

    # Uso la parola chiave global per accedere alla variabile player
    global player

    # Controllo se il bottone nella riga e colonna specificate è vuoto e se c'è un vincitore
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # Se il giocatore è il primo della lista players
        if player == players[0]:

            # Assegno il simbolo del giocatore al testo del bottone
            buttons[row][column]['text'] = player

            # Controllo se il giocatore ha vinto
            if check_winner() is True:
                # Se ha vinto, cambio il testo dell'etichetta
                label.config(text=(players[0]+" wins"))
            # Controllo se il gioco è in pareggio
            elif check_winner() == "Tie":
                # Se è in pareggio, cambio il testo dell'etichetta
                label.config(text="Tie!")
            # Altrimenti, il gioco continua
            else:
                # Cambio il giocatore con il secondo della lista players
                player = players[1]
                # Cambio il testo dell'etichetta
                label.config(text=(players[1]+" turn"))

        # Se il giocatore è il secondo della lista players
        else:

            # Assegno il simbolo del giocatore al testo del bottone
            buttons[row][column]['text'] = player

            # Controllo se il giocatore ha vinto
            if check_winner() is True:
                # Se ha vinto, cambio il testo dell'etichetta
                label.config(text=(players[1]+" wins"))
            # Controllo se il gioco è in pareggio
            elif check_winner() == "Tie":
                # Se è in pareggio, cambio il testo dell'etichetta
                label.config(text="Tie!")
            # Altrimenti, il gioco continua
            else:
                # Cambio il giocatore con il primo della lista players
                player = players[0]
                # Cambio il testo dell'etichetta
                label.config(text=(players[0]+" turn"))

# Definisco una funzione che controlla se c'è un vincitore
def check_winner():

    # Check righe
    for row in range(3):
        # Se i tre bottoni nella stessa riga hanno lo stesso testo diverso da vuoto
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Cambio il colore dei bottoni in verde
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            # Restituisco True, cioè c'è un vincitore
            return True

    # Check colonne
    for column in range(3):
        # Se i tre bottoni nella stessa colonna hanno lo stesso testo diverso da vuoto
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # Cambio il colore dei bottoni in verde
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            # Restituisco True, cioè c'è un vincitore
            return True

    # Check diagonale principale
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # Cambio il colore dei bottoni in verde
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        # Restituisco True, cioè c'è un vincitore
        return True

    # Check diagonale secondaria
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # Cambio il colore dei bottoni in verde
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        # Restituisco True, cioè c'è un vincitore
        return True

    # Check spazi vuoti
    elif empty_spaces() is False:

        # Se non ci sono spazi vuoti, il gioco è in pareggio
        for row in range(3):
            for column in range(3):
                # Cambio il colore dei bottoni in giallo
                buttons[row][column].config(bg="yellow")
        # Restituisco "Tie", cioè il gioco è in pareggio
        return "Tie!"

    # Altrimenti, il gioco non è finito
    else:
        # Restituisco False, cioè non c'è un vincitore
        return False


# Definisco una funzione che controlla se ci sono spazi vuoti
def empty_spaces():

    # Inizializzo una variabile spaces a 9, il numero totale di caselle
    spaces = 9

    # Scorro le righe e le colonne
    for row in range(3):
        for column in range(3):
            # Se il bottone nella riga e colonna corrente ha un testo diverso da vuoto
            if buttons[row][column]['text'] != "":
                # Decremento la variabile spaces di 1
                spaces -= 1

    # Se la variabile spaces è 0, non ci sono spazi vuoti
    if spaces == 0:
        # Restituisco False
        return False
    # Altrimenti, ci sono spazi vuoti
    else:
        # Restituisco True
        return True

# Definisco una funzione che inizia una nuova partita
def new_game():

    # Uso la parola chiave global per accedere alla variabile player
    global player

    # Scelgo un giocatore casuale tra i due della lista players
    player = random.choice(players)

    # Cambio il testo dell'etichetta con il turno del giocatore
    label.config(text=player+" turn")

    # Scorro le righe e le colonne
    for row in range(3):
        for column in range(3):
            # Resetto il testo e il colore dei bottoni
            buttons[row][column].config(text="",bg="#F0F0F0")


# Creo una finestra con un titolo
window = Tk()
window.title("Tic-Tac-Toe")
# Creo una lista con i due simboli dei giocatori
players = ["x","o"]
# Scelgo un giocatore casuale tra i due della lista players
player = random.choice(players)
# Creo una matrice di bottoni vuota
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# Creo una etichetta con il testo del turno del giocatore 
label = Label(text=player + " turn", font=('consolas',40))
# Posiziono l'etichetta sopra la finestra
label.pack(side="top")

# Creo un pulsante con il testo "restart"
reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# Posiziono il pulsante sopra la finestra
reset_button.pack(side="top")

# Creo un frame nella finestra
frame = Frame(window)
# Posiziono il frame nella finestra
frame.pack()

# Scorro le righe e le colonne
for row in range(3):
    for column in range(3):
        # Creo un bottone nel frame con un testo vuoto, un font, una larghezza, un'altezza e un comando
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        # Posiziono il bottone nella griglia del frame
        buttons[row][column].grid(row=row,column=column)

# Avvio il ciclo degli eventi della finestra
window.mainloop()


# Author Xiao Li Savio Feng