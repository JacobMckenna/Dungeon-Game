#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Other Files
from global_variables import *
from classes import *
from level_design import *
from game import *
from menu import *

# Play intial music.
# pygame.mixer.music.load(music_dict[current_music])
# pygame.mixer.music.play(-1)

#test cases
# test = Sprite(100,48,39,19)
# print(test.y)
# print(pineapple)

# Main
def main():
    global game_state
    global level_num

    Player0, Player1 = create_player_sprite(current_level) # returns a list of [Player0,Player1]


    # Main loop.
    running = True
    while running:
        # Capture events and check if user chose to close the program.
        events = pygame.event.get()
        for event in events:
            # If the user pressed to close the window then stop the program.
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        # Check if the user is in the menu or in game.
        if game_state == "menu":
            game_state, level_num = main_menu(events, level_num)
        elif game_state == "game":
            game_state, level_num = main_game(events, level_num, Player0, Player1)
        else:
            running = False
            pygame.quit()


        #refresh display
        pygame.display.flip()

        #make each frame stay for 50 miliseconds
        clock.tick(50)

main()
