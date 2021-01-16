#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Pygame
import pygame

#Import Other Files
#import level_design
#from global_variables.py import *
#from player_data.py import *

pygame.init()

clock = pygame.time.Clock()

#List Variables
#global current_level
obstacles = []

# Set up the drawing window
screen = pygame.display.set_mode([1000, 800])



def check_events(key_list):

    #check all events that happened in this frame
    for event in pygame.event.get():

        # Was a key just pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #if pressed w
                #make the player jump
                key_list[0] = True
            if event.key == pygame.K_a: #if pressed a
                key_list[1] = True
            if event.key == pygame.K_d: #if pressed d
                key_list[2] = True
            if event.key == pygame.K_UP: #if pressed up
                #make the player jump
                key_list[3] = True
            if event.key == pygame.K_LEFT: #if pressed left
                key_list[4] = True
            if event.key == pygame.K_RIGHT: #if pressed right
                key_list[5] = True

        # Was a key just let go
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: #if just stopped pressing w
                #stops jumping
                key_list[0] = False
            if event.key == pygame.K_a: #if just stopped pressing a
                key_list[1] = False
            if event.key == pygame.K_d: #if just stopped pressing d
                key_list[2] = False
            if event.key == pygame.K_UP: #if just stopped pressing up
                #stops jumping
                key_list[3] = False
            if event.key == pygame.K_LEFT: #if just stopped pressing left
                key_list[4] = False
            if event.key == pygame.K_RIGHT: #if just stopped pressing right
                key_list[5] = False
        
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            pygame.quit()
        
    return key_list


