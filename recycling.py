import pygame
import consts
import consts2
import screen


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_recycling()
    screen.screen.blit(consts2.GREEN_BIN_PHOTO, (70, 150))
    screen.screen.blit(consts2.ORANGE_BIN_PHOTO, (290, 150))
    screen.screen.blit(consts2.BLUE_BIN_PHOTO, (520, 150))
    pygame.display.flip()


def draw_title_recycling():
    screen.draw_title(consts2.RECYCLING_TITLE, consts2.RECYCLING_TITLE_SIZE,
                      consts.STARTING_COLOR, consts2.RECYCLING_TITLE_LOCATION)


def if_press_green():
    create_screen()
