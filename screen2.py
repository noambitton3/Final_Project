import pygame
import consts
import screen
import volunteer_place


def draw_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    screen.draw_starting_message()
    draw_deed()
    pygame.display.flip()


def draw_deed():
    deed = volunteer_place.random_volunteer(consts.VOLUNTEER_LIST)
    screen.draw_text(deed, consts.DEED_SIZE,
                     consts.DEED_COLOR, consts.DEED_LOCATION)
