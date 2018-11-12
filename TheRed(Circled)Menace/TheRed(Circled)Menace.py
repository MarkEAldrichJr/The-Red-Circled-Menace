#The Red Circled Menace

import pygame
import gameLogic
import gameInterface
import gameMath
import gameOSOP
import gameGraphics

def main():
    
    #start pygame
    pygame.init()
    
    #setup pygame's initial font
    pygame.font.init()
    menu_font = pygame.font.SysFont('Comic Sans MS', 24)
    title_font = pygame.font.SysFont('dokchampa', 54)
    
    #define useful colors
    BLACK = (10, 10, 10)
    #set screen details
    screen_info = pygame.display.Info()
    size = (screen_info.current_w, screen_info.current_h)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Red (Circled) Menace")
    
    #set loop conditions
    done = False
    clock = pygame.time.Clock()
    
    Options = gameOSOP.Options()
    Options.getOptions()
    screen = Options.getScreen(screen, size)
    #Options.getVolume()
    
    #puzzle dimensions
    puzzle_x = 18
    puzzle_y = 18
    piece_size = 48
    
    #creates a blank slate puzzle for us to modify and use
    the_puzzle = gameMath.initializePuzzle(puzzle_x, puzzle_y)
    
    #the menu the game will start in
    #menu variable used to determine which interface will be displayed
    menu = "Main Menu"
    
    is_ingame = False #decides when to display puzzle and when to update puzzle
    is_modgame = False #decides when to display puzzle and when to modify puzzle
    active_fill = False #decides when to fill all spaces in modify mode
    playoredit = 'play' 
    button_pressed = 0 #default button ID
    
    title_text = 'The Red (Circled) MENACE'
    
    piece_name = 'empty' #default piece names
    
    button_list = [] #list of all the buttons we will use
    page_number = 0  #default page number for map list
    puzzle_list = [] #list of puzzles available in file
    

    
    
    name_box = gameInterface.InputBox(size[0] - 200, 100, 100, 50, '')
    time_limit_box = gameInterface.InputBox(size[0] - 200, 155, 100, 50, '0')
    win_condition_box = gameInterface.InputBox(size[0] - 200, 210, 100, 50, '1')
    
    input_boxes = [name_box, time_limit_box, win_condition_box]
    
    
    #all the menu buttons will be initialized below this line
    gameInterface.initMenues(size, button_list)
    
    #main gameplay loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user clicked close
                done = True  #exit the game
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #left mouse button released
                    pos = pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    #if mouse is pressed over button, return text
                    button_pressed = gameInterface.findButtonCollision(mouse_x, mouse_y, button_list, menu)
                    
                    #if any button is pressed, do buttonFunctions.
                    if not button_pressed == 0:
                        #100s are for main menu buttons
                        if button_pressed == 101: #quickplay
                            print('quickplay')
                            is_ingame = True
                            menu = 'Quick Play'
                            gameMath.randomPuzzle(the_puzzle, puzzle_x, puzzle_y)
                            
                        elif button_pressed == 103 or button_pressed == 201: #my puzzles
                            print('my puzzles')
                            page_number = 0
                            menu = 'Map Select'
                            puzzle_list = gameOSOP.getPuzzleList('my puzzles')
                            playoredit = 'play'
                            title_text = 'My Puzzles'
                            is_ingame = False
                            
                        elif button_pressed == 106: #options
                            print('options')
                            menu = 'Options'
                            title_text = 'Options'
                            
                        elif button_pressed == 107: #quit
                            print('quit')
                            done = True
                            
                        #200s are for ingame menu buttons
                        elif button_pressed == 301 or button_pressed == 401 or button_pressed == 501 or button_pressed == 601: #return to menu
                            is_ingame = False
                            is_modgame = False
                            menu = 'Main Menu'
                            title_text = 'The Red (Circled) MENACE'
                            
                        #300s are for the make your own puzzle menu
                        elif button_pressed == 302: #save new map
                            print('saving map')
                            
                            gameOSOP.savePuzzle(the_puzzle, name_box.savename, time_limit_box.savename, win_condition_box.savename)
                            
                        elif button_pressed >= 304 and button_pressed <= 313: #piece selection buttons
                            piece_name = gameOSOP.getNamesFromMenu(button_list, button_pressed)
                            piece_name = piece_name.lower()
                            #changes color of button that was selected
                            gameGraphics.changeButtonColor(button_list, [304, 313], button_pressed)
                        
                        #400s are for the Options menu
                        elif button_pressed == 402: #fullscreen button
                            print("fullscreen toggle")
                            is_fullscreen = Options.is_fullscreen
                            if not is_fullscreen:  #game toggles between fullscreen and windowed mode
                                Options.is_fullscreen = 1
                            elif is_fullscreen:
                                Options.is_fullscreen = 0
                            
                            Options.setOptions()    
                            screen = Options.getScreen(screen,size)
                        
                        elif button_pressed >= 511 and button_pressed <= 518: #map selection buttons
                            #if a map button is selected, find the name of the puzzle that was selected,
                            #then load that puzzle to the_puzzle
                            puzzle_name = gameOSOP.getNamesFromMenu(button_list, button_pressed)

                            
                            #load that puzzle to the_puzzle
                            puzzle_information = gameOSOP.loadPuzzle(puzzle_name)
                            the_puzzle = puzzle_information[0]
                            
                            if playoredit == 'edit':
                                #open map editor with the map associated with the above map name.
                                is_modgame = True
                                menu = 'Map Gen'
                                name_box.text = puzzle_name
                                time_limit_box.text = puzzle_information[1]
                                win_condition_box.text  = puzzle_information[2]
                                name_box.txt_surface = menu_font.render(name_box.text, True, name_box.color)
                                time_limit_box.txt_surface = menu_font.render(time_limit_box.text, True, time_limit_box.color)
                                win_condition_box.txt_surface = menu_font.render(win_condition_box.text, True, win_condition_box.color)
                                
                            elif playoredit == 'play':
                                #open game and play map
                                is_ingame = True
                                menu = 'In Game'
                            
                        elif button_pressed == 602: #regenerate random map
                            gameMath.randomPuzzle(the_puzzle, puzzle_x, puzzle_y)
                        
                        #500s are for the selection menu
                            
                        elif button_pressed == 502: #back button
                            if page_number > 0:
                                page_number = page_number - 1
                                
                        elif button_pressed == 503: #forward button
                            if len(puzzle_list) > 8 * (page_number + 1):
                                page_number = page_number + 1
                        
                        elif button_pressed == 504: #make new map button
                            the_puzzle = gameMath.initializePuzzle(18, 18)
                            is_modgame = True
                            menu = 'Map Gen'
                        
                        elif button_pressed == 505: #open map list and select button for edit
                            playoredit = 'edit'
                            title_text = 'Select Puzzle To Edit'
                            
                            
                    button_pressed = 0
                        
                    gameOSOP.addNamesToMenu(button_list, puzzle_list, page_number)
                    
                    #if the player is in the game, have the game find the game piece selected
                    if is_ingame or is_modgame:
                        board_space = gameMath.findPiece(mouse_x, mouse_y, the_puzzle, size, puzzle_x, puzzle_y, piece_size)
                        
                        #make changes to the board based on what was selected
                        x_b = board_space[0]
                        y_b = board_space[1]
                        
                        if x_b >= 0 and y_b >= 0 and x_b < 18 and y_b < 18:
                            if is_ingame:
                                #if we are playing the game, and we select a valid spot, change the pieces based on the player's selection.
                                gameLogic.selectPiece(board_space, the_puzzle)
                            elif is_modgame:
                                #if we are modding the game, change the space to the selected piece type.
                                the_puzzle[x_b][y_b] = piece_name

                #turns off active filling when RMB is released
                elif event.button == 3:
                    print('released RMB')
                    if is_modgame:
                        active_fill = False
                        
            #turns on active filling when RMB is selected            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    print('selected RMB')
                    if is_modgame:
                        active_fill = True
                        
            #run input boxes while the game is in mod mode    
            for box in input_boxes:
                box.handle_event(event)
                    
        for box in input_boxes:
            box.update()
        
        if is_modgame and active_fill:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            board_space = gameMath.findPiece(mouse_x, mouse_y, the_puzzle, size, puzzle_x, puzzle_y, piece_size)
                
            x_b = board_space[0]
            y_b = board_space[1]
                
            if x_b >= 0 and y_b >= 0 and x_b < 18 and y_b < 18:
                the_puzzle[x_b][y_b] = piece_name        
                
        #changes color of button if mouse is over it
        gameGraphics.indicateMouseOver(button_list)     
    
        #ALL GRAPHICAL CHANGES TAKE PLACE BELOW THIS LINE
        #erase all other items on screen
        if menu != 'Map Gen':
            screen.fill(BLACK)
        else:
            screen.fill([64,64,64])
        
        #draw the menu, decided by the string, 'menu'
        gameGraphics.drawMenu(screen, button_list, size, menu_font, menu)
        
        if not is_modgame and not is_ingame:
            gameGraphics.drawTitle(title_font, screen, size, title_text)
            
        #draw input boxes if we are editing a map
        if is_modgame:
            for box in input_boxes:
                box.draw(screen)    
            
        #draw the board when we are in-game
        if is_ingame or is_modgame:
            gameGraphics.drawPuzzle(screen, size, the_puzzle, puzzle_x, puzzle_y, piece_size)
            
            
        pygame.display.flip()
        
        clock.tick(30)
        
    pygame.quit()
    

if __name__ == "__main__":
    main()