import pygame
import consts
import screen
import volunteer_place


def draw_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    screen.draw_starting_message()
    deed = draw_deed()
    draw_button()
    pygame.display.flip()
    return deed


def draw_deed():
    deed = volunteer_place.random_volunteer(consts.VOLUNTEER_LIST)
    screen.draw_text(deed, consts.DEED_SIZE,
                     consts.DEED_COLOR, consts.DEED_LOCATION)
    return deed


def draw_button():
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (100, 450))
    screen.draw_text(consts.LEFT_BUTTON_TEXT, consts.LEFT_BUTTON_SIZE,
                     consts.LEFT_BUTTON_COLOR, consts.LEFT_BUTTON_LOCATION)
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (550, 450))
    screen.draw_text(consts.RIGHT_BUTTON_TEXT, consts.RIGHT_BUTTON_SIZE,
                     consts.RIGHT_BUTTON_COLOR, consts.RIGHT_BUTTON_LOCATION)

