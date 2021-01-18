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

        # was a key just pressed down?
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

        # was a key just let go?
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
            #quit the program
            pygame.quit()
    
    #return a list of all significant keys (either True or False for each)
    return key_list


#class used for creating obstacles and players
class Sprite:
    def __init__(self, x, y, w, h):
        self.x = x #x coordinate
        self.y = y #y coordinate
        self.w = w #width
        self.h = h #height
        self.moveX = 0 #how far to move x this frame
        self.moveY = 0 #how far to move y this frame

        #jumping related values:
        self.mass = 4
        self.velocity = 5
        self.jumping = False #the player is not starting jumping
        self.can_jump = True #the player is able to jump
    
    def get_rect(self):
        #returns a pygame Rect of the sprite
        return pygame.Rect(int(self.x), int(self.y), int(self.w), int(self.h))

    #Detects if any sprite it touching the "obstacles" aka walls/floors
    def detectCollisions(self):
        
        #get all the global lists that this function requires
        global obstacles,red_only,blue_only,Players,current_level,doors
        
        #loop through all walls/floors
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

        #go through all the red only squares
        for red in red_only:
            #if it is colliding with a red rectagle
            if self.get_rect().colliderect(red.get_rect()):
                #if it is the blue player
                if self == Players[0]:
                    print("Restarting Level...")
                    #restart the level
                    reset_players(current_level)
        
        #go through all the blue only squares
        for blue in blue_only:
            #if it is colliding with a blue rectagle
            if self.get_rect().colliderect(blue.get_rect()):
                #if it is the red player
                if self == Players[1]:
                    print("Restarting Level...")
                    #restart the level
                    reset_players(current_level)
        
        #go through every pressure plate
        for button in pressure_plates:
            #if touching a button
            if self.get_rect().colliderect(button.rect):
                #print("Touching a Button")
                button.active = True

                for door in doors:
                    #set door to open
                    door.open = True
        

    def render(self,colour = (0, 0, 255),collisions = False):
        
        #if collisions are enabled (only on players)
        if collisions:
            #check for any collisions
            self.detectCollisions()

        #move the x and y the amount calculated over this frame
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY

        #draws a rectagle with dimentions of self
        pygame.draw.rect(screen, colour, self.get_rect())

        #reset movement to 0 for next frame
        self.moveX = 0
        self.moveY = 0
    
    def jump(self):
        # Force = 1 / 2 * mass * velocity ^ 2
        F  = (1 / 2)* self.mass * (self.velocity**2)
        
        # change the y value
        self.moveY -= F
        
        # constantly reduce velocity (therefore making it an arc shaped jump)
        self.velocity = self.velocity-1
        
        # object reached its maximum height 
        if self.velocity < 0: 
            # negative sign is added to counter negative velocity 
            self.mass = -0.1
        
        # object is where is began
        if self.velocity == -6:
            #reset mass and velocity now that the jump is finished
            self.mass,self.velocity = 4,5
            self.jumping = False #sprite is no longer jumping
            self.can_jump = False #sprite can not jump right away
        



class Pressure_Plate:
    def __init__(self,rect):
        self.rect = rect
        #self.id = id #unused variable
        self.active = False

    def render(self):
        colour = ()
        #print(self.active)

        #if it is pressed down in this frame
        if self.active:
            #make it green
            colour = (0,100,0)
        else:
            #make it red
            colour = (100,0,0)
        
        #draw a rectagle where the pressure plate's rect is (red if off, green if on)
        pygame.draw.rect(screen, colour, self.rect)

class Door:
    def __init__(self,rect):
        self.rect = rect #a python rect (x,y,width,hight)
        self.open = False #the door starts closed
    
    def render(self):
        global current_level

        #if the door is closed
        if self.open == False:
            #draw a rectagle where the door is
            pygame.draw.rect(screen, (255,255,255), self.rect)

            modify_level("/","|") #replace all "/" (open door) with "|" (closed door)
        else: #if the door is open
            modify_level("|","/")#replace all "|" (open door) with "/" (closed door)


# Main
def main():
    global obstacles
    global current_level # current_level is the level that will constantly be displayed
    global Players
    global pressure_plates

    current_level = testing_level
    Players = create_player_sprite(current_level) # returns a list of [Player0,Player1]
    
    #changes player0 and player1 to nicer variables
    Player0 = Players[0]
    Player1 = Players[1]

    #keys are w,a,d,up,left,right
    key_list = [False,False,False,False,False,False]

    # Run until the user asks to quit
    while True:

        #draws the stone brick background
        draw_stone_background()

        #check for any events this frame
        key_list = check_events(key_list)
        
        ###########
        # JUMPING #
        ###########
        
        #if pressing "w"
        if key_list[0] == True and Player0.can_jump == True:
            #make player 0 jump
            Player0.jump()
        else: #apply gravity
            Player0.moveY = Player0.moveY + 5
        
        #if pressing "up"
        if key_list[3] == True and Player1.can_jump == True:
            #make player 1 jump
            Player1.jump()
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
        
        #display the current level
        render_level(current_level)

        #render the players in the map
        Player0.render((0,0,255),True)
        Player1.render((255,0,0),True)

        #render the buttons and doors
        for button in pressure_plates:
            button.render()
        for door in doors:
            door.render()

        #refresh display
        pygame.display.flip()

        #make each frame stay for 50 miliseconds
        clock.tick(50)
        



