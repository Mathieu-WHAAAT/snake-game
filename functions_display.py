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
