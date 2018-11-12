#gameGraphics
#this library will hold everything necessary to display the game's buttons and pieces.
import pygame


def drawPuzzle(screen, size, puzzle, x, y, piece_size):
    
    #define the colors we will use
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    VIOLET = (255, 0, 255)
    GREY = (128, 128, 128)
    ORANGE = (255, 165, 0)

    
    #go through each piece of the array and draw an elipse
    for i in range(0, x):
        for j in range(0, y):
            
            name = puzzle[i][j]
            
            piece_color = BLACK
            piece_fill = 2
            
            #empty space
            if name == 'empty':
                piece_color = BLACK
            elif name == 'floor':
                piece_color = GREY
                piece_fill = 1
            elif name == 'player':
                piece_color = BLUE
                piece_fill = 0
            elif name == 'zombie':
                piece_color = RED
                piece_fill = 0
            elif name == 'finish':
                piece_color = VIOLET
                piece_fill = 0
            elif name == 'move':
                piece_color = GREEN
                piece_fill = 2
            elif name == 'moving':
                piece_color = ORANGE
                piece_fill = 0
            elif name == 'conway':
                piece_color = RED
                piece_fill = 10
            elif name == 'horizontal':
                piece_color = RED
                piece_fill = 5
            elif name == 'vertical':
                piece_color = RED
                piece_fill = 5
            elif name == 'portala':
                piece_color = BLUE
                piece_fill = 5
            elif name == 'portalb':
                piece_color = GREEN
                piece_fill = 5
                
            pixel_x = ((size[0] - (x * piece_size)) / 2) + (i * piece_size)
            pixel_y = ((size[1] - (y * piece_size)) / 2) + (j * piece_size)
            
            pygame.draw.ellipse(screen, piece_color, [pixel_x, pixel_y, piece_size, piece_size], piece_fill)
            
def drawMenu(screen, button_list, size, myfont, menu):
    #draws buttons to screen
    for i in range(len(button_list)):
        btn = button_list[i]
        if btn.menu == menu:
            if not btn.use_image:
                textsurface = myfont.render(btn.text, False, (0, 0, 0))
                pygame.draw.rect(screen, btn.color, [btn.x_pos, btn.y_pos, btn.l, btn.h], 0)
                screen.blit(textsurface, (btn.x_pos, btn.y_pos))
                
def changeButtonColor(btn_list, btn_range, selected):
    #changes all buttons within a range to a set color, then the selected one to a different color
    for i in range(len(btn_list)):
        button = btn_list[i]
        if button.number >= btn_range[0] and button.number <= btn_range[1]:
            button.color = (255, 255, 255)
            if button.number == selected:
                button.color = (128, 128, 128)

def indicateMouseOver(button_list):
    #change color of mouse buttons when cursor is over them
    mouseposition = pygame.mouse.get_pos ()
    mousep_x = mouseposition[0]
    mousep_y = mouseposition[1]
    
    for i in range(len(button_list)):
        btn = button_list[i]
        left = btn.x_pos
        right = btn.x_pos + btn.l
        top = btn.y_pos
        bottom = btn.y_pos + btn.h
        
        if not btn.color == (128, 128, 128):
            if mousep_x > left and mousep_x < right and mousep_y > top and mousep_y < bottom:
            #if mouse pointer is within the coordinate position of a button

                btn.color = (128, 25, 25)
            
            else:
                btn.color = (255, 51, 51)    
    
    
def drawTitle(font, screen, size, content):
    #draws the title at the top of the screen
    textsurface = font.render(content, False, (255, 255, 255))
    
    text_w = textsurface.get_rect().width
    text_h = textsurface.get_rect().height

    screen.blit(textsurface, ((size[0] / 2) - (text_w / 2), 50))