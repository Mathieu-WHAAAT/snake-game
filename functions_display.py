""" 
  functions for updates
"""

def initialise_all():
    """ Reinitialise the object """
    i_Plateau = Board(s_board, nb_cases, case)
    i_Serpent = Snake(nb_cases//2, nb_cases//2)
    i_displacement = (0,0)
    i_Pomme = Apple(Plateau, nb_cases)
    i_vitesse = 0.4
    return i_Plateau, i_Serpent, i_displacement, i_Pomme, i_vitesse

def check_option(mouse, rects):
    """ Check which option has been choosed """        
    index = 0
    for rect in rects:
        index += 1
        if (rect.left < mouse[0] < rect.right) and (rect.top < mouse[1] < rect.bottom):
            return index
        
def options_menu(stage=4):
    """ Determine the differents options """
    big_rect = pygame.Rect(0, 0, int(2/5*s_screen), int(3/4*s_screen))
    big_rect.centerx = 2/3*s_screen + 0.0575*s_screen
    big_rect.centery = (1/2*s_screen) + 0.0575*s_screen
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
