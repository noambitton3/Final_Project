import pygame
import consts
import consts2
import screen


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_food()
    city_food_text1()
    draw_button()
    pygame.display.flip()


def draw_title_food():
    screen.draw_title(consts2.TITLE_FOOD, consts2.TITLE_FOOD_SIZE,
                      consts.STARTING_COLOR, consts2.TITLE_FOOD_LOCATION)


def city_food_text1():
    screen.draw_text(consts2.TEXT_FOOD_1, consts2.TEXT_FOOD_SIZE,
                     consts.EXPLAIN_COLOR, consts2.TEXT_FOOD_LOCATION)


def draw_button():
    screen.screen.blit(consts2.CITY_BUTTON_PHOTO, (70, 200))
    screen.draw_text(consts2.FIRST_BUTTON_TEXT, consts2.FIRST_BUTTON_SIZE,
                     consts2.FIRST_BUTTON_COLOR, consts2.FIRST_BUTTON_LOCATION)
    screen.screen.blit(consts2.CITY_BUTTON_PHOTO, (285, 200))
    screen.draw_text(consts2.SECOND_BUTTON_TEXT, consts2.SECOND_BUTTON_SIZE,
                     consts2.SECOND_BUTTON_COLOR, consts2.SECOND_BUTTON_LOCATION)
    screen.screen.blit(consts2.CITY_BUTTON_PHOTO, (500, 200))
    screen.draw_text(consts2.THIRD_BUTTON_TEXT, consts2.THIRD_BUTTON_SIZE,
                     consts2.THIRD_BUTTON_COLOR, consts2.THIRD_BUTTON_LOCATION)


def go_to_text():
    screen.draw_text(consts2.AFTER_CHOOSE_CITY_TEXT, consts2.AFTER_CHOOSE_CITY_TEXT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.AFTER_CHOOSE_CITY_TEXT_LOCATION)


def city_addresses_tel_aviv():
    screen.draw_text(consts2.TEL_AVIV_ADDRESS, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS_LOCATION)

def city_addresses_jerusalem():
    screen.draw_text(consts2.JERUSALEM_ADDRESS, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS_LOCATION)

def city_addresses_petah_tikva():
    screen.draw_text(consts2.PETAH_TIKVA_ADDRESS, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS_LOCATION)


def tel_aviv():
    create_screen()
    go_to_text()
    city_addresses_tel_aviv()
    pygame.display.flip()


def jerusalem():
    create_screen()
    go_to_text()
    city_addresses_jerusalem()
    pygame.display.flip()



def petah_tikva():
    create_screen()
    go_to_text()
    city_addresses_petah_tikva()
    pygame.display.flip()