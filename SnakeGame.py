"""
Project Title: SnakeGame 

Description:
    The old Snake Game recreated.
    - move your snake
    - eat the apples
    - grow as much as possible without dying !

Authors: Mathieu Dario
"""

##### IMPORTS 
import pygame, sys
import random

from pygame.locals import*
from sounds import*
from class_Snake import*
from class_Board import*
from class_Apple import*

##### FUNDAMENTAL INITIALISATIONS 
pygame.init()

FPS = fps_snake = 60
fps_Clock = pygame.time.Clock()

### SCREEN
s_screen = 700
DISPLAYSURF = pygame.display.set_mode((s_screen, s_screen),0,32)
pygame.display.set_caption('Snake Game')

s_board = s_screen*0.9
nb_cases = 42
case = s_board/nb_cases

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


##### CLASSES
class Board():
    """ Cases du tableau """
    def __init__(self, s_board, nb_cases, size_case):
        """ Constructor """
        # board
        self.board_rect = pygame.Rect(0, 0, s_board, s_board)
        self.board_rect.centerx = s_screen//2
        self.board_rect.centery = s_screen//2
        # list des cases + oqp
        self.board_case = []
        self.case_taken = []
        add = (s_screen-s_board)/2
        for lig in range(nb_cases):
            self.board_case.append([])
            self.case_taken.append([])
            for col in range(nb_cases):
                self.board_case[lig].append([int(add+size_case*lig), int(add+size_case*col), int(size_case), int(size_case)])
                self.case_taken[lig].append(False)

    def get_board(self):
        """ Return the Rect object """
        return self.board_rect

    def get_cases(self):
        """ Return the list of cases """
        return self.board_case
    
    def set_case(self, x, y):
        """ set if case is available or not """
        self.case_taken[x][y] = True
        
    def reset(self, nb_cases):
        for lig in range(nb_cases):
            for col in range(nb_cases):
                self.case_taken[lig][col] = False

    def cases_oqp(self, nb_cases):
        """ """
        oqp = []
        for lig in range(nb_cases):
            for col in range(nb_cases):
                if self.case_taken[lig][col]:
                    oqp.append((lig,col))
        return oqp

    def cases_available(self, nb_cases):
        """ Return the cases available as a tuple """
        available = []
        for lig in range(nb_cases):
            for col in range(nb_cases):
                if not self.case_taken[lig][col]:
                    available.append((lig, col))         
        return available
            
class Apple():
    """ Apple object """
    def __init__(self, Plat, nb_cases, bonus=False):
        """ Constructor """
        choix = Plat.cases_available(nb_cases)
        self.pos = random.choice(choix)

    def display(self, img_food, s_case):
        """ Display the food """
        add = (s_screen-s_board)/2
        DISPLAYSURF.blit(img_food, (int(add+self.pos[0]*s_case), int(add+self.pos[1]*s_case)))

    def set_pos(self, Plat, nb_cases):
        """ Constructor """
        choix = Plat.cases_available(nb_cases)
        self.pos = random.choice(choix)

    def get_pos(self):
        """ Return Pos """
        return self.pos


