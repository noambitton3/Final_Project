import pygame

TITLE_CALL_VISIT = "Call or Visit"
TEXT_CALL_VISIT = "Do something simple: Call your grandparents, friends, visit your family..."
TEXT_CALL_VISIT_DOWN = "Even the smallest action can change someone's day!"
TEXT_CV_SIZE = 22
TEXT_CV_LOCATION = (75, 150)
TEXT_CV_LOCATION_DOWN = (95, 440)
TEXT_CV_SIZE_DOWN = 25
PLAY_PHONE_PHOTO = pygame.image.load('phone.png')
PLAY_PHONE_PHOTO = pygame.transform.scale(PLAY_PHONE_PHOTO, (200, 150))
PLAY_GRANDMA_PHOTO = pygame.image.load('grandma.png')
PLAY_GRANDMA_PHOTO = pygame.transform.scale(PLAY_GRANDMA_PHOTO, (200, 250))

TITLE_SMILE = 'Smile to the world'
TEXT_SMILE1 = 'If you go outside today,'
TEXT_SMILE2 = 'Smile !'
TEXT_SMILE3 = "It can make someone's day!"
TITLE_SMILE_SIZE = 70
TITLE_SMILE_LOCATION = (90, 20)
TEXT_SMILE1_LOCATION = (150,120)
TEXT_SMILE2_LOCATION = (270,190)
TEXT_SMILE3_LOCATION = (120,270)
TEXT_1_3_SIZE = 50
TEXT_2_SIZE = 80
PLAY_SMILE_PHOTO = pygame.image.load('smile_2.png')
PLAY_SMILE_PHOTO = pygame.transform.scale(PLAY_SMILE_PHOTO, (170, 170))


# food donate dict
FOOD_CITY_DICT = {"Tel Aviv": ["ארגון לתת- המסגר 44",
                               "חסדי נעמי- תשרי 54"],
                  'Jerusalem': ['מאיר פנים- הצבי 11',
                                'מזון לחיים- בן יהודה 2'],
                  'Petah Tikva': ['פתחון לב- זבוטינסקי 4',
                                  'מזון לחיים- מכבים 17']
                   }

TITLE_FOOD = 'Food Donation'
TITLE_FOOD_SIZE = 90
TITLE_FOOD_LOCATION = (90, 20)
TEXT_FOOD_1 = 'Choose a city:'
TEXT_FOOD_SIZE = 50
TEXT_FOOD_LOCATION = (90, 130)
CITY_BUTTON_PHOTO = pygame.image.load('screen2_button.png')
CITY_BUTTON_PHOTO = pygame.transform.scale(CITY_BUTTON_PHOTO, (200, 100))
FIRST_BUTTON_TEXT = "Tel Aviv"
FIRST_BUTTON_COLOR = (255, 255, 255)
FIRST_BUTTON_SIZE = 30
FIRST_BUTTON_LOCATION = (120, 225)
SECOND_BUTTON_TEXT = "Jerusalem"
SECOND_BUTTON_COLOR = (255, 255, 255)
SECOND_BUTTON_SIZE = 30
SECOND_BUTTON_LOCATION = (325, 225)
THIRD_BUTTON_TEXT = "Petah Tikva"
THIRD_BUTTON_COLOR = (255, 255, 255)
THIRD_BUTTON_SIZE = 30
THIRD_BUTTON_LOCATION = (530, 225)

AFTER_CHOOSE_CITY_TEXT = 'Go to one of the following:'
AFTER_CHOOSE_CITY_TEXT_SIZE = 40
AFTER_CHOOSE_CITY_TEXT_LOCATION = (100, 300)


TEL_AVIV_ADDRESS = FOOD_CITY_DICT["Tel Aviv"]
JERUSALEM_ADDRESS = FOOD_CITY_DICT["Jerusalem"]
PETAH_TIKVA_ADDRESS = FOOD_CITY_DICT["Petah Tikva"]
ADDRESS_SIZE = 20
ADDRESS_LOCATION = (530, 225)

