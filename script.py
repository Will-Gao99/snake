import pygame
import os
import time

pygame.font.init()


WIN_HEIGHT = 800
WIN_WIDTH = 800

SNAKE_IMG = pygame.image.load(os.path.join("imgs","snake.png"))
TARGET_IMG = pygame.image.load(os.path.join("imgs","target.png"))
BG_IMG = pygame.image.load(os.path.join("imgs","bg.png"))


STAT_FONT = pygame.font.SysFont("comicsans", 20)

"""
class Piece represents one segment of the entire Snake and contains information
about each individual piece.
"""
class Piece:

    """
    Initializes an object of class Piece at location (x,y) facing right with
    velocity 20
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = 1
        self.direction = "right"
        self.vel = 20
        self.img = SNAKE_IMG

    """
    Changes the piece's location based on the direction it's facing and the
    piece's velocity
    """
    def move(self):
        if self.direction == "right":
            self.x += self.vel
        if self.direction == "left":
            self.x -= self.vel
        if self.direction == "up":
            self.y -= self.vel
        if self.direction == "down":
            self.y += self.vel

    """
    Sets the piece's velocity to 0
    """
    def freeze(self):
        self.vel = 0

    """
    Returns a string representation of an object of type Piece
    """
    def to_str(self):
        string = "[("+ str(self.x) + "," + str(self.y) + "), n=" + str(self.number) + ", " + self.direction + ", velocity=" + str(self.vel) + "]"
        return string

    """
    Draws the piece object to the window
    """
    def draw(self, win):
        win.blit(self.img,(self.x,self.y))

"""
class Snake represents the player controlled snake. Represented by a list of
pieces
"""
class Snake:

    """
    Initilizes an object of class Snake with inputted length and location
    """
    def __init__(self, length, x, y):
        self.x = x
        self.y = y
        self.length = length
        self.pieces = []

    """
    Adds objects of class Piece to self.piece based on self.length
    """
    def build(self):
        for x in range(self.length):
            self.pieces.append(Piece(self.x-(x*20),self.y))

    """
    Iterates through the list of pieces and calls move on each of them
    """
    def move(self):
        for n in self.pieces:
            n.move()
        self.x = self.pieces[0].x
        self.y = self.pieces[0].y

    """
    Returns True if the snake has exited the window and False otherwise
    """
    def exited(self):
        True if ((self.x < 0) or (self.x > WIN_WIDTH)) or ((self.y<0) or (self.y > WIN_HEIGHT)) else False

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
        str = "["
        for x in self.pieces:
            str += (x.to_str() + ";")
        return str + "]"

    """
    Draws the snake to the window
    """
    def draw(self, win):
        for n in self.pieces:
            win.blit(n.img,(n.x,n.y))

"""
Draws inputted objects to the window
"""
def draw_window(win, snake):
    win.blit(BG_IMG, (0,0))
    snake.draw(win)
    pygame.display.update()


def main():
    snake = Snake(4,400,400)
    snake.build()
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
