import pygame
import screen
import call_visit
import screen2
import consts
import smile
import food_donate
import donate_money
import recycling

state = {
    "is_window_open": True,
    "first_window_open": True,
    "second_window_open": False,
    "food_window_open": False,
    "money_window_open": False,
    "second_money_window_open": False,
    "recycling_window_open": False,
    "smile_visit_window_open": False
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
        if state["second_money_window_open"]:
            money_handle_user_events()
        if state['recycling_window_open']:
            recycling_handle_user_events()
        if state["smile_visit_window_open"]:
            smile_visit_handle_user_events()
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state["second_window_open"] = False
                state["first_window_open"] = True
                screen.draw_screen()


def food_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            if 70 <= mouse[0] <= 270 and 200 <= mouse[1] <= 300:
                food_donate.tel_aviv()
            if 285 <= mouse[0] <= 485 and 200 <= mouse[1] <= 300:
                food_donate.jerusalem()
            if 500 <= mouse[0] <= 700 and 200 <= mouse[1] <= 300:
                food_donate.petah_tikva()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state["food_window_open"] = False
                state["first_window_open"] = True
                screen.draw_screen()


def money_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            # 50
            if 70 <= mouse[0] <= 320 and 200 <= mouse[1] <= 350:
                state["money_window_open"] = False
                state["second_money_window_open"] = True
                donate_money.second_screen()
                amount = 50
            # 100
            elif 440 <= mouse[0] <= 640 and 200 <= mouse[1] <= 350:
                state["money_window_open"] = False
                state["second_money_window_open"] = True
                donate_money.second_screen()
                amount = 100
            # 200
            elif 70 <= mouse[0] <= 320 and 350 <= mouse[1] <= 500:
                state["money_window_open"] = False
                state["second_money_window_open"] = True
                donate_money.second_screen()
                amount = 200
            # 500
            elif 440 <= mouse[0] <= 640 and 350 <= mouse[1] <= 500:
                state["money_window_open"] = False
                state["second_money_window_open"] = True
                donate_money.second_screen()
                amount = 500


def recycling_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            if 70 <= mouse[0] <= 240 and 150 <= mouse[1] <= 350:
                recycling.if_press_green()
            if 290 <= mouse[0] <= 460 and 150 <= mouse[1] <= 350:
                recycling.if_press_orange()
            if 520 <= mouse[0] <= 690 and 150 <= mouse[1] <= 350:
                recycling.if_press_blue()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state["recycling_window_open"] = False
                state["first_window_open"] = True
                screen.draw_screen()


def smile_visit_handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state["smile_visit_window_open"] = False
                state["first_window_open"] = True
                screen.draw_screen()


def mouse_location():
    return pygame.mouse.get_pos()


def decide(name):
    if name == "call or visit":
        call_visit.create_screen()
        state["smile_visit_window_open"] = True
        state["second_window_open"] = False
    elif name == "smile to the world":
        smile.create_smile_screen()
        state["smile_visit_window_open"] = True
        state["second_window_open"] = False
    elif name == "food donation":
        food_donate.create_screen()
        state["food_window_open"] = True
        state["second_window_open"] = False
    elif name == "donate money":
        donate_money.create_screen()
        state["money_window_open"] = True
        state["second_window_open"] = False
    elif name == 'recycle':
        recycling.create_screen()
        state["second_window_open"] = False
        state['recycling_window_open'] = True



if __name__ == '__main__':
    main()

