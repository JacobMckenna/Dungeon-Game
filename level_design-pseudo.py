


FUNCTION draw_background():

    Loop through the rows
        Loop through the columns
            Draw a stone block with a certain colour in the relative


FUNCTION draw_torch():
    Set colour of the torch's stick and fire
    Draw the torch to the screen with colour and relative positions

FUNCTION draw_exit():
    Set colour of door
    Draw door to the screen

FUNCTION reset_players():
    Loop through the rows in the map
        Loop through the columns places in each row
            Check if a block represents a player
            Player1:
                Reset player1's x and y to spawn location
            Player2:
                Reset player2's x and y to spawn location

    Return players coordinates in a list

FUNCTION exit_location():
    Loop through the rows of the map
        Loop through the columns values of the row
            Check if current block an exit
            Is an exit:
                Store the location of the block in a variable
    Return exit location as list

FUNCTION modify_level(old, new): Handle different
    Loop through the rows of the map
        Loop through the columns values of the row
            Check if old block is found
            Found:
                Replace block symbol with new block symbol from global map variable

FUNCTION render_block_list(blocks_to_render):
    Loop through the blocks to render
        Add the height of the block
        Call object's render method to render to screen

FUNCTION render_level(): Gather all the blocks then call their render methods
    Check if level changed
    Changed:
        Reset player movements


    Loop through the rows in the map
        Loop through the columns in the rows
            Check which type of block needs to be rendered
            Wall:
                Add wall object with coordinates to obstacle list
            Exit:
                Call the draw_exit function to handle rendering the exit locations
            Torch:
                Call the draw_torch function to handle getting rendering the exits
            Blue area (water):
                Add blue block object with coordinates to blue list
            Red area (fire):
                Add blue block object with coordinates to red list
            Pressure plate:
                Add pressure plate object with coordinates to plate list
            Closed door (water):
                Add blue block object with coordinates to obstacle list
            Opened door (water):
                Add to obstacle list a rect object
                Add to door list door with coordinates
            Closed door (water):
                Add to door list door with coordinates

    Call render_block_list to render obstacles, red blocks, blue blocks

    Loop through the plates
        Render the current plate (separate to check if stepped on)

    Make a button that displays the score
    Render the score button

    Return obstacles, red blocks, blue blocks, pressure plates, doors
