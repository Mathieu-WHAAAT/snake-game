""" 
  Apple class file
"""

class Apple():
    """ Apple object """
    def __init__(self, Plat, nb_cases, bonus=False):
        """ Constructor """
        choix = Plat.cases_available(nb_cases)
        self.pos = random.choice(choix)

    def set_pos(self, Plat, nb_cases):
        """ Constructor """
        choix = Plat.cases_available(nb_cases)
        self.pos = random.choice(choix)

    def get_pos(self):
        """ Return Pos """
        return self.pos
    
    def display(self, img_food, s_case):
        """ Display the food """
        add = (s_screen-s_board)/2
        DISPLAYSURF.blit(img_food, (int(add+self.pos[0]*s_case), int(add+self.pos[1]*s_case)))
        
"""
  Associated Functions
"""

