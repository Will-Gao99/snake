import pygame
import os
import time
import linkedlist

pygame.font.init()


WIN_HEIGHT = 800
WIN_WIDTH = 800

SNAKE_IMG = pygame.image.load(os.path.join("imgs","snake.png"))
TARGET_IMG = pygame.image.load(os.path.join("imgs","target.png"))
BG_IMG = pygame.image.load(os.path.join("imgs","bg.png"))

SNAKE_VEL = 20
STAT_FONT = pygame.font.SysFont("comicsans", 20)

"""
class Piece represents one segment of the entire Snake and contains information
about each individual piece.
"""
class Piece:

    """
    Initializes an object of class Piece at location (x,y)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = SNAKE_IMG

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y

    """
    Returns a string representation of an object of type Piece
    """
    def to_str(self):
        string = "[("+ str(self.x) + "," + str(self.y) + ")]"
        return string

    """
    Draws the piece object to the window
    """
    def draw(self, win):
        win.blit(self.img,(self.x,self.y))

"""
class Snake represents the player controlled snake. Represented by a linkedlist
of pieces
"""
class Snake(linkedlist.LinkedList):

    """
    Initilizes an object of class Snake with inputted length and location
    """
    def __init__(self, length, x, y):
        self.length = length
        self.direction = "right"
        self.vel = SNAKE_VEL
        root_node = linkedlist.Node(Piece(x,y))
        super().__init__(root_node)
        for n in range(self.length):
            super().append(linkedlist.Node(Piece(x-(n*20),y)))

    """
    Changes the position of the first Piece by its velocity and updates the
    position of the rest of the snake to inherit its predecessor's positions
    """
    def move(self):
        pass

    """
    Returns True if the snake has exited the window and False otherwise
    """
    def exited(self):
        pass

    """
    Returns True if the first piece of the snake has either left the boundaries
    of the window or if the first piece is in the same location as another piece.
    Returns False otherwise
    """
    def check_loss(self):
        pass

    """
    Returns a string represention of the Snake
    """
    def to_str(self):
        pass

    """
    Draws the snake to the window
    """
    def draw(self, win):
        pass

"""
Draws inputted objects to the window
"""
def draw_window(win, snake):
    win.blit(BG_IMG, (0,0))
    snake.draw(win)
    pygame.display.update()


def main():
    snake = Snake(4,400,400)
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        snake.move()

        draw_window(win, snake)


if __name__ == "__main__":
    main()
