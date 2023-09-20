import pygame
import consts
import consts2
import screen


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_call_visit()
    screen.screen.blit(consts2.PLAY_PHONE_PHOTO, (150, 350))
    screen.screen.blit(consts2.PLAY_GRANDMA_PHOTO, (550, 250))
    call_visit_explanation()
    call_visit_down_text()
    pygame.display.flip()

def draw_title_call_visit():
    screen.draw_title(consts2.TITLE_CALL_VISIT, consts.STARTING_FONT_SIZE,
                      consts.STARTING_COLOR, consts.STARTING_LOCATION)


def call_visit_down_text():
    screen.draw_text(consts2.TEXT_CALL_VISIT_DOWN, consts2.TEXT_CV_SIZE_DOWN,
                     consts.EXPLAIN_COLOR, consts2.TEXT_CV_LOCATION_DOWN)


def call_visit_explanation():
    screen.draw_text(consts2.TEXT_CALL_VISIT, consts2.TEXT_CV_SIZE,
                     consts.EXPLAIN_COLOR, consts2.TEXT_CV_LOCATION)