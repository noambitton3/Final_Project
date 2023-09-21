import pygame
import consts
import screen
import main
import sys


def create_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_money()
    draw_first_sentence()
    draw_button()
    while main.state["money_window_open"]:
        main.money_handle_user_events()
    pygame.display.flip()


def second_screen():
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_money()
    draw_second_sentence()
    pygame.display.flip()


def draw_title_money():
    screen.draw_title(consts.MONEY_MESSAGE, consts.MONEY_FONT_SIZE,
                      consts.MONEY_COLOR, consts.MONEY_LOCATION)


def draw_first_sentence():
    screen.draw_text(consts.MONEY1, consts.MONEY1_FONT_SIZE,
                     consts.MONEY1_COLOR, consts.MONEY1_LOCATION)


def draw_second_sentence():
    screen.draw_text(consts.MONEY2, consts.MONEY2_FONT_SIZE,
                     consts.MONEY2_COLOR, consts.MONEY2_LOCATION)


def draw_button():
    # # left top
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (70, 200))
    screen.draw_text(consts.NUM50_BUTTON_TEXT, consts.NUM50_BUTTON_SIZE,
                     consts.NUM50_BUTTON_COLOR, consts.NUM50_BUTTON_LOCATION)
    # # right top
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (440, 200))
    screen.draw_text(consts.NUM100_BUTTON_TEXT, consts.NUM100_BUTTON_SIZE,
                     consts.NUM100_BUTTON_COLOR, consts.NUM100_BUTTON_LOCATION)
    # right bottom
    screen.screen.blit(consts.MONEY_BUTTON_PHOTO, (440, 350))
    screen.draw_text(consts.NUM500_BUTTON_TEXT, consts.NUM500_BUTTON_SIZE,
                     consts.NUM500_BUTTON_COLOR, consts.NUM500_BUTTON_LOCATION)
    # left bottom
    screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (70, 350))
    screen.draw_text(consts.NUM200_BUTTON_TEXT, consts.NUM200_BUTTON_SIZE,
                     consts.NUM200_BUTTON_COLOR, consts.NUM200_BUTTON_LOCATION)

    def draw_button2():
        # # left top
        screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (70, 200))
        screen.draw_text(consts.NUM50_BUTTON_TEXT, consts.NUM50_BUTTON_SIZE,
                         consts.NUM50_BUTTON_COLOR, consts.NUM50_BUTTON_LOCATION)
        # # right top
        screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (440, 200))
        screen.draw_text(consts.NUM100_BUTTON_TEXT, consts.NUM100_BUTTON_SIZE,
                         consts.NUM100_BUTTON_COLOR, consts.NUM100_BUTTON_LOCATION)
        # right bottom
        screen.screen.blit(consts.MONEY_BUTTON_PHOTO, (440, 350))
        screen.draw_text(consts.NUM500_BUTTON_TEXT, consts.NUM500_BUTTON_SIZE,
                         consts.NUM500_BUTTON_COLOR, consts.NUM500_BUTTON_LOCATION)
        # left bottom
        screen.screen.blit(consts.SCREEN_2_BUTTON_PHOTO, (70, 350))
        screen.draw_text(consts.NUM200_BUTTON_TEXT, consts.NUM200_BUTTON_SIZE,
                         consts.NUM200_BUTTON_COLOR, consts.NUM200_BUTTON_LOCATION)

