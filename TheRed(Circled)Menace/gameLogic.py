#The Red Circled Menace
#Game Logic Library
#this library will contain all non_graphical code necessary to run the board

    
def selectPiece(coordinates, the_grid):
    #updates the board based on the input coordinates
    x = coordinates[0]
    y = coordinates[1]
    
    #if the player is selected, move spaces are added to all empty spaces around it
    if the_grid[x][y] == 'player':
        #first, remove all other move spaces and change all moving spaces to player spaces
        resetBoardToDefault(the_grid)
        
        #change this player space into a moving space
        the_grid[x][y] = 'moving'

        #checks if all spaces around the move piece are valid, then checks if they are floor space.
        #changes floor space to open space
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < 18 and j >= 0 and j < 18:
                    if the_grid[i][j] == 'floor':
                        the_grid[i][j] = 'move'
                        
    #if a move space is selected, moving enemies are updates, move space becomes a player space,
    #all other move spaces become floor spaces, the player move space is removed,
    #and it stabs your balls
    elif the_grid[x][y] == 'move':
        
        #update moving pieces
        conwayPieces(the_grid)
        
        #turns moving pieces and move pieces into floor space
        for i in range(len(the_grid)):
            for j in range(len(the_grid[0])):
                if the_grid[i][j] == 'moving' or the_grid[i][j] == 'move':
                    the_grid[i][j] = 'floor'
                    
        #turns the selected move space into a moving space
        #this is so the player can quickly move pieces around the board
        the_grid[x][y] = 'moving'
        
        #changes floor space around the new move space into move space
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < 18 and j >= 0 and j < 18:
                    if the_grid[i][j] == 'floor':
                        the_grid[i][j] = 'move'
        
        #destroys any pieces that are not supposed to be there.                
        setForDestruction(the_grid)
        
def resetBoardToDefault(board):
    #when a piece is selected, all other pieces are reset to their default state
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'moving':
                board[i][j] = 'player'
            elif board [i][j] == 'move':
                board[i][j] = 'floor'
            
def setForDestruction(the_board):
    #mark zombies or players for deletion
    
    death_list = []
    
    for i in range(len(the_board)):
        for j in range(len(the_board[0])):
            does_it_die = 0
            if the_board[i][j] == 'player' or the_board[i][j] == 'moving':
                #check the board for all players
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        #if a player is near at least two zombies
                        if k >= 0 and k < len(the_board) and l >= 0 and l < len(the_board[0]):
                            if the_board[k][l] == 'zombie' or the_board[k][l] == 'conway':
                                does_it_die = does_it_die + 1
                                #kill the player
                                if does_it_die >= 2:
                                    death_list.append([i, j])
            elif the_board[i][j] == 'zombie' or the_board[i][j] == 'conway' or the_board[i][j] == 'horizontal' or the_board[i][j] == 'vertical':
                #check the board for all zombie types
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        #if the zombie is near at least two players...
                        if k >= 0 and k < len(the_board) and l >= 0 and l < len(the_board[0]):
                            if the_board[k][l] == 'player' or the_board[k][l] == 'moving':
                                does_it_die = does_it_die + 1
                                #kill the zombie
                                if does_it_die >= 2:
                                    death_list.append([i, j])
                                    
    if not len(death_list) == 0:
        killPieces(death_list, the_board)

def killPieces(death_list, the_board):
    #turns marked zombies or player pieces into floop pieces
    #in effect, it 'kills' them
    
    for i in range(len(death_list)):
        the_board[death_list[i][0]][death_list[i][1]] = 'floor'
        
    do_keep = False
    
    for i in range(len(the_board)):
        for j in range(len(the_board[0])):
            if the_board[i][j] == 'moving':
                keep_piece = [i, j]
                do_keep = True
    
    resetBoardToDefault(the_board)
    
    if do_keep:
        x = keep_piece[0]
        y = keep_piece[1]
        the_board[x][y] = 'moving'
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < 18 and j >= 0 and j < 18:
                    if the_board[i][j] == 'floor':
                        the_board[i][j] = 'move'
                    
def conwayPieces(the_board):
    #these zombies move by Conway's Game Of Life on update.
    
    living_list = []
    dead_list = []
    
    for i in range(len(the_board)):
        for j in range(len(the_board[0])):
            
            living = 0
            #R1 - R3 if a living cell borders 2 or 3 living cells, it lives.  Else it dies
            if the_board[i][j] == 'conway':
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k >= 0 and k < len(the_board) and l >= 0 and l < len(the_board[0]):
                            if the_board[k][l] == 'conway':
                                living = living + 1
                
                #the above code counts the center space itself, so it needs to be removed                
                living = living - 1
                if living < 2 or living > 3:
                    dead_list.append([i, j])
                    
            #R4 if an open cell bordered 3 living cells, the cell comes to life
            elif the_board[i][j] == 'floor' or the_board[i][j] == 'move':
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k >= 0 and k < len(the_board) and l >= 0 and l < len(the_board[0]):
                            if the_board[k][l] == 'conway':
                                living = living + 1
                                
                #by definition, the center space will not be counted, so it doesn't need to be removed
                if living == 3:
                    living_list.append([i,j])
                    
    #kill units on the dead list, and bring life to spots on the living list
    for i in range(len(dead_list)):
        the_board[dead_list[i][0]][dead_list[i][1]] = 'floor'
    for i in range(len(living_list)):
        the_board[living_list[i][0]][living_list[i][1]] = 'conway'