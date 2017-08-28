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

    
### MENU











        
### GAME













    
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

