
Import everything from global_variables file

Create class Sprite

    FUNCTION __init__(): Initialize the following variables to self
    from Parameters:
        x, y, w, h, player
        'player' has default value of 0, 1 or 2 represent the players



  FUNCTION clicked(): Handle user clicking buttons
    Parameters: page, music, level
    Check which type of button it was with self.type:
    If type is equal to page:
        Change current_page to the page the button goes to
        page = self.click
    If type is equal to music:
        Change current_music to the song the button is given
        page = self.click
    If type is equal to level:
        Change level_num to the level the button is given
        level_num = self.click
    If type is equal to main:
        Change rendering from menu to game
        Return 'Game'

    Return page, music, level in a tuple/list
