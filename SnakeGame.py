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
from visual import*
from class_Snake import*
from class_Board import*
from class_Apple import*

##### FUNDAMENTAL INITIALISATIONS 
pygame.init()

FPS = fps_snake = 60
fps_Clock = pygame.time.Clock()

s_screen = 700
DISPLAYSURF = pygame.display.set_mode((s_screen, s_screen),0,32)
pygame.display.set_caption('Snake Game')

##### FUNCTIONS

    
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










    
################################################################################
jeu = 1
time_sec = 0.0

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

