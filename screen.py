import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("THE DAILY GOOD")


def draw_screen():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_starting_message()
    screen.blit(consts.PLAY_BUTTON_PHOTO, (225, 150))
    draw_choose()
    draw_explanation()
    pygame.display.flip()


def draw_starting_message():
    draw_title(consts.STARTING_MESSAGE, consts.STARTING_FONT_SIZE,
               consts.STARTING_COLOR, consts.STARTING_LOCATION)


def draw_choose():
    draw_text(consts.CHOOSE_TEXT, consts.CHOOSE_SIZE,
              consts.CHOOSE_COLOR, consts.CHOOSE_LOCATION)


def draw_explanation():
    draw_text(consts.EXPLAIN_TEXT, consts.EXPLAIN_SIZE,
              consts.EXPLAIN_COLOR, consts.EXPLAIN_LOCATION)


def draw_text(message, font_size, color, location):
    font = pygame.font.SysFont(consts.TEXT_FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_title(message, font_size, color, location):
    font = pygame.font.SysFont(consts.TITLE_FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
