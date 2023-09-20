import pygame
import screen
import call_visit
import screen2
import consts

state = {
    "is_window_open": True
}


def main():
    pygame.init()
    screen.draw_screen()
    while state["is_window_open"]:
        handle_user_events()
    pygame.display.flip()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouse_location()
            if 350 <= mouse[0] <= 650 and 275 <= mouse[1] <= 475:
                # screen2.draw_screen()
                call_visit.create_screen()


def mouse_location():
    return pygame.mouse.get_pos()


if __name__ == '__main__':
    main()
