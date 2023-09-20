import pygame
import screen
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


if __name__ == '__main__':
    main()
