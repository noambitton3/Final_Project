import pygame
import consts
import consts2
import screen

state = {
    "is_window_open": True
}

screen_call_visit = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("CALL OR VISIT")


def main_call_visit():
    pygame.init()
    create_screen()
    while state["is_window_open"]:
        handle_user_events()
    pygame.display.flip()


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False


def create_screen():
    pygame.init()
    screen.screen.fill(consts.BACKGROUND_COLOR)
    draw_title_call_visit()
    screen_call_visit.blit(consts2.PLAY_PHONE_PHOTO, (150, 350))
    screen_call_visit.blit(consts2.PLAY_GRANDMA_PHOTO, (550, 250))
    call_visit_explanation()
    call_visit_down_text()
    pygame.display.flip()


def draw_title_call_visit():
    draw_title(consts2.TITLE_CALL_VISIT, consts.STARTING_FONT_SIZE,
               consts.STARTING_COLOR, consts.STARTING_LOCATION)


def draw_title(message, font_size, color, location):
    font = pygame.font.SysFont(consts.TITLE_FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen_call_visit.blit(text_img, location)

def call_visit_down_text():
    text_visit_call(consts2.TEXT_CALL_VISIT_DOWN, consts2.TEXT_CV_SIZE_DOWN,
                    consts.EXPLAIN_COLOR, consts2.TEXT_CV_LOCATION_DOWN)
def call_visit_explanation():
    text_visit_call(consts2.TEXT_CALL_VISIT, consts2.TEXT_CV_SIZE,
              consts.EXPLAIN_COLOR, consts2.TEXT_CV_LOCATION)


def text_visit_call(message, font_size, color, location):
    font = pygame.font.SysFont(consts.TEXT_FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen_call_visit.blit(text_img, location)


if __name__ == '__main__':
    main_call_visit()
