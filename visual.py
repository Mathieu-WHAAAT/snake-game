"""
  all visual settings
"""

### COLORS
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GRIS  = (196,196,196)
GREY  = (128,128,128)
DARK  = ( 64, 64, 64)
GREEN = ( 42,216,  0)
VERTP = (150,215, 50)

### IMAGES
# buttons
img_horizontal = pygame.image.load('IMAGES\\horizontal2.png')
img_vertical = pygame.image.load('IMAGES\\vertical2.png')
img_space = pygame.image.load('IMAGES\\space.png')
img_space = pygame.transform.scale(img_space, (int(524*1/3),int(79*1/3)))
img_ctrl = pygame.image.load('IMAGES\\ctrl.png')
img_ctrl = pygame.transform.scale(img_ctrl, (int(100*2/3), int(81*2/3)))
# characteres
img_head = pygame.image.load('IMAGES\\head.png')
img_head = pygame.transform.scale(img_head,(int(case),int(case)))
img_body = pygame.image.load('IMAGES\\body.png')
img_body = pygame.transform.scale(img_body,(int(case),int(case)))
img_food = pygame.image.load('IMAGES\\food.png')
img_food = pygame.transform.scale(img_food,(int(case),int(case)))
# backgrounds
img_launch = pygame.image.load('IMAGES\\launch_screen.png')
img_launch = pygame.transform.scale(img_launch,(int(s_screen),int(s_screen)))
img_menu = pygame.image.load('IMAGES\\bg2.png')
img_menu = pygame.transform.scale(img_menu, (int(s_screen),int(s_screen)))

### Textes
text_screen_start = ' Click anywhere on the screen '
text_screen_start2 = ' or press ENTER on keyboard '
font_screen_start = pygame.font.Font('freesansbold.ttf', 20)
text_menu = ' -- MENU -- '
text_stop = ' -- PAUSE -- '
font_menu = pygame.font.Font('freesansbold.ttf', 50)
text_pause = ' PAUSE '
text_pause2 = ' ( or press key SPACE ) '
font_pause = pygame.font.Font('freesansbold.ttf', 25)
font_pause2 = pygame.font.Font('freesansbold.ttf', 15)
text_end = 'GAME OVER'
font_end = pygame.font.Font('freesansbold.ttf', 70)
font_score = pygame.font.Font('freesansbold.ttf', 25)
