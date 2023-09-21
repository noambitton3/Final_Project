import pygame
import consts
import consts2
import screen


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_food()
    city_food_text1()
    pygame.display.flip()


def draw_title_food():
    screen.draw_title(consts2.TITLE_FOOD, consts2.TITLE_FOOD_SIZE,
                      consts.STARTING_COLOR, consts2.TITLE_FOOD_LOCATION)


def city_food_text1():
    screen.draw_text(consts2.TEXT_FOOD_1, consts2.TEXT_FOOD_SIZE,
                     consts.EXPLAIN_COLOR, consts2.TITLE_FOOD_LOCATION)
