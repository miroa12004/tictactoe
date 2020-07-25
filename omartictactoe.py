## Function to display TicTacToe

def display_board(board):
    
    def format_row(row):
        return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'
    
    return print ('\n\n'.join(format_row(row) for row in zip(*[iter(board)]*3)))


def player_input():
    
    #Define the Player choice to choose between X or O
    
    player1marker = " "
    player2marker = "Wrong"
    
    while player1marker not in ["X","x","O","o"]:
         #Ask Player1 to choose X or O
        
        player1marker = input ("Player 1, please choose your marker (X-O):")
        
        if player1marker == "x" or player1marker == "X":
            player1marker = "X"
            player2marker = "O"
        elif player1marker == "o" or player1marker == "O":
            player1marker = "O"
            player2marker = "X"
        else:
            
            print ("Sorry I didn't get that!")
        
    return (player1marker,player2marker)

        
   
def place_marker(board, marker, position):


	#Function to take Marker (X or O) and puts in on the board
    board [position-1] = marker
    return board
    

def win_check(board,mark):
    #Function to check if a player has won

    wincheck = False
    
    if ((board[0]==mark) and (board[1]==mark) and (board[2]==mark) or
       (board[0]==mark) and (board[3]==mark) and (board[6]==mark) or
       (board[0]==mark) and (board[4]==mark) and (board[8]==mark) or
       (board[1]==mark) and (board[4]==mark) and (board[7]==mark) or
       (board[2]==mark) and (board[5]==mark) and (board[8]==mark) or
       (board[2]==mark) and (board[4]==mark) and (board[6]==mark) or
       (board[3]==mark) and (board[4]==mark) and (board[5]==mark) or
       (board[6]==mark) and (board[7]==mark) and (board[8]==mark)):
        wincheck = True
    return wincheck


import random
def choose_first():
    

	#function to randomely choose who goes first
    firstchoice = random.randint(1,2)
    
    if firstchoice == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    #Function to check if the position chosen is free or not
    if board [position-1] == " ":
        return True
    else:
        return False

    


def full_board_check(board):
    #Function to check if the board is full
    isfull = 0
    
    for i in range(0,len(board)):
        if board[i] != " ":
            isfull +=1
        else:
            pass
        
    return isfull==9

def player_choice(board): 

	#Function to check if the player_choice was free or not
    position = "Wrong"
    withinrange = False
    
    while position.isdigit() == False or withinrange == False:
        
        position = input("Please enter your next move:")
        
        if position.isdigit()==False:
            print ("Sorry I didn't get that")
        elif int(position) in range (1,10):
            
            if space_check(board, int(position)):
                return int(position)
            else:
                print ("Sorry Position already taken")
        else:
            print ("Not applicable, Position Out of range")


def replay():
    #Function to check if the players want to play again
    replaycheck = False
    playerinput = " "
    
    while playerinput not in ["Y","y","N","n"]:
        playerinput = input("Do you want a replay? (Y or N)!")
        
        if playerinput == "Y" or playerinput == "y":
            return True
        elif playerinput == "N" or playerinput == "n":
            return False
        else:
            print ("Sorry I didn't get that!")
            ##clear_output()
            print('\n'*100)

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    
    lst = [" "]*9
    player1marker, player2marker = player_input()
    playerturn = choose_first()
    print (f"{playerturn} will go first")
    ready = input("Are you ready to play the game? (Y-N)")
    
    if ready == "Y" or ready == "y":
        game_on = True
    else:
        game_on = False
    
    while game_on == True:
        if playerturn == "Player 1":
            print (f"{playerturn}'s Turn")
             #Player 1 Turn
            
            display_board (lst)
            position = player_choice(lst)
            place_marker(lst,player1marker,position)
            if win_check(lst,player1marker):
                
                #Check if player 1 has won
                display_board (lst)
                print("Congratulations Player 1 has won the game")
                game_on = False
                
                
            elif full_board_check (lst):
                
                #Check if the game has ended in a tie
                display_board (lst)
                print ("The game has ended in a draw")
                game_on = False
                break
            else:
                
                #Switch to Player 2
                playerturn = "Player 2"
 
        # Player2's turn.         
        else:
            
            print (f"{playerturn}'s Turn")
            display_board (lst)
            position = player_choice(lst)
            place_marker(lst,player2marker,position)
            
            if win_check(lst,player2marker):
                
                #Check if Player 2 has won
                display_board (lst)
                print("Congratulations Player 2 has won the game")
                game_on = False
                
            elif full_board_check(lst):
                
                #Check if the game has ended in a tie
                display_board (lst)
                print ("The game has ended in a draw")
                game_on = False
                break
            else:
                
                #Switch to player1
                playerturn = 'Player 1'

    if not replay():
        break