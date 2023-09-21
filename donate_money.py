import pygame
import consts
import screen
import main
import sys


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_money()
    draw_first_sentence()
    pygame.display.flip()


def draw_title_money():
    screen.draw_title(consts.MONEY_MESSAGE, consts.MONEY_FONT_SIZE,
                      consts.MONEY_COLOR, consts.MONEY_LOCATION)


def draw_first_sentence():
    screen.draw_text(consts.MONEY1, consts.MONEY1_FONT_SIZE,
                      consts.MONEY1_COLOR, consts.MONEY1_LOCATION)
