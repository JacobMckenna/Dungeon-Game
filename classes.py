#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Due Jan 22, 2021
#classes.py
#Sprite, Pressure_Plate and Door classes.


from global_variables import *

# Load the images of the two players.
img_player1 = pygame.image.load('./assets/images/player1.png')
img_player2 = pygame.image.load('./assets/images/player2.png')

#Class used for creating obstacles and players
class Sprite:
    """Short summary.

    Parameters
    ----------
    x : int
        X position of object on the screen.
    y : int
        Y position of object on the screen.
    w : int
        Width of object.
    h : int
        Height of object.
    player : boolean
        Whether the object is a player.

    Attributes
    ----------
    moveX : int
        How much to change x by.
    moveY : int
        How much to change y by.
    mass : int
        Mass of the object (for players and gravity).
    velocity : int
        Initial speed of objects (for players and gravity).
    jumping : boolean
        Whether the object is jumping or not.
    can_jump : boolean
        Whether the object is able to jump (handles players and gravity).
    left_level : boolean
        Whether the object is standing on the exit.

    """
    def __init__(self, x, y, w, h, player = 0):
        self.x = x #x coordinate
        self.y = y #y coordinate
        self.w = w #width
        self.h = h #height
        self.moveX = 0 #how far to move x this frame
        self.moveY = 0 #how far to move y this frame

        # Jumping related values:
        self.mass = 4
        self.velocity = 5
        self.jumping = False #the player is not starting jumping
        self.can_jump = True #the player is able to jump

        self.left_level = False #if the player is at the exit

        # Whether object is a player
        self.player = player


    def get_rect(self):
        """
        Creates a pygame.Rect object of self and returns that.

        Returns
        -------
        pygame.Rect object
            Returns a pygame Rect object of the sprite.

        """


        # Returns a pygame Rect object of the sprite.
        return pygame.Rect(int(self.x), int(self.y), int(self.w), int(self.h))



    #Detects if any sprite it touching the "obstacles" aka walls/floors
    def detectCollisions(self, blocks, Players):
        """Short summary.

        Parameters
        ----------
        blocks : list
            List of all the walls, obstacles, doors, plates that the player can collide with.
        Players : list of Sprite objects
            Check which object collided and apply aprpropriate movement changes.

        Returns
        -------
        None
        """

        # Break up the list for easier access.
        obstacles = blocks[0]
        red_only = blocks[1]
        blue_only = blocks[2]
        pressure_plates = blocks[3]
        doors = blocks[4]
        exits = blocks[5]

        # Loop through all walls/floors.
        for i in obstacles:

            # If top left of self is colliding.
            if(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y >= i.y):

                # If your left side is farther left than their right side (minus X movement).
                if self.x <= i.x + (i.w - 6): #touches more on the top
                    self.y = i.y + i.h

                # If your top side is above their bottom side (minus Y movement).
                elif self.y <= i.y + (i.h ): #touches more on the left
                    self.x = i.x + i.w

            # If top right of self is colliding.
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y >= i.y):

                # If your right side is farther right than their left side.
                if self.x >= i.x - (self.w - 6): #touches more on the top
                    self.y = i.y + i.h

                # If your top side is above their bottom side.
                elif self.y <= i.y + (i.h ): #touches more on the right
                    self.x = i.x - self.w

            # If bottom left of self is colliding.
            elif(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                # If your left side is farther left than their right side.
                if self.x <= i.x + (i.w - abs(self.moveY)): #touches more on bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False

                # If your bottom side is below their top side
                elif self.y <= i.y - (self.h ): #touches more on left
                    self.x = i.x + i.w

            # If bottom right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                # If your right side is farther right than their left side
                if self.x >= i.x - (self.w - abs(self.moveY)): #touches more on the bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False

                # If your bottom side is below their top side
                elif self.y <= i.y + (self.h ): #touches more on the right
                    self.x = i.x - self.w

        # Go through all the red only squares
        for red in red_only:
            # If it is colliding with a red rectangle
            if self.get_rect().colliderect(red.get_rect()):
                # If it is the blue player
                if self == Players[0]:

                    # Reset the player positions.
                    for y in range(len(current_level)):
                        # For every block in the column.
                        for x in range(len(current_level[0])):
                            # "0" is the key for Player0 spawn.
                            if current_level[y][x] == "0":
                                Players[0].x = x*50
                                Players[0].y = y*50
                            # "1" is the key for Player1 spawn.
                            if current_level[y][x] == "1":
                                Players[1].x = x*50
                                Players[1].y = y*50

        # Go through all the blue only squares.
        for blue in blue_only:
            # If it is colliding with a blue rectagle.
            if self.get_rect().colliderect(blue.get_rect()):
                # If it is the red player.
                if self == Players[1]:

                    # Reset the player positions.
                    for y in range(len(current_level)):
                        # For every block in the column.
                        for x in range(len(current_level[0])):
                            # "0" is the key for Player0 spawn.
                            if current_level[y][x] == "0":
                                Players[0].x = x*50
                                Players[0].y = y*50
                            # "1" is the key for Player1 spawn.
                            if current_level[y][x] == "1":
                                Players[1].x = x*50
                                Players[1].y = y*50

        # Go through every pressure plate.
        for plate in pressure_plates:
            # If player is touching the plate.
            if self.get_rect().colliderect(plate.rect):
                # Change attribute to change colour.
                plate.active = True

                # Loop through all the doors.
                for door in doors:
                    # Set door to open.
                    door.open = True

        # Check if the players are on the exit.
        if self.get_rect().colliderect((exits[0], exits[1], 50, 50)):
            self.left_level = True
        else:
            self.left_level = False


    def render(self, colour = (0, 0, 255),collisions = False, blocks = (), players = []):
        """
        Check collision and draw the objects to the screen.

        Parameters
        ----------
        colour : tuple
            Holds colour information of object as RGB.
        collisions : boolean
            Whether to check for collisions for the current object.
        blocks : list
            List of objects on screen to render.
        players : list
            Contains the two Sprite object players.

        Returns
        -------
        None
        """

        # If collisions are enabled (only on players).
        if collisions:
            # Check for any collisions and apply movement changes.
            self.detectCollisions(blocks, players)

        # Move the x and y the amount calculated over this frame.
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY

        # If it's not a player.
        if self.player == 0:
            # Draws a rectagle with dimenions of self.
            pygame.draw.rect(screen, colour, self.get_rect())
        if self.player == 1:
            # Draws image of player 0 on the screen.
            screen.blit(img_player1, (self.x, self.y))
        elif self.player == 2:
            # Draws image of player 0 on the screen.
            screen.blit(img_player2, (self.x, self.y))

        # Reset movement to 0 for next frame.
        self.moveX = 0
        self.moveY = 0

    def jump(self):
        """
        Handles force and gravity for movement when jumping.

        Returns
        -------
        None
        """

        # Calculate force on player.
        # Force = 1 / 2 * mass * velocity ^ 2
        F  = (1 / 2)* self.mass * (self.velocity**2)

        # Change the y value.
        self.moveY -= F

        # Constantly reduce velocity (therefore making it an arc shaped jump).
        self.velocity -= 1

        # Object reached the peak of the jump arc.
        if self.velocity == 0:
            # Reset mass and velocity now that the jump is finished.
            self.mass,self.velocity = 4,5
            self.jumping = False #sprite is no longer jumping
            self.can_jump = False #sprite can not jump right away


# Get the location of the player starting position (SPRITE).
def create_player_sprite(current_level):
    """
    Get the location of the player starting position (SPRITE). Called once.

    Parameters
    ----------
    current_level : matrix
        List of lists containing all the objects on the map.

    Returns
    -------
    list
        List of player Sprite objects.

    """

    # Go through the map and where the player's positions, make an object of them.
    for y in range(len(current_level)):

        # Go through the columns of each row.
        for x in range(len(current_level[0])):

            # Check which player is present in that part of the map.
            if current_level[y][x] == "0":
                Player0 = Sprite(x*50, y*50, 40, 50, 1) #player width/height is stored here
            if current_level[y][x] == "1":
                Player1 = Sprite(x*50, y*50, 40, 50, 2)

    # Combine for easier access and return it.
    Players = [Player0,Player1]
    return Players





class Pressure_Plate:
    """
    Holds all pressure plate object attributes and renders them to the screen.

    Parameters
    ----------
    rect : tuple
        Width, height, x and y positions of Sprite object.

    Attributes
    ----------
    active : boolean
        Whether a player is standing on the plate.
    """

    def __init__(self,rect):
        self.rect = rect
        self.active = False

    def render(self):
        """
        Draws the plate to the screen with the desired colour.

        Returns
        -------
        None
        """

        colour = ()

        # If it is pressed down in this frame.
        if self.active:
            # Make it green.
            colour = (0,100,0)
        else:
            # Make it red.
            colour = (100,0,0)

        # Draw a rectagle where the pressure plate's rect is (red if off, green if on).
        pygame.draw.rect(screen, colour, self.rect)






class Door:
    """
    Check if it's open or closed then draw that shape to the screen as either open or closed.

    Parameters
    ----------
    rect : tuple
        Width, height, x and y positions of Sprite object.

    Attributes
    ----------
    open : boolean
        Whether the door is open or closed.
    """

    def __init__(self,rect):
        self.rect = rect #a python rect (x,y,width,hight)
        self.open = False #the door starts closed

    def render(self):
        """
        Draw to the screen as either open or closed.

        Returns
        -------
        None
        """

        global current_level

        # If the door is closed
        if self.open == False:
            # Draw a rectagle where the door is.
            pygame.draw.rect(screen, (255,255,255), self.rect)
            level_design.modify_level("/","|") #replace all "/" (open door) with "|" (closed door)

        # Door is open.
        else:
            level_design.modify_level("|","/") #replace all "|" (open door) with "/" (closed door)

# Import here to avoid circular imports.
import level_design
