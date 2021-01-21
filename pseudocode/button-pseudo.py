
Import everythig from global_variables file

Create class Button that inherits class pygame.Rect

  FUNCTION __init__(): Initialize the following variables to self
  from Parameters:
    type, click, can_hover, hovered
    x, y, w, h, rect, bg
    font_fam, colour, text, font, font_render, font_render_hover,
    font_x, font_y, font_dimen

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

    FUNCTION render(): Draws the buttons to the given screen
        Check if the button is hovered from its attributes
        If hovered and can_hover both equal to True:
            Font colour and bg colour are inverted.
            Draw the rectangle to the given screen
            Draw the font to the screen to the middle of the rectangle
        If either hovered or can_hover is False:
        Draw the rectangle to the given screen
        Draw the font to the screen to the middle of the rectangle
