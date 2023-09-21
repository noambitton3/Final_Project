import pygame
import consts
import consts2
import screen


def create_smile_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_smile()
    screen.screen.blit(consts2.PLAY_SMILE_PHOTO, (300, 320))
    smile_explanation(consts2.TEXT_SMILE1, consts2.TEXT_SMILE1_LOCATION, consts2.TEXT_1_3_SIZE)
    smile_explanation(consts2.TEXT_SMILE2, consts2.TEXT_SMILE2_LOCATION, consts2.TEXT_2_SIZE)
    smile_explanation(consts2.TEXT_SMILE3, consts2.TEXT_SMILE3_LOCATION, consts2.TEXT_1_3_SIZE)
    pygame.display.flip()

def draw_title_smile():
    screen.draw_title(consts2.TITLE_SMILE, consts2.TITLE_SMILE_SIZE,
                      consts.STARTING_COLOR, consts2.TITLE_SMILE_LOCATION)


def smile_explanation(text, location, size):
    screen.draw_text(text, size,
                     consts.EXPLAIN_COLOR, location)