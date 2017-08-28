### SOUNDS
VOL_MUSIC = 0.6
VOL_EFFECT= 0.6

snake_grow = pygame.mixer.Sound("SOUNDS\\grow_sound.wav")
snake_grow.set_volume(VOL_EFFECT)
snake_die = pygame.mixer.Sound("SOUNDS\\die_sound.wav")
snake_die.set_volume(0.7)

sound_bg1 = "SOUNDS\\game_msc.mp3"
pygame.mixer.music.load(sound_bg1)
pygame.mixer.music.set_volume(VOL_MUSIC)
