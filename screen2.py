import pygame
import consts
import screen
import volunteer_place


def draw_screen(deed):
    screen.screen.fill(consts.BACKGROUND_COLOR)
    screen.draw_starting_message()
    draw_deed(deed)
    draw_button()
    pygame.display.flip()


def choose_deed():
    return volunteer_place.random_volunteer(consts.VOLUNTEER_LIST)


deed = choose_deed()


def draw_deed(deed):
    screen.draw_text(deed, consts.DEED_SIZE,
                     consts.DEED_COLOR, consts.DEED_LOCATION)


def draw_button():
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (70, 350))
    screen.draw_text(consts.LEFT_BUTTON_TEXT, consts.LEFT_BUTTON_SIZE,
                     consts.LEFT_BUTTON_COLOR, consts.LEFT_BUTTON_LOCATION)
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (440, 350))
    screen.draw_text(consts.RIGHT_BUTTON_TEXT, consts.RIGHT_BUTTON_SIZE,
                     consts.RIGHT_BUTTON_COLOR, consts.RIGHT_BUTTON_LOCATION)

