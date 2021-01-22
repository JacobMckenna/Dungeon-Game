
Import everything from global_variables file

Create class Sprite

    METHOD __init__(): Initialize the following variables from self
    from Parameters:
        x, y, w, h, player
        'player' has default value of 0, 1 or 2 represent the players

    from hardcoded:
        set mass to some fixed number
        set velocity to some fixed number
        set is_jumping to False
        set can_jump to True

        set self.player to player

    FUNCTION get_rect(): Returns an instance of pygame.Rect
        Return pygame.Rect(x, y, w, h)

    METHOD detect_collisions(blocks)

        Loop through the blocks on the map
        Check if the player is touching the block
        If top left of player is touching:
            If player is going to left:
                set player x to right of block
            If player is moving top:
                set player y to bottom of block
        If top right of player is touching:
            If player is going to right:
                set player x to left of block
            If player is moving top:
                set player y to bottom of block
        If bottom left of player is touching:
            If player is going to right:
                set player x to right of block
            If player is moving top:
                set player y to top of block
        If bottom right of player is touching:
            If player is going to right:
                set player x to left of block
            If player is moving top:
                set player y to top of block

        Loop through the red blocks (fire)
        Check if the user is inside the read area
        If inside:
            Check if it's blue player
            Blue player:
                Change the player's x and y position to spawn location

        Loop through the blue blocks (water)
        Check if the user is inside the blue area
        If inside:
            Check if it's red player
            Red player:
                Change the player's x and y position to spawn location

        Loop through each pressure plate
        Check if the player is touching a pressure plate
        Touching:
            Make button change colours (to show activated)

            Loop through the doors in the map:
            Make the doors open

        Get location of the exits
        Check if player1 is touching the first exit
        Touching:
            set self attribute exit to True
        Check if player2 is touching the first exit
        Touching:
            set self attribute exit to True


    METHOD render(): Draw the players to the screen
        Check if current self is player
        Is player:
            Check if player is colliding with block
            detect_collisions()

        set object's x to x + moveX
        set object's y to y + moveY

        Check which player it is
        Player1:
            Draw the player as image1 to the screen
        Player2:
            Draw the player as image2 to the screen

        Reset movement for next frame
        object's x to 0
        object's y to 0

    METHOD jump(): Handle jumping movement of players

        Calculate the force to move the player up/down using kinetic energy formula

        Change y of player to current force
        Lower the speed of player by a fixed number

        Check if the velocity is negative and by how much for going up or down
        Negative velocity:
            Make mass negative to counter force
        Velocity less than a fixed number:
            Reset mass and velcoty to original values
            Player finished jumping, set attribute jumping to False
            Player can't jump right away, set can_jump attribute to False


    METHOD create_player(): Creates instances of the two players
        Create an instance of player 1 with a set coordinates
        Create an instance of player 2 with a set coordinates

        Put the two players in a list
        Players = [Player1, Player2]

        Return the Players list


Create class Pressure_Plate:
    METHOD __init__(): Initialize attributes
    Parameters:
        set rect to rect from param
    Hardcoded:
        set active to False

    METHOD render(): Sets the colour of the plate and draws to screen

        Check if a player is standing on plate
        If current player is colliding with plate:
            set plate colour to green
        Else:
            set plate colour to red

        Draw the object to the pygame screen


Create class Door:
    METHOD __init__(): Initialize attributes
    Parameters:
        set object rect to rect from parameter
        set object open to False initally

    METHOD render():
        Check if the door is open
        Door is open:
            Change the door symbol to open for rendering
        Door is closed:
            Change the door symbol to closed for rendering
