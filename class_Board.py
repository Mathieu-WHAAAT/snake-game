"""
  Board class file
"""

s_board = s_screen*0.9
nb_cases = 42
case = s_board/nb_cases

class Board():
    """ Cases du tableau """
    def __init__(self, s_board, nb_cases, size_case):
        """ Constructor """
        self.board_rect = pygame.Rect(0, 0, s_board, s_board)
        self.board_rect.centerx = s_screen//2
        self.board_rect.centery = s_screen//2
        self.board_case = []
        self.case_taken = []
        add = (s_screen-s_board)/2
        for lig in range(nb_cases):
            self.board_case.append([])
            self.case_taken.append([])
            for col in range(nb_cases):
                self.board_case[lig].append([int(add+size_case*lig), int(add+size_case*col), int(size_case), int(size_case)])
                self.case_taken[lig].append(False)
    def reset(self, nb_cases):
        """ reset the free cases """
        for lig in range(nb_cases):
            for col in range(nb_cases):
                self.case_taken[lig][col] = False
    
    def set_case(self, x, y):
        """ set if case is available or not """
        self.case_taken[x][y] = True
                
    def cases_oqp(self, nb_cases):
        """ give the non-available cases """
        oqp = []
        for lig in range(nb_cases):
            for col in range(nb_cases):
                if self.case_taken[lig][col]:
                    oqp.append((lig,col))
        return oqp
    
    def cases_available(self, nb_cases):
        """ Return the cases available as a tuple """
        available = []
        for lig in range(nb_cases):
            for col in range(nb_cases):
                if not self.case_taken[lig][col]:
                    available.append((lig, col))         
        return available

    def get_board(self):
        """ Return the Rect object """
        return self.board_rect

    def get_cases(self):
        """ Return the list of cases """
        return self.board_case
   
"""
  Functions associate
"""


    
        


    

    