#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.

#import global_variables.py

# MAP LEGEND

# "." = open sapce
# "x" = map barrier --  CANNOT HAVE 1 BLOCK GAPS OR CAN JUMP THROUGH
# "E" = exit
# "R" = red only area
# "B" = blue only area
# "0" = player 0 start
# "1" = player 1 start
# "i" = decoration torch
# "_" = pressure plate
# "|" = vertical door (shift + \ NOT capital "i")


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
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".","x","x","x","x","x","x","x" ], #7
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #8
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #9
    [ "x",".","x","x",".",".",".",".",".",".",".",".",".","x","x","x","x","x",".","x" ], #10
    [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #11
    [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","_","x" ], #12
    [ "x",".",".",".",".",".",".","i",".",".",".",".","i",".",".",".",".",".","x","x" ], #13
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
    #colour palette
    wood_colour = (60,40,0)
    centre_flame_colour = (200,90,0)
    outer_flame_colour = (200,150,0)

    #draws the parts of the torch
    pygame.draw.rect(screen, wood_colour, (x+22, y+20, 6, 15))
    pygame.draw.rect(screen, outer_flame_colour, (x+19, y+8, 12, 12))
    pygame.draw.rect(screen, centre_flame_colour, (x+21, y+12, 8, 8))

# draws the exit door
def draw_exit(x,y):
    #colour palette
    wood_colour = (60,40,0)
    black_colour = (0,0,0)

    #draws the parts of the exit
    pygame.draw.rect(screen, wood_colour, (x, y, 50, 50))
    pygame.draw.rect(screen, black_colour, (x+10, y+10, 30, 40))

# DONT USE THIS ONE, USE THE ONE BELOW
# get the location of the player starting position (SPRITE).
def create_player_sprite(current_level):
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            
            if current_level[y][x] == "0":
                Player0 = Sprite(x*50, y*50, 40, 50) #player width and height data is stored here
            if current_level[y][x] == "1":
                Player1 = Sprite(x*50, y*50, 40, 50)
    Players = [Player0,Player1]
    return Players

#USE THIS ONE
def reset_players(current_level):
    global Players
    #for every column
    for y in range(len(current_level)):
        #for every value in the column
        for x in range(len(current_level[0])):
            # "0" is the key for Player0 spawn
            if current_level[y][x] == "0":
                Players[0].x = x*50
                Players[0].y = y*50
            # "1" is the key for Player1 spawn
            if current_level[y][x] == "1":
                Players[1].x = x*50
                Players[1].y = y*50
    return Players

#returns the coordinates of the door to exit the map
def get_exit_location(current_level):
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            
            if current_level[y][x] == "E":
                exit = (x*50, y*50)
    return exit

# takes in two values, seraches the map for the first value and if found will change to the second one
def modify_level(old_value, new_value):
    global current_level
    
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            if current_level[y][x] == old_value:
                current_level[y][x] = new_value

#renders the list of blocks with an colour inputed
def render_block_list(list_to_render, R, G, B, height=0):
    for block in list_to_render:
        block.y += height
        block.h -= height
        block.render((R, G, B))

#Displays the chosen level to the user
def render_level(level):
    global current_level
    global obstacles
    global red_only
    global blue_only
    global pressure_plates
    global doors

    #reset sprite lists
    obstacles = []
    red_only = []
    blue_only = []
    pressure_plates = []
    doors = []
    
    #render each block
    if level != current_level:
        reset_players(level)
    current_level = level

    #check each spot in the level
    for y in range(len(level)):
        for x in range(len(level[0])):
            
            #add walls to obstacles list
            if level[y][x] == "x":
                obstacles.append(Sprite(x*50,y*50,50,50))
            
            #render the exit
            elif level[y][x] == "E":
                draw_exit(x*50,y*50)
            
            #render torches
            elif level[y][x] == "i":
                draw_torch(x*50,y*50)
            
            #add red/blue only blocks to their respective lists
            elif level[y][x] == "R":
                red_only.append(Sprite(x*50,y*50,50,50))
            elif level[y][x] == "B":
                blue_only.append(Sprite(x*50,y*50,50,50))
            
            #add pressure plates to their respective lists
            elif level[y][x] == "_":
                pressure_plates.append(Pressure_Plate((x*50,y*50 + 40,50,20)))
            
            #add closed doors to the door and obstacle list
            elif level[y][x] == "|":
                obstacles.append(Sprite(x*50,y*50,50,50))
                doors.append(Door((x*50,y*50,50,50)))
            
            #add opened doors to the door list
            elif level[y][x] == "/":
                doors.append(Door((x*50,y*50,50,50)))
    
    #render the blocks in each list
    render_block_list(obstacles, 150, 150, 150)
    render_block_list(red_only, 200, 50, 50, 10)
    render_block_list(blue_only, 50, 50, 200, 10)

main()

pygame.quit()