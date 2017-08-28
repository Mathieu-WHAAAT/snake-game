### SOUNDS
pygame.mixer.init()

VOL_MUSIC = 0.6
VOL_EFFECT= 0.6

snake_grow = pygame.mixer.Sound("SOUNDS\\grow_sound.wav")
snake_grow.set_volume(VOL_EFFECT)
snake_die = pygame.mixer.Sound("SOUNDS\\die_sound.wav")
snake_die.set_volume(0.7)

sound_bg1 = "SOUNDS\\game_msc.mp3"
pygame.mixer.music.load(sound_bg1)
pygame.mixer.music.set_volume(VOL_MUSIC)

### SOUNDS
def bg_music_start():
    """ Play the background music """
    pygame.mixer.music.play(-1, 0.0)

def bg_music_pause():
    """ Pause the bg_music """
    pygame.mixer.music.pause()

def bg_music_unpause():
    """ Unpause the bg_music """
    pygame.mixer.music.unpause()

def play_sound(sound):
    """ Play the sound given in param """
    sound.play()

def low_vol(choice, vol):
    """ Low the volume of the type choosen """
    if vol > 0.0: 
        vol -= 0.05
    else: 
        vol = 0.0  
    vol = round(vol*100)/100
    if choice == 'music':
        pygame.mixer.music.set_volume(vol)
    elif choice == 'effect':
        snake_grow.set_volume(vol)
    return vol

def up_vol(choice, vol):
    """ Low the volume of the type choosen """
    if vol < 1.0:
        vol += 0.05
    else:
        vol = 1.0
    vol = round(vol*100)/100
    if choice == 'music':
        pygame.mixer.music.set_volume(vol)
    elif choice == 'effect':
        snake_grow.set_volume(vol)
    return vol
