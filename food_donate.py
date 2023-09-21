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


def city_addresses1_tel_aviv():
    screen.draw_text(consts2.TEL_AVIV_ADDRESS1, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS1_LOCATION)

def city_addresses1_jerusalem():
    screen.draw_text(consts2.JERUSALEM_ADDRESS1, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS1_LOCATION)

def city_addresses1_petah_tikva():
    screen.draw_text(consts2.PETAH_TIKVA_ADDRESS1, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS1_LOCATION)



def city_addresses2_tel_aviv():
    screen.draw_text(consts2.TEL_AVIV_ADDRESS2, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS2_LOCATION)

def city_addresses2_jerusalem():
    screen.draw_text(consts2.JERUSALEM_ADDRESS2, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS2_LOCATION)

def city_addresses2_petah_tikva():
    screen.draw_text(consts2.PETAH_TIKVA_ADDRESS2, consts2.ADDRESS_SIZE,
                     consts.EXPLAIN_COLOR, consts2.ADDRESS2_LOCATION)


def thank_you_text():
    screen.draw_text(consts2.THANK_YOU_TEXT, consts2.THANK_YOU_TEXT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.THANK_YOU_TEXT_LOCATION)

def shopping_list():
    screen.draw_text(consts2.SHOPPING_LIST_TITLE, consts2.SHOPPING_LIST_TITLE_SIZE,
                     consts.EXPLAIN_COLOR, consts2.SHOPPING_LIST_TITLE_LOCATION)
    screen.draw_text(consts2.PRODUCT_1, consts2.SHOPPING_LIST_PRODUCT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.SHOPPING_LIST_PRODUCT_1_LOCATION)
    screen.draw_text(consts2.PRODUCT_2, consts2.SHOPPING_LIST_PRODUCT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.SHOPPING_LIST_PRODUCT_2_LOCATION)
    screen.draw_text(consts2.PRODUCT_3, consts2.SHOPPING_LIST_PRODUCT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.SHOPPING_LIST_PRODUCT_3_LOCATION)
    screen.draw_text(consts2.PRODUCT_4, consts2.SHOPPING_LIST_PRODUCT_SIZE,
                     consts.EXPLAIN_COLOR, consts2.SHOPPING_LIST_PRODUCT_4_LOCATION)

def tel_aviv():
    create_screen()
    go_to_text()
    city_addresses1_tel_aviv()
    city_addresses2_tel_aviv()
    thank_you_text()
    screen.screen.blit(consts2.NOTE_PHOTO, (540, 290))
    shopping_list()
    pygame.display.flip()


def jerusalem():
    create_screen()
    go_to_text()
    city_addresses1_jerusalem()
    city_addresses2_jerusalem()
    thank_you_text()
    screen.screen.blit(consts2.NOTE_PHOTO, (540, 290))
    shopping_list()
    pygame.display.flip()



def petah_tikva():
    create_screen()
    go_to_text()
    city_addresses1_petah_tikva()
    city_addresses2_petah_tikva()
    thank_you_text()
    screen.screen.blit(consts2.NOTE_PHOTO, (540, 290))
    shopping_list()
    pygame.display.flip()