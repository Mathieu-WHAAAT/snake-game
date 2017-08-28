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



