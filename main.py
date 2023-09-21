import pygame
import screen
import call_visit
import screen2
import consts
import smile
import food_donate
import donate_money

state = {
    "is_window_open": True,
    "first_window_open": True,
    "second_window_open": False,
    "food_window_open": False,
    "money_window_open": False
}


def main():
    pygame.init()
    screen.draw_screen()
    while state["is_window_open"]:
        if state["first_window_open"]:
            first_handle_user_events()
        if state["second_window_open"]:
            second_handle_user_events()
        if state["food_window_open"]:
            food_handle_user_events()
        if state["money_window_open"]:
            money_handle_user_events()
    pygame.display.flip()


def first_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            if 225 <= mouse[0] <= 525 and 150 <= mouse[1] <= 350:
                screen2.draw_screen(screen2.deed)
                state["first_window_open"] = False
                state["second_window_open"] = True


def second_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            if 70 <= mouse[0] <= 320 and 350 <= mouse[1] <= 500:
                decide(screen2.deed)
            if 440 <= mouse[0] <= 690 and 350 <= mouse[1] <= 500:
                screen2.deed = screen2.choose_deed()
                screen2.draw_screen(screen2.deed)


def food_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()


def money_handle_user_events():
    user_text = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode


def mouse_location():
    return pygame.mouse.get_pos()


def decide(name):
    if name == "call or visit":
        call_visit.create_screen()
    elif name == "smile to the world":
        smile.create_smile_screen()
    elif name == "food donation":
        food_donate.create_screen()
        state["food_window_open"] = True
        state["second_window_open"] = False
    elif name == "donate money":
        donate_money.create_screen()
        state["money_window_open"] = True
        state["second_window_open"] = False


if __name__ == '__main__':
    main()

