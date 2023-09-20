import pygame
import consts
import screen


def draw_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    screen.draw_starting_message()
    pygame.display.flip()
