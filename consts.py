import pygame

VOLUNTEER_LIST = ['donate money', 'volunteer place', 'food donation', 'recycling', 'call or visit', 'smile to the world']
# VOLUNTEER_LIST = ['call or visit', 'smile to the world']
CITY_LIST_COMMUNITY_SERVICE = ['Ramat Gan', 'Tel Aviv', 'Bat Yam', 'Ashdod', 'Haifa', 'Petah Tikva']
COMMUNITY_SERVICE = {'Ramat Gan': {'elderly people': ["עמך- ביקורי בית לניצולי שואה",
                                                      "יחידות סגולה- סיוע לקשישים מאושפזים במיצוי זכויותיהם",
                                                      "מטב- הפגת בדידות לקשישים בביקורים",
                                                      "ביקור קשישים מאושפזים בבית החולים",
                                                      "מטב- ליווי ותמיכה בקשישים עם בעלי חיים"],
                                   'Children': ["ליווי ילדים מאושפזים בבתי חולים", "השתתפות בהפקות לנוער בסיכון"],
                                   'Animals': ["הוצאת כלבי הכלבייה ועזרה בחתולייה", "ליווי קשישים עם בעלי חיים"],
                                   'Earth': ["סיוע בבתי החולים לחיות בר",  "סיוע בגינון ופיתוח גינות קהילתיות"]},
 'Tel Aviv': {'elderly people': ["מטב- התנדבות טלפונית",
                                 "מטב- הפעלות וסדנאות לקשישים"],
              'Children': ["חונכות אישית בבתי ספר", "השתתפות בפעילות בגני חינוך מיוחד"],
              'Animals': ["התנדבות שטח במקלט לבעלי חיים", "ליווי קשישים עם בעלי חיים"],
              'Earth': ["ניקוי חופים"
                  ,"ניקוי יערות קקל"]},
'Bat Yam': {'elderly people': ["מגד- הפגת בדידות לקשישים"
                                ,"מועדון מורשת השואה- העברת הפעלה"],
            'Children': ["שיעורי עזרה בלמודים בהתנדבות", "השתתפות בהפקות לנוער בסיכון"],
            'Animals': ["ליווי קשישים עם בעלי חיים", "גג לחיות- ניקוי כלובים ומתן אוכל"],
            'Earth': ["ניקוי חופים", "סיוע בגינון ופיתוח גינות קהילתיות"]},
'Ashdod': {'elderly people': ["ליווי קשישים לבדיקות בבית החולים",
                              "מטב- בילוי עם קשישים עם בעלי חיים"],
           'Children': ["ליווי ילדים עם מוגבלויות בחוגים שונים", "סוע לילדים בלימודים בהתנדבות"],
           'Animals': ["ליווי קשישים עם בעלי חיים", "התנדבות בכלבייה העירונית"],
           'Earth': ["ניקוי חופים", "ניקוי פארקים"]},
'Haifa': {'elderly people': ["ליווי קשישים לבדיקות בבית החולים",
                             "מהלב לצלחת- בישול ארוחות חמות לקשישים"],
          'Children': ["שיעורי עזרה בלימודים בהתנדבות", "סיוע לתלמידים בפנימיות"],
          'Animals': ["גלבוע אוהבת חיות- תחזוקה וסיוע בכלבייה", "צער בעלי חיים- הוצאת כלבי הכלבייה"],
          'Earth': ["סיוע בעבודה חקלאית בבוסתן", "ניקוי חופים"]},
'Petah Tikva': {'elderly people': ["ליווי קשישים לבדיקות בבית החולים",
                                   "יחידות סגולה- סיוע לקשישים מאושפזים במיצוי זכויותיהם"],
                'Children': ["השתתפות בהפקות לנוער בסיכון", "ליווי ילדים עם מוגבלויות בחוגים שונים"],
                'Animals': ["התנדבות מהבית למען בעלי חיים", "ארגון בכלבייה העירונית"],
                'Earth': ["צביעת שולחנות וגדרות בפארקים", "סיוע בגינון ופיתוח גינות קהילתיות"]}}


# window size
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500

# colors
BACKGROUND_COLOR = (162, 201, 206)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# fonts
TEXT_FONT_NAME = "Calibri"
TITLE_FONT_NAME = "georgia"

# starting title
STARTING_MESSAGE = "Daily Good"
STARTING_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
STARTING_COLOR = BLACK
STARTING_LOCATION = (0.12 * WINDOW_WIDTH, 10)

# money title
MONEY_MESSAGE = "Money Donation"
MONEY_FONT_SIZE = 77
MONEY_COLOR = BLACK
MONEY_LOCATION = STARTING_LOCATION

# money1 text
MONEY1 = "How much money do you want to donate?"
MONEY1_FONT_SIZE = 26
MONEY1_COLOR = BLACK
MONEY1_LOCATION = (150, 110)

# money2 text
MONEY2 = "these are our places, choose one of the options:"
MONEY2_FONT_SIZE = MONEY1_FONT_SIZE
MONEY2_COLOR = BLACK
MONEY2_LOCATION = STARTING_LOCATION

# money3 text
MONEY3 = "Thank you for your donation!"
MONEY3_FONT_SIZE = MONEY1_FONT_SIZE
MONEY3_COLOR = BLACK
MONEY3_LOCATION = STARTING_LOCATION

# starting button text
CHOOSE_TEXT = "Choose"
CHOOSE_COLOR = WHITE
CHOOSE_SIZE = 70
CHOOSE_LOCATION = (270, 225)

# random deed text (screen 2)
DEED_COLOR = BLACK
DEED_SIZE = 60
DEED_LOCATION = (200, 210)


# explaining the program
EXPLAIN_TEXT = ("This is a program "
                "that gives you the opportunity "
                "to contribute to the community "
                "through a good deed")
EXPLAIN_COLOR = BLACK
EXPLAIN_SIZE = 18
EXPLAIN_LOCATION = (20, 450)

# starting button photo
PLAY_BUTTON_PHOTO = pygame.image.load('button.png')
PLAY_BUTTON_PHOTO = pygame.transform.scale(PLAY_BUTTON_PHOTO, (300, 200))

# screen2 button photo
SCREEN_2_BUTTON_PHOTO = pygame.image.load('screen2_button.png')
SCREEN_2_BUTTON_PHOTO = pygame.transform.scale(SCREEN_2_BUTTON_PHOTO, (250, 150))

# screen2 left button text
LEFT_BUTTON_TEXT = "agree"
LEFT_BUTTON_COLOR = WHITE
LEFT_BUTTON_SIZE = 40
LEFT_BUTTON_LOCATION = (145, 390)

# screen2 right button text
RIGHT_BUTTON_TEXT = "choose again"
RIGHT_BUTTON_COLOR = WHITE
RIGHT_BUTTON_SIZE = 40
RIGHT_BUTTON_LOCATION = (455, 390)
