#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Due Jan 22, 2021
#button.py
#Class for all the button objects.

# Import local modules.
from global_variables import *

# Class Button.
class Button(pygame.Rect):

    """
    Every rectangle with text inside is an object of class Button. Initalize attributes of button objects. Handle actions when any of them is hovered or clicked. Render the buttons with the positions to the given screen.

    Parameters
    ----------
    text : string
        Stores what is displayed on the button.
    type : string
        If it changes variables of the game like pages.
    click : string
        Value to change the variable to; only if type is not empty.
    can_hover : boolean
        Whether when the mouse is on the button it changes colour.
    x : int
        X position of button on the screen.
    y : int
        Y position of button on the screen.
    w : int
        Width of button.
    h : int
        Height of button.
    colour : tuple
        Colour of text in (r, g, b) format.
    bg : tuple
        Colour of rectangle in (r, g, b) format.
    font_size : int
        Font size of text displayed.
    font_fam : string
        Font family of text displayed.

    Returns
    -------
    None

    """
    def __init__(self, text, type, click, can_hover, x, y, w, h, colour, bg, font_size, font_fam = "ani"):

        # General attributes.
        self.type = type
        self.click = click
        self.can_hover = can_hover
        self.hovered = False

        # Rectangle attributes.
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (x, y, w, h)
        self.bg = bg

        # Font attributes.
        self.font_fam = font_fam
        self.colour = colour
        self.text = text
        self.font = pygame.font.Font(f'./assets/font/{self.font_fam}.ttf', font_size)
        self.font_render = self.font.render(self.text, True, self.colour)
        self.font_render_hover = self.font.render(self.text, True, self.bg)

        # Get the x and y coordinates of the font.
        # Find middle of two points, minus half of font length to center font.

        self.font_x = (self.left + self.right) / 2 - \
        self.font_render.get_rect().width / 2

        self.font_y = (self.bottom + self.top) / 2 - \
        self.font_render.get_rect().height / 2

        # Join both coordinates.
        self.font_dimen = (self.font_x, self.font_y)


    # Update game information when clicked.
    def clicked(self, page, music, level):
        """
        Handles actions when buttons are clicked by verifying type then applying changes.

        Parameters
        ----------
        page : string
            Current page the menu is displaying.
        music : string
            Current song the game is playing.
        level : int
            Current level that is selected by the user.

        Returns
        -------
        tuple/string
            tuple: The updated page, music and level variables.
            string: Whether user chose to start playing the game.

        """

        # If the button clicked was to go to a new page.
        if self.type == "page":
            page = self.click

        # If the button clicked was to change music.
        elif self.type == "music":
            music = self.click

        # If the button clicked was to choose a new level.
        elif self.type == "level":
            level = self.click

        elif self.type == "main":
            # call actual game window.
            return 'Game'

        return [page, music, level]


    # Render the button to the screen given.
    def render(self):
        """
        Render/draw the button to the screen given.

        Parameters
        ----------
        pygame : module
            The pygame module required to draw to the screen.
        screen : pygame surface
            The window every object is drawn/rendered to.

        Returns
        -------
        None

        """

        # Check if hovered.
        if self.hovered and self.can_hover:
            # Draw the rectangle.
            pygame.draw.rect(screen, self.colour, self.rect, 0, 5)
            # Draw the font.
            screen.blit(self.font_render_hover, self.font_dimen)

        # Regular state (not hovered).
        else:
            # Draw the rectangle.
            pygame.draw.rect(screen, self.bg, self.rect, 0, 5)
            # Draw the font.
            screen.blit(self.font_render, self.font_dimen)



# Reference
# https://pythonprogramming.altervista.org/buttons-in-pygame/
