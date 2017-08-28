""" 
    Functions for display
"""

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
    surf_p = font_pause.render(text_pause, True, BLACK, VERTP)
    rect_p = surf_p.get_rect()
    rect_p.centery =  int(0.975*s_screen)
    rect_p.centerx = int(1/2*s_screen)
    surf_p2 = font_pause2.render(text_pause2, True, VERTP)
    rect_p2 = surf_p2.get_rect()
    rect_p2.centery = int(0.975*s_screen)
    rect_p2.left = rect_p.right
    ## Display
    DISPLAYSURF.blit(surf_p, rect_p)
    DISPLAYSURF.blit(surf_p2, rect_p2)