class Sprite:
    def __init__(self, x, y, w, h,moveX = 0,moveY = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.moveX = moveX
        self.moveY = moveY
        self.jumping = False
        self.can_jump = True
    
    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), int(self.w), int(self.h))

    #Detects if any sprite it touching the "obstacles" aka walls/floors
    def detectCollisions(self):
        
        global obstacles,red_only,blue_only,Players,current_level

        for i in obstacles:
            #if top left of self is colliding
            if(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y >= i.y):
                
                #if your left side is farther left than their right side (minus X movement)
                if self.x <= i.x + (i.w - 6):#- abs(self.moveX)): #touches more on the top
                    self.y = i.y + i.h
                
                #if your top side is above their bottom side (minus Y movement)
                elif self.y <= i.y + (i.h ):#- abs(self.moveY)): #touches more on the left
                    self.x = i.x + i.w

            #if top right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y >= i.y):

                #if your right side is farther right than their left side
                if self.x >= i.x - (self.w - 6):#- abs(self.moveX)): #touches more on the top
                    self.y = i.y + i.h
                
                #if your top side is above their bottom side
                elif self.y <= i.y + (i.h ):#- abs(self.moveY)): #touches more on the right
                    self.x = i.x - self.w

            #if bottom left of self is colliding
            elif(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                #if your left side is farther left than their right side
                if self.x <= i.x + (i.w - abs(self.moveY)):#- abs(self.moveX)): #touches more on bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False
                
                #if your bottom side is below their top side
                elif self.y <= i.y - (self.h ):#- abs(self.moveY)): #touches more on left
                    self.x = i.x + i.w
                
            #if bottom right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y + self.h >= i.y):
                
                #if your right side is farther right than their left side
                if self.x >= i.x - (self.w - abs(self.moveY)):#- abs(self.moveX)): #touches more on the bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False
                
                #if your bottom side is below their top side
                elif self.y <= i.y + (self.h ):#- abs(self.moveY)): #touches more on the right
                    self.x = i.x - self.w

        for red in red_only:
            #if it is colliding with a red rectagle
            if self.get_rect().colliderect(red.get_rect()):
                #if it is the blue player
                if self == Players[0]:
                    print("Restarting Level...")
                    #restart the level
                    get_player_start(current_level)
        
        for blue in blue_only:
            #if it is colliding with a blue rectagle
            if self.get_rect().colliderect(blue.get_rect()):
                #if it is the red player
                if self == Players[1]:
                    print("Restarting Level...")
                    #restart the level
                    get_player_start(current_level)
                    

    #JOEL REMEMBER TO ADD COMMENTS TO THIS FUNCTION ITS IMPORTANT
    def render(self,colour = (0, 0, 255),collisions = False):
        
        if collisions:
            self.detectCollisions()

        self.x = self.x + self.moveX
        self.y = self.y + self.moveY

        #draws a rectagle with dimentions of self
        pygame.draw.rect(screen, colour, self.get_rect())
        self.moveX = 0
        self.moveY = 0

def main():
    global obstacles
    global current_level # current_level is the level that will constantly be displayed
    global Players

    current_level = testing_level
    Players = get_player_start(current_level) # returns a list of [Player0,Player1]
    
    Player0 = Players[0]
    Player1 = Players[1]

    #Players = [Player0,Player1]

    #keys are w,a,d,up,left,right
    key_list = [False,False,False,False,False,False]

    m0,v0, = 4,5
    m1,v1 = 4,5

    # Run until the user asks to quit
    while True:

        #screen.fill((0,0,0))
        draw_stone_background()

        #check for any events this frame
        key_list = check_events(key_list)
        
        ###########
        # JUMPING #
        ###########

        if key_list[0] == True:
            Player0.jumping = True
        
        if key_list[3] == True:
            Player1.jumping = True

        #if player0 is jumping
        if Player0.jumping == True and Player0.can_jump == True:
            # F = 1 / 2 * mass * velocity ^ 2. 
            F0 = (1 / 2)*m0*(v0**2)
                
            # change the y value
            Player0.moveY -= F0
                
            # constantly reduce velocity
            v0 = v0-1
                
            # object reached its maximum height 
            if v0 < 0: 
                # negative sign is added to counter negative velocity 
                m0 = -0.1
            
            # object is where is began
            if v0 == -6:
                m0,v0 = 4,5
                isJump0 = False
                Player0.can_jump = False
        else: #apply gravity
            Player0.moveY = Player0.moveY + 5
        
        #if player 1 is jumping
        if Player1.jumping == True and Player1.can_jump == True:
            # F = 1 / 2 * mass * velocity ^ 2. 
            F1 = (1 / 2)*m1*(v1**2)
                
            # change the y value
            Player1.moveY -= F1
                
            # constantly reduce velocity
            v1 = v1-1
                
            # object reached its maximum height 
            if v1<0: 
                # negative sign is added to counter negative velocity 
                m1 = -0.1

            # object is where is began
            if v1 == -6:
                m1,v1 = 4,5
                Player1.jumping = False
                Player1.can_jump = False
        else: #apply gravity
            Player1.moveY = Player1.moveY + 5
        
        ############
        # CONTROLS #
        ############

        if key_list[1] == True: #if pressing a
            Player0.moveX = Player0.moveX - 5 #move left
        elif key_list[2] == True: #if pressing d
            Player0.moveX = Player0.moveX + 5 #move right
        
        if key_list[4] == True: #if pressing left
            Player1.moveX = Player1.moveX - 5 #move left
        elif key_list[5] == True: #if pressing right
            Player1.moveX = Player1.moveX + 5 #move right
        
        render_level(current_level)

        Player0.render((0,0,255),True)

        Player1.render((255,0,0),True)

        #pygame.draw.rect(screen, (0, 0, 255), (Player0.x,Player0.y,Player0.w,Player0.h))
        pygame.display.flip()

        clock.tick(50)
        



#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.

#import global_variables.py

# MAP LEGEND

# "." = open sapce
# "x" = map barrier
# "E" = door
# "R" = red only area
# "B" = blue only area
# "0" = player 0 start
# "1" = player 1 start
# "i" = decoration torch


#display = pygame.display.set_mode((800,800))
#pygame.display.set_caption("Map Testing") 
#line above might not be needed

#Map for level one of the game.
#So far this map is mainly going to be used for testing purposes
testing_level = [
#      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
    [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ], #0
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #1
    [ "x",".","x",".","x",".","x",".","x",".",".","x",".","x",".","x",".","x",".","x" ], #2
    [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #3
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #4
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #5   x going across
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #6   y going down
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #7
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #8
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #9
    [ "x",".","x","x",".",".",".",".",".",".",".",".",".",".",".",".","x","x",".","x" ], #10
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #11
    [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #12
    [ "x",".",".",".",".",".",".","i",".",".",".",".","i",".",".",".",".",".",".","x" ], #13
    [ "x","E",".","0",".","B","B","x","x","x","x","x","x","R","R",".","1",".",".","x" ], #14
    [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ]  #15
]

# draws the stone brick background for the entire screen
def draw_stone_background():
    screen.fill((0,0,0))
    brick_colour = (75,75,75)
    
    for y in range(0,800,30):
        for x in range(0,1000,60):
            if y % 60 == 30:
                pygame.draw.rect(screen, brick_colour, (x, y, 56, 26))
            else:
                pygame.draw.rect(screen, brick_colour, (x-30, y, 56, 26))

# draws a small torch
def draw_torch(x,y):
    wood_colour = (60,40,0)
    centre_flame_colour = (200,90,0)
    outer_flame_colour = (200,150,0)

    pygame.draw.rect(screen, wood_colour, (x+22, y+20, 6, 15))
    pygame.draw.rect(screen, outer_flame_colour, (x+19, y+8, 12, 12))
    pygame.draw.rect(screen, centre_flame_colour, (x+21, y+12, 8, 8))

# draws the exit door
def draw_door(x,y):
    wood_colour = (60,40,0)
    black_colour = (0,0,0)

    pygame.draw.rect(screen, black_colour, (x+2, y, 46, 50))
    pygame.draw.rect(screen, wood_colour, (x+2, y, 46, 50))


# get the location of the player starting position. can use for any map
def get_player_start(current_level):
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            
            if current_level[y][x] == "0":
                Player0 = Sprite(x*50, y*50, 40, 50) #player width and height data is stored here
            if current_level[y][x] == "1":
                Player1 = Sprite(x*50, y*50, 40, 50)
    Players = [Player0,Player1]
    return Players
    
#Displays the chosen level to the user
def render_level(level):
    global current_level
    global obstacles
    global red_only
    global blue_only

    obstacles = []
    red_only = []
    blue_only = []

    current_level = level
    for y in range(len(level)):
        for x in range(len(level[0])):
            
            #add walls to obstacles list
            if level[y][x] == "x":
                obstacles.append(Sprite(x*50,y*50,50,50))
            
            #render the door
            if level[y][x] == "E":
                door = Sprite(x*50,y*50,50,50)
                door.render((80, 60, 0))
            
            #render torches
            if level[y][x] == "i":
                draw_torch(x*50,y*50)
            
            #add red/blue only blocks to their respective lists
            if level[y][x] == "R":
                red_only.append(Sprite(x*50,y*50,50,50))
            if level[y][x] == "B":
                blue_only.append(Sprite(x*50,y*50,50,50))
    
    # render in special collidable blocks
    for block in obstacles:
        block.render((150, 150, 150))

    for block in red_only:
        block.render((200, 50, 50))
    for block in blue_only:
        block.render((50, 50, 200))


main()

pygame.quit()