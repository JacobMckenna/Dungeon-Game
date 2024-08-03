# Dungeon Game

## Project Description
Dungeon Game was made in a team of 3 as a High School Summative Project. This is a two-player game where you must traverse a 2d level puzzle filled with traps, buttons, and doors.
To win, both players must work together and navigate to the escape door to complete the level. There are three playable levels in this game as well as customizable music.


## Installation
To install Dungeon Game you must:
1. Install the [repository](https://github.com/JacobMckenna/Grade12-CS-Summative/archive/refs/heads/main.zip) on your device.
2. Install [Python](https://www.python.org/downloads/)
3. Use [pip](https://pip.pypa.io/en/stable/) to install [Pygame](https://www.pygame.org/wiki/about)
```bash
pip install pygame
```

After installing the necessary files, you can run main.py using Python to play Dungeon Game.

## How to play Dungeon Game
After installing the necessary files, you can run main.py using Python to play Dungeon Game.

Once you open the game, you will be greeted by a start menu with some music playing. After clicking 'Start' you will be greeted with the main game menu.
Here, you can: choose your preferred music, open credits, view our help page for more info, or play a level. 
To start playing a level, click which one you wish to play, and then click 'Play Game' to begin.

Once you load into the level there will be two players you may control, a red character controlled by the arrow keys, and a blue character controlled by WASD.
There will also be various obstacles that you work around such as red zones, blue zones, buttons, and doors. I'll explain what each obstacle does.
- Red and Blue zones are areas where only the red or blue character of the corresponding color can enter.
For example, the red character can enter red zones, but the blue character cannot and will be respawned if they attempt to enter.
- Buttons are small maroon-colored rectangles on the floor, these buttons will turn green when pressed and will open all doors on the level.
- Doors appear to be white-colored walls. They block your movement until a button is pressed. While it is pressed, they will disappear and can be moved through.
Once a button stops being pressed, all doors will close and will resume blocking your movement.

## Possible Improvements
- Rework the jumping mechanic so that it feels smoother
- Implement proper file structure so that the repository can be navigated more easily
- Reduce function sizes to make the code more modular
- Add a UI function to display when a level has been selected
- Implement a standard naming convention for variable names, file names, and functions
- Add a level designer for players to create their new levels

## Contributors
[***Jacob Mckenna***](https://github.com/jacobmckenna)
- Primarily worked on the level design

[***Joel Harder***](https://github.com/joelharder4)
- Primarily worked on the playable characters

[***Omar el Mabrouk***](https://github.com/envoamr)
- Primarily worked on the user interface

## References
* [Formatting a Readme](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Make a Readme](https://www.makeareadme.com/)
