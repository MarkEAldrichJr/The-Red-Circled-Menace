#gameMath
#this library will hold any purely mathematical functions, such as page number math
#or win condition math

import random

def initializePuzzle(x, y):
    #creates the initial blank 2d array used for the game
    
    blank_puzzle = [[0] * x for i in range(y)]
    
    for i in range(x):
        for j in range(y):
            blank_puzzle[i][j] = 'empty'
            
    return blank_puzzle

def randomPuzzle(puzzle, x, y):
    for i in range(x):
        for j in range(y):
            rng = random.randrange(10)
            if rng < 3:
                puzzle [i][j] = 'zombie'
            else:
                puzzle[i][j] = 'floor'
    
    #sets player starting spots
    puzzle[4][4] = 'player'
    puzzle[4][5] = 'player'
    puzzle[5][5] = 'player'
    puzzle[5][4] = 'player'
    
    #sets spots around players to floors
    puzzle[3][4] = 'floor'
    puzzle[4][3] = 'floor'
    puzzle[3][5] = 'floor'
    puzzle[5][3] = 'floor'
    puzzle[6][4] = 'floor'
    puzzle[4][6] = 'floor'
    puzzle[6][5] = 'floor'
    puzzle[5][6] = 'floor'
    
    #set exit point
    puzzle[14][14] = 'finish'
    
    
def findPiece(mouse_x, mouse_y, the_puzzle, size, puzzle_x, puzzle_y, piece_size):
    #convert the x and y position of the mouse into puzzle locations
    #return a list of x and y dimensions and name for selected piece
    
    #sets up initial return in case nothing is selected
    spot_found = [100, 100]
    
    #finds the x coordinate selected by player
    #converts pixel length to coordinate position
    #I have no idea how this math works, but it does, so don't fuck with it.
    x_spot = ((mouse_x - ((size[0] - (puzzle_x * piece_size)) / 2)) - (piece_size / 2)) / piece_size
    
    #round() to 0 decimal places
    x_spot = round(x_spot, 0)
    
    #negative 0 occasionally occurs.  Change to 0 when that happens
    if x_spot == -0:
        x_spot = 0
        
    #change x_spot from float to int
    x_spot = int(x_spot)
    
    #same as above, but for y values
    y_spot = ((mouse_y - ((size[1] - (puzzle_y * piece_size)) / 2)) - (piece_size / 2)) / piece_size
    y_spot = round(y_spot, 0)
    if y_spot == -0:
        y_spot = 0
    y_spot = int(y_spot)
    
    
    print (str(x_spot) + ', ' + str(y_spot)) 
    
    spot_found = [x_spot, y_spot]
    
    return spot_found