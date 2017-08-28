""" 
  Snake class file
"""

class Snake():
    """ Snake object """
    def __init__(self, x = nb_cases//2, y = nb_cases//2, img = 'head'):
        """ Constructor """        
        self.img = img
        self.pos = [x, y]
      
    def new_pos(self, x, y):
        """ Change the position """
        self.pos = [x, y]

    def get_pos(self):
        """ Return position of the snake """
        return (self.pos[0], self.pos[1])
    
    def update(self, gradient):
        """ Method to update position """
        self.pos = [self.pos[0]+gradient[0], self.pos[1]+gradient[1]]
        if self.pos[0] < 0:
            self.pos[0] = nb_cases-1
        elif self.pos[0] >= nb_cases:
            self.pos[0] = 0
        elif self.pos[1] < 0:
            self.pos[1] = nb_cases-1
        elif self.pos[1] >= nb_cases:
            self.pos[1] = 0
            
    def display(self, img_head, img_body, s_case):
        """ Display on the screen """
        add = (s_screen-s_board)/2
        if self.img == 'head':
            DISPLAYSURF.blit(img_head, (int(add+self.pos[0]*s_case), int(add+self.pos[1]*s_case)))
        elif self.img == 'body':
            DISPLAYSURF.blit(img_body, (int(add+self.pos[0]*s_case), int(add+self.pos[1]*s_case)))

"""
  Function associate
"""
def update_serpents(list_serp, move):
    """ Update the position of the snake """
    for iSerp in range(len(list_serp)-1,0,-1):
        x_pos, y_pos = list_serp[iSerp-1].get_pos()
        list_serp[iSerp].new_pos(x_pos, y_pos)
    list_serp[0].update(move)
    return list_serp

def update_cases_free(list_serp, Plat, nb_cases):
    """ nothing interesting """
    Plat.reset(nb_cases)
    for iSerp in list_serp:
        if iSerp != list_serp[0]:
            x_pos, y_pos = iSerp.get_pos()
            Plat.set_case(x_pos, y_pos)
    return Plat

def is_eating(pom, serp, Plateau, nb_cases):
    """ Check if is eating. return True or False """
    pos_pom = pom.get_pos()
    pos_serp = serp.get_pos()
    if pos_pom == pos_serp:
        pom.set_pos(Plateau, nb_cases)
        return True
    else:
        return False
    
def colision(serp, Plat, nb_cases):
    """"""
    pos = serp.get_pos()
    list_pos_oqp = Plat.cases_oqp(nb_cases)
    if pos in list_pos_oqp:
        return True
    else: 
        return False

def display_serpents(list_serp, case):
    """ Display the snake on the screen """
    for serpent in Serpents_list:
            serpent.display(img_head, img_body, case)
