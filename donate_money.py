import pygame
import consts
import screen


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_money()
    pygame.display.flip()


def draw_title_money():
    screen.draw_title(consts.MONEY_MESSAGE, consts.MONEY_FONT_SIZE,
                      consts.MONEY_COLOR, consts.MONEY_LOCATION)


def text(user_text):
    text_surface = consts.TEXT_FONT_NAME.render(user_text, True, consts.BLACK)
