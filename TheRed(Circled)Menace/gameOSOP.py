#GameOSOP
#OS Operations
#Stupid name, stucking with it

import os
import pygame

class Options:
    #stores the options currently in use
    def __init__ (self):
        self.is_fullscreen = 0
        self.antialiasing_geometry = 0
        self.music_volume = 10
        self.effects_volume = 10
        self.ismuted = 0
        
    def setOptions(self):
        print('set options')
        #saves changes to file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'Options.txt')
        
        options_file = open(filename, 'w')
        
        options_file.write(str(self.is_fullscreen) + '\n')
        options_file.write(str(self.antialiasing_geometry) + '\n')
        options_file.write(str(self.music_volume) + '\n')
        options_file.write(str(self.effects_volume) + '\n')
        options_file.write(str(self.is_muted) + '\n')
        
        options_file.close()
        
    def getOptions(self):
        print('get options')
        #loads settings from file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'Options.txt')
        
        options_file = open(filename, 'r')
        
        self.is_fullscreen = int(options_file.readline())
        print ('Get fullscreen: ' + str(self.is_fullscreen))
        
        self.antialiasing_geometry = int(options_file.readline())
        print('Get AA: ' + str(self.antialiasing_geometry))
              
        self.music_volume = int(options_file.readline())
        print('Get music volume: ' + str(self.music_volume))
        
        self.effects_volume = int(options_file.readline())
        print('Get effect volume: ' + str(self.effects_volume))
        
        self.is_muted = int(options_file.readline())
        print('Get mute sound: ' + str(self.is_muted))
        
        options_file.close()
    def getScreen(self, screen, size):
        #run set options at startup
        if self.is_fullscreen == 1:
            screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(size)
        
        return screen
        

def loadPuzzle(puzzle_name):
    #loads a player map from a save file
    print('loading puzzle ' + puzzle_name)
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'puzzles', 'my puzzles', puzzle_name)
    
    print('loading from directory' + filename)
    
    puzzle_file = open(filename, 'r')
    
    puzzle = []
    
    for i in range(18):
        #read each line individually
        line = puzzle_file.readline()
        
        #remove unuseful text
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace(' ', '')
        line = line.replace("'", "")
        
        #split line into an array, and append array to puzzle.
        lines = line.split(',')
        
        print('line array:' + str(lines))
        
        puzzle.append(lines)
    
    #get last bits of useful info from file
    turn_limit = puzzle_file.readline()
    unit_minimum = puzzle_file.readline()
    
    #close file
    puzzle_file.close()
    
    #returns array with map, max # of turns, and minimum number of pieces needed to win
    puzzle_info = [puzzle, turn_limit, unit_minimum]
    print(str(puzzle_info[0]))
    return(puzzle_info)

def savePuzzle(puzzle, puzzle_name, time_req, win_condition = '0'):
    #saves a player's map to the player_map file
    print('save map to disk')
    
    #find directory location
    directory_name = os.path.dirname(__file__)
    filename = os.path.join(directory_name, 'puzzles', 'my puzzles', puzzle_name)
    print('saving to' + str(filename))
    
    #open location in directory, create if it doesn't exist
    puzzle_file = open(filename, 'w+')
    print('open file')
    
    #copy puzzle to directory
    print('copy map to file')
    for i in range(len(puzzle)):
        line = str(puzzle[i])
        puzzle_file.write(line + '\n')
    
    #copy time limit and win condition to file
    print('copy map req to file')
    puzzle_file.write(time_req + '\n')
    puzzle_file.write(win_condition + '\n')
    print('close file')
    puzzle_file.close()
    print('save file complete')
    
def getPuzzleList(puzzle_file):
    #retrieves a list of all puzzles in a folder and returns an array of strings
    print('Get list of puzzles')
    puzzle_list = []
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'puzzles', puzzle_file)
    
    #read entrues and print map names to console
    print('scanning file')
    with os.scandir(path) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                print('add ' + str(entry))
                puzzle_list.append(entry.name)
    print('returning names')
    return puzzle_list

def addNamesToMenu(button_list, puzzle_list, page_number):
    #uses page number to single out puzzle list names
    #changes names of numbered buttons to match.
    
    for i in range(len(button_list)):
        button = button_list[i]
        
        if button.number >= 511 and button.number <= 518:
            button.text = ''
            for j in range(len(puzzle_list)):
                if button.number - 510 + (8 * page_number) == j + 1:
                    button.text = puzzle_list[j]
                    
def getNamesFromMenu(button_list, numselected):
    for i in range(len(button_list)):
        if button_list[i].number == numselected:
            return button_list[i].text