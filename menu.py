
# Import local modules.
from global_variables import *
from menu_render import *
from button import *

# Organize bg images into a dictionary for easier access.
img_bg = {
    "intro": pygame.image.load('./assets/images/bg-new.png'),
    "settings": pygame.image.load('./assets/images/bg-new2.png'),
    "help": pygame.image.load('./assets/images/bg-new2.png'),
    "credits": pygame.image.load('./assets/images/bg-new2.png')
}

# Organize songs into a dictionary for easier access.
music_dict = {
    'coffin': './assets/audio/coffin.wav',
    'polka': './assets/audio/polka.wav',
    'avengers': './assets/audio/avengers.wav',
    'none': './assets/audio/coffin.wav',
}

# Start with this song.
current_music = 'coffin'

# Organize page buttons into a dictionary for easier access.
page = {
    "intro": page_btns['intro'],
    "settings": page_btns['settings'],
    "help": page_btns['help'],
    "credits": page_btns['credits']
}

# Start with this page.
current_page = "intro"

# Generate page buttons with calculated positions.
music_btns(music_dict)
level_btns()
credits_btn()


# Main loop
def main_menu(events, level_num):

    global img_bg
    global music_dict
    global page
    global current_page
    # global level_num
    global current_music
    global current_level

    render_btns(pygame, screen, img_bg[current_page], page_btns[current_page])

    # Check if the mouse hovered over a button.
    mouse_point = pygame.mouse.get_pos()
    update = check_mouse(pygame, screen, current_page, current_music, level_num, page_btns[current_page], mouse_point)

    for event in events:

        # Check if the user clicked somewhere on the window.
        if event.type == pygame.MOUSEBUTTONDOWN:

            # User clicked 'Play Game'.
            if update == 'Game':
                return ['game', level_num]

            # User is still in menu, update any new page/music/level.
            current_page = update[0]
            level_num = update[2]
            print(level_num)

            # If a different music is picked.
            if current_music != update[1]:
                current_music = update[1]

                # If user doesn't want music.
                if current_music == "none":
                    pygame.mixer.music.stop()

                # User wants another song.
                else:
                    pygame.mixer.music.load(music_dict[current_music])
                    pygame.mixer.music.play(-1)

    return ['menu', level_num]



# source
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://pythonprogramming.net/adding-sounds-music-pygame/
