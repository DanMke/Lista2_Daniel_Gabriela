import sys
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGRAY = (169, 169, 169)
YELLOW = (222, 178, 0)
PINK = (225, 96, 253)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
ORANGE = (255, 99, 71)
GRAY = (119, 136, 153)
LIGHTORANGE = (255, 176, 56)
INTERMEDIARYORANGE = (255, 154, 0)
LIGHTBLUE = (60, 170, 255)
DARKBLUE = (0, 101, 178)
BEIGE = (178, 168, 152)

WIDTH = 1002
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

MARGIN = 2

QTT = 100
MIN_HEIGHT = 10
MAX_HEIGHT = 580
RECTANGLE_THICKNESS = 8

WAIT_CONSTANT = 10

def text(background, message, color, size, coordinate_x, coordinate_y):
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    background.blit(text, [coordinate_x, coordinate_y])


class Rectangle():
    def __init__(self, height, width, color, pos_x, pos_y):
        self.height = height
        self.width = width
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])


class Rectangles():
    def __init__(self):
        self.set_rectangles = []

    def append_rectangle(self, rectangle):
        self.set_rectangles.append(rectangle)

    def render(self, background):
        initial_pos_x = MARGIN
        for rectangle in self.set_rectangles:
            rectangle.pos_x = initial_pos_x
            rectangle.render(background)
            initial_pos_x += RECTANGLE_THICKNESS + MARGIN


class Game():
    def __init__(self):
        try:
            pygame.init()
        except:
            print('The pygame module did not start successfully')
        
        self.background = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Sort O(n²)')
        self.rectangles = self.create_rectangles()

    def create_rectangles(self):
        rectangles = Rectangles()
        initial_pos_x = MARGIN
        random_heights = random.sample(range(MIN_HEIGHT, MAX_HEIGHT), QTT)

        for height in random_heights:
            rectangles.append_rectangle(Rectangle(height, RECTANGLE_THICKNESS, WHITE, initial_pos_x, HEIGHT - height - MARGIN))
            initial_pos_x += RECTANGLE_THICKNESS + MARGIN

        return rectangles

    def render(self):
        self.background.fill(BLACK)
        self.rectangles.render(self.background)
    
    def run(self):
        exit = False
        
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit = True
                    if event.key == pygame.K_s:
                        print("chamou selection sort")
                        selection_sort(self.rectangles, self.background)
            
            self.render()
            pygame.display.update()

        pygame.quit()
        sys.exit(0)

# Selection Sort
def selection_sort(rectangles, background):
    for i in range(len(rectangles.set_rectangles)):
        min_index = i

        rectangles.set_rectangles[min_index].color = RED
        rectangles.set_rectangles[min_index].render(background)
        pygame.display.update()
        pygame.time.wait(WAIT_CONSTANT)

        for j in range(i + 1, len(rectangles.set_rectangles)):

            if j > 0 and rectangles.set_rectangles[j - 1].color == BLUE:
                rectangles.set_rectangles[j - 1].color = WHITE
    
            rectangles.set_rectangles[j].color = BLUE
            background.fill(BLACK)
            rectangles.render(background)
            pygame.display.update()
            pygame.time.wait(WAIT_CONSTANT)

            if rectangles.set_rectangles[j].height < rectangles.set_rectangles[min_index].height:

                rectangles.set_rectangles[min_index].color = WHITE
                rectangles.set_rectangles[j].color = RED
                background.fill(BLACK)
                rectangles.render(background)
                pygame.display.update()
                pygame.time.wait(WAIT_CONSTANT)

                min_index = j

        if rectangles.set_rectangles[len(rectangles.set_rectangles) - 1].color == BLUE:
            rectangles.set_rectangles[len(rectangles.set_rectangles) - 1].color = WHITE
        
        aux_rectangle = rectangles.set_rectangles[i]
        rectangles.set_rectangles[i] = rectangles.set_rectangles[min_index]
        rectangles.set_rectangles[min_index] = aux_rectangle


        rectangles.set_rectangles[i].color = GREEN
        background.fill(BLACK)
        rectangles.render(background)
        pygame.display.update()
        pygame.time.wait(WAIT_CONSTANT)

# TODO: Insertion Sort
# TODO: Bubble Sort
# TODO: Shell Sort

def main():
    mygame = Game()
    mygame.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption')