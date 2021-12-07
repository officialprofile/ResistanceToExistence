import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Resistance to Existence")

def set_difficulty(value, difficulty):

    pass

def start_the_game():

    pass

mytheme = pygame_menu.Theme(background_color=pygame_menu.baseimage.BaseImage("img/bg_menu.jpg"),
                title = False,
		title_background_color=(4, 47, 126),
                title_font_shadow=True,
		title_font = pygame_menu.font.FONT_COMIC_NEUE,
                widget_padding=25,
		widget_font_color = (169, 169, 169, 200),
		widget_font = pygame_menu.font.FONT_COMIC_NEUE,
		title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE)

menu = pygame_menu.Menu('Resistance to Existence', 1200, 600, theme = mytheme)
menu.add.selector('Difficulty', [('Easy', 1), ('Hard', 2)], onchange = set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
