import pygame
import screen
import call_visit
import screen2
import consts
import smile

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
            if 225 <= mouse[0] <= 525 and 150 <= mouse[1] <= 350:
                deed = screen2.draw_screen()


def mouse_location():
    return pygame.mouse.get_pos()


def decide(name):
    if name == "call or visit":
        call_visit.create_screen()
    elif name == "smile to the world":
        smile.create_smile_screen()


if __name__ == '__main__':
    main()