##### FUNCTIONS
def initialise_all():
    """ Reinitialise the object """
    i_Plateau = Board(s_board, nb_cases, case)
    i_Serpent = Snake(nb_cases//2, nb_cases//2)
    i_displacement = (0,0)
    i_Pomme = Apple(Plateau, nb_cases)
    i_vitesse = 0.4
    return i_Plateau, i_Serpent, i_displacement, i_Pomme, i_vitesse
    
### START SCREEN
def display_start_screen(bg, size_s, text_screen, text_screen2, font_screen, color):
    """ Display the start screen """
    DISPLAYSURF.blit(bg, (0,0))
    if color:
        surf_screen = font_screen.render(text_screen, True, BLACK, GREEN)
        surf_screen2 = font_screen.render(text_screen2, True, BLACK, GREEN)
    else:
        surf_screen = font_screen.render(text_screen, True, GREEN, BLACK)
        surf_screen2 = font_screen.render(text_screen2, True, GREEN, BLACK)
    rect_screen = surf_screen.get_rect()
    rect_screen.centerx = size_s // 2
    rect_screen.centery = 0.15*size_s
    rect_screen2 = surf_screen2.get_rect()
    rect_screen2.top = rect_screen.bottom + 3
    rect_screen2.centerx = rect_screen.centerx
    DISPLAYSURF.blit(surf_screen, rect_screen)
    DISPLAYSURF.blit(surf_screen2, rect_screen2)
    
### MENU
def check_option(mouse, rects):
    """ Check which option has been choosed """        
    index = 1
    for rect in rects:
        if (rect.left < mouse[0] < rect.right) and (rect.top < mouse[1] < rect.bottom):
            return index
        index += 1

def options_menu(stage=4):
    """ Determine the differents options """
    big_rect = pygame.Rect(0, 0, int(2/5*s_screen), int(3/4*s_screen))
    big_rect.centerx = 2/3*s_screen + 0.0575*s_screen
    big_rect.centery = (1/2*s_screen) + 0.0575*s_screen
    text_options = []
    if stage == 2:
        text_options = [' PLAY ', ' VOLUME ', ' HIGH SCORES ', ' CONTROLS ', ' QUIT ']
    else:
        text_options = [' RESUME ', ' RESTART ', ' VOLUME ', ' CONTROLS ', ' QUIT ']
    rect_options = []
    for index in range(5):
        rect_option = pygame.Rect(0, 0, int(2/5*s_screen), int(3/20*s_screen))
        rect_option.left = big_rect.left
        rect_option.top = big_rect.top + index*3/20*s_screen
        rect_options.append(rect_option)
    return rect_options, text_options

def display_menu(bg, options, textes, text_menu, font_menu, size_s):
    """ Display the menu """
    DISPLAYSURF.blit(bg, (0,0))
    surf_menu = font_menu.render(text_menu, True, VERTP, BLACK)
    rect_menu = surf_menu.get_rect()
    rect_menu.centerx = size_s // 2
    rect_menu.top = 0.025*size_s
    DISPLAYSURF.blit(surf_menu, rect_menu)
    mouse = pygame.mouse.get_pos()
    for rect in range(len(options)):
        pygame.draw.rect(DISPLAYSURF, BLACK, options[rect])
        if (options[rect].left < mouse[0] < options[rect].right) and (options[rect].top < mouse[1] < options[rect].bottom):
            pygame.draw.rect(DISPLAYSURF, VERTP, options[rect], 5)
    font_options = pygame.font.Font('freesansbold.ttf', 35)
    for text in range(len(textes)):
        surf_text = font_options.render(textes[text], True, VERTP, BLACK)
        rect_text = surf_text.get_rect()
        rect_text.centerx = options[text].centerx
        rect_text.centery = options[text].centery
        DISPLAYSURF.blit(surf_text, rect_text)

def option_volume():
    """ Option rect of the menu """
    big_rect = pygame.Rect(0, 0, int(2/5*s_screen), int(2/3*s_screen))
    big_rect.centerx = 2/3*s_screen + 0.0575*s_screen
    big_rect.centery = (1/2*s_screen) + 0.0575*s_screen
    rect_options = []
    for index in range(2):
        rect_option = pygame.Rect(0, 0, int(2/5*s_screen), int(2/6*s_screen))
        rect_option.left = big_rect.left
        rect_option.top = big_rect.top + index*2/6*s_screen
        rect_options.append(rect_option)
    return rect_options

def display_volume_setting(bg, font_menu, size_s, textes, options, v_mus, v_eff):
    """ Display the menu """
    font_options = pygame.font.Font('freesansbold.ttf', 35)
    mouse = pygame.mouse.get_pos()
    vols = (str(v_mus), str(v_eff))
    rect_vol_settings = []
    DISPLAYSURF.blit(bg, (0,0))
    surf_menu = font_menu.render(' --VOLUME-- ', True, VERTP, BLACK)
    rect_menu = surf_menu.get_rect()
    rect_menu.centerx = size_s // 2
    rect_menu.top = 0.025*size_s
    DISPLAYSURF.blit(surf_menu, rect_menu)
    surf_back = font_options.render(' BACK ', True, VERTP, BLACK)
    rect_back = surf_back.get_rect()
    rect_back.top = 0.03*size_s
    rect_back.left = 0.025*size_s
    DISPLAYSURF.blit(surf_back, rect_back)
    rect_vol_settings.append(rect_back)
    if (rect_back.left < mouse[0] < rect_back.right) and (rect_back.top < mouse[1] < rect_back.bottom):
        pygame.draw.rect(DISPLAYSURF, VERTP, rect_back, 3)
    for rect in range(len(options)):
        pygame.draw.rect(DISPLAYSURF, BLACK, options[rect])
        pygame.draw.rect(DISPLAYSURF, VERTP, options[rect], 3)
        surf_button_l = font_options.render(' < ', True, VERTP, BLACK)
        rect_button_l = surf_button_l.get_rect()
        rect_button_l.bottom = options[rect].bottom - 1/10*s_screen
        rect_button_l.left = options[rect].left + 1/30*s_screen
        DISPLAYSURF.blit(surf_button_l, rect_button_l)
        rect_vol_settings.append(rect_button_l)
        if (rect_button_l.left < mouse[0] < rect_button_l.right) and (rect_button_l.top < mouse[1] < rect_button_l.bottom):
            pygame.draw.rect(DISPLAYSURF, VERTP, rect_button_l, 3)
        surf_button_r = font_options.render(' > ', True, VERTP, BLACK)
        rect_button_r = surf_button_r.get_rect()
        rect_button_r.bottom = options[rect].bottom - 1/10*s_screen
        rect_button_r.right = options[rect].right - 1/30*s_screen
        DISPLAYSURF.blit(surf_button_r, rect_button_r)
        rect_vol_settings.append(rect_button_r)
        if (rect_button_r.left < mouse[0] < rect_button_r.right) and (rect_button_r.top < mouse[1] < rect_button_r.bottom):
            pygame.draw.rect(DISPLAYSURF, VERTP, rect_button_r, 3)
    for text in range(2):
        surf_text = font_options.render(textes[text], True, VERTP, BLACK)
        rect_text = surf_text.get_rect()
        rect_text.centerx = options[text].centerx
        rect_text.centery = options[text].top + 1/9*size_s
        DISPLAYSURF.blit(surf_text, rect_text)
        surf_value = font_options.render(vols[text], True, VERTP)
        rect_value = surf_value.get_rect()
        rect_value.centerx = rect_text.centerx
        rect_value.bottom = options[text].bottom - 1/10*s_screen
        DISPLAYSURF.blit(surf_value, rect_value)
    return rect_vol_settings

def option_controls():
    """ Option rect of the menu """
    big_rect_larg = 7/8*s_screen
    big_rect_long = 2/3*s_screen
    big_rect = pygame.Rect(0, 0, int(big_rect_larg), int(big_rect_long))
    big_rect.centerx = s_screen/2 
    big_rect.centery = (1/2*s_screen) + 0.0575*s_screen
    rect_options = []
    for index in range(4):
        rect_option = pygame.Rect(0, 0, int(big_rect_larg*2/5), int(big_rect_long/4))
        rect_option.left = big_rect.left
        rect_option.top = big_rect.top + index*big_rect_long/4
        rect_2 = pygame.Rect(0, 0, int(big_rect_larg*3/5), int(big_rect_long/4))
        rect_2.right = big_rect.right
        rect_2.top = rect_option.top
        rect_options.append((rect_option,rect_2))
    return rect_options

def display_controles(bg, size_s, font_menu, img_list):
    """ page to tell the control commands """
    font_options = pygame.font.Font('freesansbold.ttf', 35)
    font_text = pygame.font.Font('freesansbold.ttf', 20)
    mouse = pygame.mouse.get_pos()
    text_list = [' horizontal motion (LEFT & RIGHT) ',
                 ' vertical motion (UP & DOWN) ',
                 ' PAUSE menu button ',
                 ' ACCELERATION button ']
    options = option_controls()
    surf_menu = font_menu.render(' --CONTROLS-- ', True, VERTP, BLACK)
    rect_menu = surf_menu.get_rect()
    rect_menu.centerx = size_s // 2
    rect_menu.top = 0.025*size_s
    surf_back = font_options.render(' BACK ', True, VERTP, BLACK)
    rect_back = surf_back.get_rect()
    rect_back.top = 0.03*size_s
    rect_back.left = 0.025*size_s

    DISPLAYSURF.blit(bg, (0,0))
    DISPLAYSURF.blit(surf_menu, rect_menu)
    DISPLAYSURF.blit(surf_back, rect_back)
    if (rect_back.left < mouse[0] < rect_back.right) and (rect_back.top < mouse[1] < rect_back.bottom):
        pygame.draw.rect(DISPLAYSURF, VERTP, rect_back, 3)
    for irect in range(len(options)):
        pygame.draw.rect(DISPLAYSURF, BLACK, options[irect][0])
        pygame.draw.rect(DISPLAYSURF, VERTP, options[irect][0], 3)
        pygame.draw.rect(DISPLAYSURF, BLACK, options[irect][1])
        pygame.draw.rect(DISPLAYSURF, VERTP, options[irect][1], 3)
        rect_img = img_list[irect].get_rect()
        rect_img.center = options[irect][0].center
        DISPLAYSURF.blit(img_list[irect], rect_img)
        surf_text = font_text.render(text_list[irect], True, VERTP, BLACK)
        rect_text = surf_text.get_rect()
        rect_text.center = options[irect][1].center
        DISPLAYSURF.blit(surf_text, rect_text)
    return rect_back
        
### GAME
def compte_a_rebours(): ##son
    """ Compte à rebours avant le jeu """
##    play_sound(son)
    time_sec = 1.5
    chiffre = 4
    while chiffre>0:
        ### INPUTS
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        ### Update
        if time_sec >= 1.25:
            text_chiffre = str(chiffre-1)
            font_chiffre = pygame.font.Font('freesansbold.ttf', int(1/(chiffre)*s_screen))
            chiffre -= 1
            time_sec = 0.0
        surf_chiffre = font_chiffre.render(text_chiffre, True, GREEN)
        rect_chiffre = surf_chiffre.get_rect()
        rect_chiffre.center = (s_screen//2, s_screen//2)
        time_sec += 1/FPS
        ### Display
        DISPLAYSURF.fill(BLACK)
        if chiffre > 0:
            DISPLAYSURF.blit(surf_chiffre, rect_chiffre)
        pygame.display.update()
        fps_Clock.tick(FPS)

def display_board(Plat):
    """ Display the grill on the screen """
    DISPLAYSURF.fill(BLACK)
    board = Plat.get_cases()
    rect = Plat.get_board()
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)
    for case in board:
        for listes in case:
            pygame.draw.rect(DISPLAYSURF, WHITE, listes)
            pygame.draw.rect(DISPLAYSURF, GRIS, listes, 1)

def display_buttons(text_pause, text_pause2, font_pause, font_pause2):
    """ Display the buttons on the game screen """
    # pause button
    surf_p = font_pause.render(text_pause, True, BLACK, VERTP)
    rect_p = surf_p.get_rect()
    rect_p.centery =  int(0.975*s_screen)
    rect_p.centerx = int(1/2*s_screen)
    surf_p2 = font_pause2.render(text_pause2, True, VERTP)
    rect_p2 = surf_p2.get_rect()
    rect_p2.centery = int(0.975*s_screen)
    rect_p2.left = rect_p.right
    # ..... button
    
    ## Display
    DISPLAYSURF.blit(surf_p, rect_p)
    DISPLAYSURF.blit(surf_p2, rect_p2)










def display_score(score, font):
    """ display the score """
    text = 'Score: '+ str(score)
    surf = font.render(text, True, VERTP)
    rect = surf.get_rect()
    rect.topleft = (10, 10)
    DISPLAYSURF.blit(surf, rect)
    
################################################################################
jeu = 1
time_sec = 0.0
# textes
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
# objets
Plateau = Board(s_board, nb_cases, case)
Serpents_list = []
Serpent = Snake()
Serpents_list.append(Serpent)
Pomme = Apple(Plateau, nb_cases)
# attributs
displacement = (0,0)
vitesse = 0.3
boost = vitesse
score = 0
# aides
interact_rect = []
back = []

##### GAME LOOP
bg_music_start()
pygame.key.set_repeat(50,100)
while True:
    if jeu == 1: #start screen
        ##### INPUTS #####
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                enter = True
            else:
                enter = False               
        if ((pygame.mouse.get_pressed()[0] == 1) or enter) and time_sec > 0.3:
            jeu = 2 #menu
            setting = 0
            time_sec = 0.0
            continue
        ##### UPDATES #####
        if time_sec >= 1.0:
            time_sec = 0.0
        elif time_sec >= 0.5:
            bg_color = True
        else:
            bg_color = False
        time_sec += 1/FPS
        ##### DISPLAY #####
        display_start_screen(img_launch, s_screen, text_screen_start, text_screen_start2, font_screen_start, bg_color)
        pygame.display.update()
    elif jeu == 2: #menu
        if setting == 1: # PLAY
            jeu = 3
            time_sec = 0.0
            compte_a_rebours()
            continue
        elif setting == 2: # VOLUME
            ##### INPUTS #####
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.3:
                time_sec = 0.0
                mouse_pos = pygame.mouse.get_pos()
                param = check_option(mouse_pos, interact_rect)
            else:
                param = 0
            ##### UPDATES #####
            if param == 1:
                setting = 0
            elif param == 2:
                VOL_MUSIC = low_vol('music', VOL_MUSIC)
            elif param == 3:
                VOL_MUSIC = up_vol('music', VOL_MUSIC)
            elif param == 4:
                VOL_EFFECT = low_vol('effect', VOL_EFFECT)
            elif param == 5:
                VOL_EFFECT = up_vol('effect', VOL_EFFECT)
            time_sec += 1/FPS
            ##### DISPLAY #####
            interact_rect = display_volume_setting(img_menu, font_menu, s_screen, [' MUSIC ', ' EFFECTS '], option_volume(), VOL_MUSIC, VOL_EFFECT)
        elif setting == 3: # HIGH SCORES
            setting = 0
            pass
        elif setting == 4: # CONTROL
            ##### INPUTS #####
            arriere = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.3:
                time_sec = 0.0
                mouse_pos = pygame.mouse.get_pos()
                arriere = check_option(mouse_pos, back)
            ##### UPDATE #####
            if arriere == True:
                setting = 0
                time_sec = 0.0
            time_sec += 1/FPS
            ##### DISPLAY #####
            but_list = [img_horizontal, img_vertical, img_space, img_ctrl]
            back.append(display_controles(img_menu, s_screen, font_menu, but_list))
        elif setting == 5: # Quit the game
            Plateau, iSerpent, displacement, Pomme, vitesse = initialise_all()
            score = 0
            Serpents_list = [iSerpent]
            jeu = 1
            time_sec = 0.0
            continue
        else:
            ##### INPUTS #####
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()       
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.1:
                time_sec = 0.0
                mouse_pos = pygame.mouse.get_pos()
                setting = check_option(mouse_pos, rect_settings)
            ##### UPDATES #####
            rect_settings, text_settings = options_menu(jeu)
            time_sec += 1/FPS
            ##### DISPLAY #####
            display_menu(img_menu, rect_settings, text_settings, text_menu, font_menu, s_screen)
        pygame.display.update()
    elif jeu == 3: #play
        change = False
        ##### INPUTS #####
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # movements
            if event.type == KEYDOWN and event.key == K_UP:
                if displacement != (0,1):
                    displacement = (0,-1)
            if event.type == KEYDOWN and event.key == K_RIGHT:
                if displacement != (-1,0):
                    displacement = (1,0)
            if event.type == KEYDOWN and event.key == K_DOWN:
                if displacement != (0,-1):
                    displacement = (0,1)
            if event.type == KEYDOWN and event.key == K_LEFT:
                if displacement != (1,0):
                    displacement = (-1,0)
            if event.type == KEYDOWN and event.key == K_LCTRL:
                boost = vitesse/2
            if event.type == KEYUP and event.key == K_LCTRL:
                boost = vitesse
            if event.type == KEYDOWN and event.key == K_SPACE:
                change = True   
        ##### UPDATES #####            
        if time_sec >= boost: #updating snake
            print(vitesse)
            x, y = Serpents_list[-1].get_pos()
            new_serp = Snake(x, y, 'body')
            Serpents_list = update_serpents(Serpents_list, displacement)
            if is_eating(Pomme, Serpents_list[0], Plateau, nb_cases): #eating test
                if boost == vitesse/2:
                    vitesse *= 0.93
                    boost = vitesse/2
                else:
                    vitesse *= 0.93
                    boost = vitesse
                score += 1
                play_sound(snake_grow)
                Serpents_list.append(new_serp)
            Plateau = update_cases_free(Serpents_list, Plateau, nb_cases)
            if colision(Serpents_list[0], Plateau, nb_cases): #colision test
                play_sound(snake_die)
                jeu = 5 #game over screen
                time_sec = 0.0
                continue
            time_sec = 0.0
        if change:
            jeu = 4 # menu game
            setting = 0
            time_sec = 0.0
            continue
        time_sec += 1/FPS
        ##### DISPLAY #####
        display_board(Plateau)
        display_score(score, font_screen_start)
        display_buttons(text_pause, text_pause2, font_pause, font_pause2)
        display_serpents(Serpents_list, case)
        Pomme.display(img_food, case)      
        pygame.display.update()
    elif jeu == 4: #menu game
        if setting == 1: # PLAY
            jeu = 3
            time_sec = 0.0
            continue
        elif setting == 2: # RESTART 
            Plateau, iSerpent, displacement, Pomme, vitesse = initialise_all()
            score = 0
            Serpents_list = [iSerpent]
            print(Serpents_list[0].get_pos())
            jeu = 3
            time_sec = 0.0
            compte_a_rebours() ##compte
            continue
        elif setting == 3: # VOLUME
            ##### INPUTS #####
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.3:
                time_sec = 0.0
                mouse_pos = pygame.mouse.get_pos()
                param = check_option(mouse_pos, interact_rect)
            else: param = 0
            ##### UPDATES #####
            if param == 1:
                setting = 0
            elif param == 2:
                VOL_MUSIC = low_vol('music', VOL_MUSIC)
            elif param == 3:
                VOL_MUSIC = up_vol('music', VOL_MUSIC)
            elif param == 4:
                VOL_EFFECT = low_vol('effect', VOL_EFFECT)
            elif param == 5:
                VOL_EFFECT = up_vol('effect', VOL_EFFECT)
            time_sec += 1/FPS
            ##### DISPLAY #####
            interact_rect = display_volume_setting(img_menu, font_menu, s_screen, [' MUSIC ', ' EFFECTS '], option_volume(), VOL_MUSIC, VOL_EFFECT)
        elif setting == 4: # CONTROL
            ##### INPUTS #####
            arriere = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.3:
                time_sec = 0.0
                mouse_pos = pygame.mouse.get_pos()
                arriere = check_option(mouse_pos, back)
            ##### UPDATE #####
            if arriere == True:
                setting = 0
                time_sec = 0.0
            time_sec += 1/FPS
            ##### DISPLAY #####
            but_list = [img_horizontal, img_vertical, img_space, img_ctrl]
            back.append(display_controles(img_menu, s_screen, font_menu, but_list))    
        elif setting == 5: # QUIT
            Plateau, Serpent_list, displacement, Pomme, vitesse = initialise_all()
            score = 0
            jeu = 1
            time_sec = 0.0
            continue
        else:
            ##### INPUTS #####
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()       
            if pygame.mouse.get_pressed()[0] == 1 and time_sec >= 0.3:
                mouse_pos = pygame.mouse.get_pos()
                time_sec = 0.0
                setting = check_option(mouse_pos, rect_settings)
            ##### UPDATES #####
            rect_settings, text_settings = options_menu(jeu)
            time_sec += 1/FPS
            ##### DISPLAY #####
            display_menu(img_menu, rect_settings, text_settings, text_stop, font_menu, s_screen)
        pygame.display.update()
    elif jeu == 5: #end screen
        ##### INPUTS #####
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    #display_credits()
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    #display_credits()
                    jeu = 4
                    setting = 5
                    continue
        ##### UPDATES #####
        text_stop = 'press ENTER to shut out the game'
        text_suit = 'press SPACE to continue the game'
        surf_stop = font_pause2.render(text_stop, True, GREEN)
        surf_suit = font_pause2.render(text_suit, True, GREEN)
        rect_stop = surf_stop.get_rect()
        rect_stop.center = (s_screen/2, s_screen*3/4)
        rect_suit = surf_suit.get_rect()
        rect_suit.top = rect_stop.bottom + 10
        rect_suit.centerx = rect_stop.centerx
        text_score = "Your score: " + str(score)
        surf_score = font_score.render(text_score, True, GREEN, BLACK)
        surf_end = font_end.render(text_end, True, GREEN, BLACK)
        rect_end = surf_end.get_rect()
        rect_end.center = (s_screen/2, s_screen/2)
        rect_score = surf_score.get_rect()
        rect_score.center = (s_screen/2, s_screen/4)
        time_sec += 1/FPS
        ##### DISPLAY #####
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(surf_end, rect_end)
        DISPLAYSURF.blit(surf_score, rect_score)
        DISPLAYSURF.blit(surf_stop, rect_stop)
        DISPLAYSURF.blit(surf_suit, rect_suit)
        pygame.display.update()
    else:
        pass
    fps_Clock.tick(FPS)
################################################################################

