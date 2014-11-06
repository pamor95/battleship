import random
 
board = []
 
#Adds 5 rows to list board[]
for x in range(0,5):
    board.append(["O"] * 5) #adds 5 'O's to each row in list board[]
 
def print_board(board):
    for row in board:       #for loop puts the rows in a grid format
        print (" ".join(row)) #deletes unnecessary formatting of the grid and makes it a clear list of 2 dimensional 'O's
 
print ("Let's play Battleship!")
print_board(board)
 
def random_row(board):      #radomint function randomly creates a number where the battleship is stored.
  return random.randint(0,len(board)-1)
 
def random_col(board):
  return random.randint(0,len(board[0])-1) #board[0] represents first row, so board[0] - 1 represents the length of column in first row.
 
ship_row = random_row(board) #ship_row stores the row number where the battleship is located.
ship_col = random_col(board) #ship_col stores the col number where the battleship is located.
 
print ('The correct row is: %d' % ship_row)
print ('The correct Column is: %d' % ship_col)
 
#Everything from here on should go in your for loop, to ensure turns.
#Be sure to indent!
for turn in range(4): #gives 4 turns to the user to correct the right location of battleship
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
 
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!\n")
        break   #End of the program if user correctly finds the location of battleship
    else:
        if (turn == 3): #if all turns have passed, game is over, end of program!
            print ('Game Over, you have used your all turns.\n')
            break
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.\n")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.\n")
        else:
            print ("You missed my battleship!\n")
            board[guess_row][guess_col] = "X"
    print ('You have used %d turn(s)' % (turn + 1)) #turn+1 because user must not get turn 0,1,2 and 3 instead the user must get turn 1,2,3 and 4.
    print_board(board)
 
print ('The correct row is: %d\n' % ship_row)
print ('The correct Column is: %d\n' % ship_col)