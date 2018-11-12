#all code for the game's menu and menu functions

import pygame

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class InputBox:
    #the box where players can input data for the map (name, turns, win condition, etc)
    def __init__(self, x, y, w, h, text = ''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.savename = text
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
                #save the text for use when saving.
                self.savename = self.text
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.savename = self.text
                    print(self.text)
                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        
class Button:
    #parent of all buttons in game
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.l = 100
        self.h = 50
        self.color = (255, 51, 51)
        self.text = ''
        self.image = ''
        
        #tells program to either display image or graphic
        self.use_image = False
        self.menu = 'main'
        
        #unique button identifier split into 3 digits
        #1st digit is menu (main, ingame, mapmaker, endgame, map selection, and options)
        #2nd and 3rd digits are markers 00-99 for each button.  
        self.number = 0
        
        #create an image at the set location
        if self.use_image == False:
            self.image = pygame.Surface([self.l, self.h])
            self.image.fill(self.color)
        
        else:
            button_image = pygame.image.load(self.image).convert()
        self.rect = self.image.get_rect()
        
def makeButton(button, button_list, text, menu, number, use_image, x, y, length = 100, height = 50, image = ''):
    #creates buttons
    button.x_pos = x #top left corner coordinates
    button.y_pos = y
    button.l = length #length and height
    button.h = height
    button.text = text #text (used to identify button)
    button.menu = menu #which menu the button appears in
    button.use_image = use_image #whether it uses an image or a graphic
    button.image = image #what image will be used
    button.number = number
    button_list.append(button)
    
def findButtonCollision(x, y, button_list, menu):
    #find out which buttons are under the x and y mouse position
    #returns button text
    for i in range(len(button_list)):
        
        btn = button_list[i]
        
        if btn.menu == menu:
            left = btn.x_pos
            right = btn.x_pos + btn.l
            top = btn.y_pos
            bottom = btn.y_pos + btn.h
            
            if x > left and x < right:
                if y > top and y < bottom:
                    return btn.number
    return 0

def initMenues(size, button_list):
    #saves all menues to one list, to be drawn as-needed
    mainMenu(size, button_list)
    ingameMenu(size, button_list)
    mapmakerMenu(size, button_list)
    #endgameMenu(size, button_list)
    mapselectMenu(size, button_list)
    quickplayMenu(size, button_list)
    optionsMenu(size, button_list)
    
def mainMenu(size, button_list):
    #make_button(button, button_list, text, menu, use_image, x, y, length, height, image
    btn_width = size[0] / 4
    btn_x_pos = (size[0] / 2) - (btn_width / 2)
    
    #7 buttons taking up 80% of vertical space 
    btn_height = ((size[1] - 150) * 0.8) / 6
    btn_separation = ((size[1] - 150) * 0.2) / 6
    ti_space = 150
    btn_size = btn_height + btn_separation
    
    quickplay_button = Button()
    makeButton(quickplay_button, button_list, 'QUICKPLAY', 'Main Menu', 101, False, btn_x_pos, ti_space + (btn_size * 1), btn_width, btn_height)
    
    my_puzzle_button = Button()
    makeButton(my_puzzle_button, button_list, 'MY PUZZLES', 'Main Menu', 103, False, btn_x_pos, ti_space + (btn_size * 2), btn_width, btn_height)
    
    options_button = Button()
    makeButton(options_button, button_list, 'OPTIONS', 'Main Menu', 106, False, btn_x_pos, ti_space + (btn_size * 3), btn_width, btn_height)
               
    exit_button = Button()
    makeButton(exit_button, button_list, 'EXIT', 'Main Menu', 107, False, btn_x_pos, ti_space + (btn_size * 4), btn_width, btn_height)
    
def ingameMenu(size, button_list):
    #menu that displayes alongside the puzzle
    
    return_button = Button()
    makeButton(return_button, button_list, 'RETURN', 'In Game', 201, False, size[0] - 100, 100, 100, 100)
    
def quickplayMenu(size, button_list):
    
    return_button = Button()
    makeButton(return_button, button_list, 'RETURN', 'Quick Play', 601, False, size[0] - 100, 100, 100, 100)
    
    random_regen_button = Button()
    makeButton(random_regen_button, button_list, 'REGENERATE', 'Quick Play', 602, False, size[0] - 100, 250, 100, 100)

def mapmakerMenu(size, button_list):
    #buttons for making your own maps
    
    #exit the map generator
    return_button = Button()
    makeButton(return_button, button_list, 'RETURN', 'Map Gen', 301, False, size[0] - 150, 5, 100, 50)
    
    #save your map
    save_button = Button()
    makeButton(save_button, button_list, 'SAVE', 'Map Gen', 302, False, size[0] - 300, 60, 100, 50)
    
    #buttons to add items to the map
    erase_button = Button()
    makeButton(erase_button, button_list, 'EMPTY', 'Map Gen', 304, False, 50, 50, 100, 50)
    
    floor_button = Button()
    makeButton(floor_button, button_list, 'FLOOR', 'Map Gen', 305, False, 50, 105, 100, 50)
    
    player_button = Button()
    makeButton(player_button, button_list, 'PLAYER', 'Map Gen', 306, False, 50, 160, 100, 50)
    
    zombie_button = Button()
    makeButton(zombie_button, button_list, 'ZOMBIE', 'Map Gen', 307, False, 50, 215, 100, 50)
    
    end_button = Button()
    makeButton(end_button, button_list, 'FINISH', 'Map Gen', 308, False, 50, 270, 100, 50)
    
    conway_button = Button()
    makeButton(conway_button, button_list, 'CONWAY', 'Map Gen', 309, False, 50, 325, 100, 50)
    
    hor_button = Button()
    makeButton(hor_button, button_list, 'HORIZONTAL', 'Map Gen', 310, False, 50, 380, 100, 50)
    
    ver_button = Button()
    makeButton(ver_button, button_list, 'VERTICAL', 'Map Gen', 311, False, 50, 435, 100, 50)
    
    a_button = Button()
    makeButton(a_button, button_list, 'PORTALA', 'Map Gen', 312, False, 50, 490, 100, 50)
    
    b_button = Button()
    makeButton(b_button, button_list, 'PORTALB', 'Map Gen', 313, False, 50, 545, 100, 50)
    
def endgameMenu(size, button_list):
    
    restart_button = Button()
    save_score_button = Button()
    return_button = Button()
    
def mapselectMenu(size, button_list):
    #make_button(button, button_list, text, menu, number, use_image, x, y, length, height, image
    
    return_button = Button()
    makeButton(return_button, button_list, 'RETURN', 'Map Select', 501, False, size[0] - 105, 5, 100, 50)
    
    #menu button spots math
    width = size[0] / 4
    r1_left = (size[0] / 2) - width - (size[0] / 64)
    r2_left = (size[0] / 2) + (size[0] / 64)
    
    ti_space = 50
    height = ((size[1] - ti_space) * 0.8) / 6
    space = (size[1] / 32)
    b_height = height + space
    
    #buttons for menu items
    menu_one_button = Button()
    makeButton(menu_one_button, button_list, '', 'Map Select', 511, False, r1_left, ti_space + b_height, width, height)
    
    menu_two_button = Button()
    makeButton(menu_two_button, button_list, '', 'Map Select', 512, False, r1_left, ti_space + (b_height * 2), width, height)
    
    menu_three_button = Button()
    makeButton(menu_three_button, button_list, '', 'Map Select', 513, False, r1_left, ti_space + (b_height * 3), width, height)
    
    menu_four_button = Button()
    makeButton(menu_four_button, button_list, '', 'Map Select', 514, False, r1_left, ti_space + (b_height * 4), width, height)
    
    menu_five_button = Button()
    makeButton(menu_five_button, button_list, '', 'Map Select', 515, False, r2_left, ti_space + b_height, width, height)
    
    menu_six_button = Button()
    makeButton(menu_six_button, button_list, '', 'Map Select', 516, False, r2_left, ti_space + (b_height * 2), width, height)
    
    menu_seven_button = Button()
    makeButton(menu_seven_button, button_list, '', 'Map Select', 517, False, r2_left, ti_space + (b_height * 3), width, height)
    
    menu_eight_button = Button()
    makeButton(menu_eight_button, button_list, '', 'Map Select', 518, False, r2_left, ti_space + (b_height * 4), width, height)
    
    back_button = Button()
    makeButton(back_button, button_list, 'BACK', 'Map Select', 502, False, r1_left, ti_space + (b_height * 5), width / 2, height * (3/4))
    
    forward_button = Button()
    makeButton(forward_button, button_list, 'FORWARD', 'Map Select', 503, False, r2_left + (width / 2), ti_space + (b_height * 5), width / 2, height * (3/4))
    
    #button to make new map
    new_button = Button()
    makeButton(new_button, button_list, 'NEW', 'Map Select', 504, False, size[0] - 105, 60, 100, 50)
    
    edit_button = Button()
    makeButton(edit_button, button_list, 'EDIT', 'Map Select', 505, False, size[0] - 105, 115, 100, 50)
    
def optionsMenu(size, button_list):
    #the options menu, with options such as sound volume and fullscreen toggle
    return_button = Button()
    makeButton(return_button, button_list, 'RETURN', 'Options', 401, False, size[0] - 150, 50, 100, 50)
    
    fullscreen_button = Button()
    makeButton(fullscreen_button, button_list, 'FULLSCREEN TOGGLE', 'Options', 402, False, size[0] / 2 - 100, 150, 400, 50)
    
    aa_button = Button()
    makeButton(aa_button, button_list, 'GEOMETRIC AA', 'Options', 403, False, size[0] / 2 - 100, 250, 400, 50)
    
    music_up_button = Button()
    makeButton(music_up_button, button_list, '+', 'Options', 404, False, size[0] / 2 - 100, 350, 75, 50)
    
    music_down_button = Button()
    makeButton(music_down_button, button_list, '-', 'Options', 405, False, size[0] / 2 + 25, 350, 75, 50)