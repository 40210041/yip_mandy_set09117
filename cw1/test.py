#cw1.py
#prepare urself for some long af code

# record play history, i.e. the sequence of moves that the players make during a game,
# so that each game that is played can be recorded and replayed.

# undo and redo, again selecting the most appropriate data structures to enable these functionalities.
# implement an algorithm that enables the computer to choose which moves to make during their own turn,
# i.e. a simple AI player.

# Your choice of algorithm for the AI player may be from the literature, or of your own design. Whichever your
# choice you must be able to evaluate and justify your selection of both data structures and algorithms.
# The game should run from the command line, using a text based interface in the first instance.

# PLS LET ME PASS LOL

##########
# SETUP #
#########

#http://www.darkfish.com/checkers/rules.html (rules)

#setup vars
player_1 = "r" #red
player_1K = "R" #Red.
player_2 = "b" #black
player_2K = "B" #BONELESS
move_turn = 0 #var for incrementing turns
current_turn = 0
current_player = ""

#create grid
b_grid = [[' ','b',' ','b',' ','b',' ','b'], #[0][0] to [0][7]
          ['b',' ','b',' ','b',' ','b',' '],
          [' ','b',' ','b',' ','b',' ','b'],
          [' ',' ',' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ',' ','R'],
          ['r',' ','r',' ','r',' ',' ',' '],
          [' ','r',' ','r',' ','r',' ','r'],
          ['r',' ','r',' ','r',' ','r',' ']] #[7][0] to [7][7]


## define functions ##

#print out the rules
def startup_rules():
    print ("Aim to remove all of the opponents pieces!")
    print ("Type 'move' to move a piece")
    print ("Type 'rules' for how to play.")
    print ("Type 'exit' to quit.\n")

#print out how to play
def rules():
    print ("\n* RULES *")
    print ("• You play as Red (r/R), the AI plays as Black(b/B).")
    print ("• Move the pieces diagonally forward to remove the other players pieces.")
    print ("• Type the number of the direction you would like to move.")
    print ("• Moving a piece to the opponents side will make that piece into a King.")
    print ("• King pieces can move back and forth diagonally.\n")

#print board
def print_grid():
    print ("    0   1   2   3   4   5   6   7 ")
    print ("  +-------------------------------+")
    i = 0
    j = 0
    #print same lines 8 times, i and j increment by 1 each loop
    while i < 8:
        print (str(j) + " | "+b_grid[i][0]+" | "+b_grid[i][1]+" | "+b_grid[i][2]+" | "+b_grid[i][3]+" | "+b_grid[i][4]+" | "+b_grid[i][5]+" | "+b_grid[i][6]+" | "+b_grid[i][7]+ " |")
        # to make board look nicer, print different horizontal line
        if i < 7:
            print ("  +---+---+---+---+---+---+---+---+")
        i += 1
        j += 1
    print ("  +-------------------------------+")


########
# GAME #
########

print ("** Now playing: Checkers! **\n")
startup_rules()

user_input = input("Please press enter to start: \n")
while (user_input != 'exit'):
    print_grid()

    #to start game, move a piece
    print ("Type move to move a piece")
    user_input = input("> ")

    if user_input == 'rules':
        rules()

    #if user enters nothing
    elif user_input == '':
        print ("\nNo input...\n")
        pass

    #if user wants to move a piece
    elif user_input == 'move':

        #co-ord to move from
        print("\nPlease enter the co-ordinates of the piece you would like to move: ")
        move_from = input("> ") #input co-ord to move from
        if move_from == 'cancel' or move_from == '':
            print ("Move cancelled...\n")
            pass
        else:
            if move_from == str(""):
                print ("pls enter numbers")
            else:
                split_from = move_from.split(',') #var to split by comma (creates into array)
                split_fromX = int(split_from[0])
                split_fromY = int(split_from[1])

                #co-ord to move to
                print ("\nWhere would you like to move your choice?")
                print ("1   2")
                print ("  "+ player_1 +"  ") ###### change to current_player
                print ("3   4\n")
                move_to = input("Please enter your choice: \n")

                #if user chooses 1
                if (move_to == '1'):
                    if(b_grid[split_fromY - 2][split_fromX - 2] == ' '): #check is space after enemy piece is free
                        print ("There is an enemy piece that you must take:\n")

                        #if the space is last row (0)
                        if ((split_fromY - 2) == 0):
                            b_grid[split_fromY][split_fromX] = ' '
                            b_grid[split_fromY - 1][split_fromX - 1] = ' '
                            b_grid[split_fromY - 2][split_fromX - 2] = (player_1K)

                        else:
                            b_grid[split_fromY][split_fromX] == ' '
                            b_grid[split_fromY - 1][split_fromX - 1] == ' '
                            b_grid[split_fromY - 2][split_fromX - 2] == (player_1)
                    else:

                        #if choice is king piece
                        if (b_grid[split_fromY][split_fromX]) == 'R':
                            if (b_grid[split_fromY - 1][split_fromX - 1]) == " ": #if empty
                                b_grid[split_fromY][split_fromX] = " " #update grid
                                b_grid[split_fromY - 1][split_fromX - 1] = (player_1K)
                            else:
                                print ("This space is not empty\n") #if not empty
                        #if choice is not king
                        elif (b_grid[split_fromY][split_fromX]) == 'r':
                            if (b_grid[split_fromY - 1][split_fromX - 1]) == " ":
                                b_grid[split_fromY][split_fromX] = " "
                                b_grid[split_fromY - 1][split_fromX - 1] = (player_1)
                            else:
                                print ("This space is not empty\n")

                #if user chooses 2
                elif (move_to == '2'):
                    if (b_grid[split_fromY][split_fromX]) == 'R':
                        if (b_grid[split_fromY - 1][split_fromX + 1]) == " ":
                            b_grid[split_fromY][split_fromX] = " "
                            b_grid[split_fromY - 1][split_fromX + 1] = (player_1)
                        else:
                            print ("This space is not empty\n")
                    elif (b_grid[split_fromY][split_fromX]) == 'r':
                        if (b_grid[split_fromY - 1][split_fromX + 1]) == " ":
                            b_grid[split_fromY][split_fromX] = " "
                            b_grid[split_fromY - 1][split_fromX + 1] = (player_1)
                        else:
                            print ("This space is not empty\n")

                #if user chooses 3, king only
                elif (move_to == '3'):
                    if (b_grid[split_fromY][split_fromX]) == 'R':
                        if (b_grid[split_fromY + 1][split_fromX - 1]) == " ":
                            b_grid[split_fromY][split_fromX] = " "
                            b_grid[split_fromY + 1][split_fromX - 1] = (player_1K)
                        else:
                            print ("This space is not empty\n")
                    else:
                        print ("\nOnly King pieces can move backwards!\n")

                #if user chooses 4, king only
                elif (move_to == '4'):
                    if (b_grid[split_fromY][split_fromX]) == 'R':
                        if (b_grid[split_fromY + 1][split_fromX + 1]) == " ":
                            b_grid[split_fromY][split_fromX] = " "
                            b_grid[split_fromY + 1][split_fromX + 1] = "R"
                        else:
                            print ("This space is not empty\n")
                    else:
                        print ("\nOnly King pieces can move backwards!\n")

    #if user wants to see rules
    elif user_input == 'rules':
        rules()

    #if user wants to quit
    else:
        break

#when game ends
print ("\nThanks for playing!\n")
