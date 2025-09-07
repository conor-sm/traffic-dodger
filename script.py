import pygame
import random
import sys

pygame.init()

running = True
menu_active = True
game_over = False
easy = False
hard = False

road_img = pygame.transform.scale((pygame.image.load("road.png")), (800, 800))

small = pygame.font.Font("font.otf", 32)
large = pygame.font.Font("font.otf", 48)

cells = 20
cell_size = 40
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((cells * cell_size, cells * cell_size))
pygame.display.set_caption("traffic-dodger")

clock = pygame.time.Clock()

#classes should be used to control difficulty of game
class Easy:
    def __init__(self):
        print("Hello World")
        #should have an update and draw function + anything else needed, easy mode should consist of a normal gameplay with slower cars

class Hard:
    def __init__(self):
        print("Hello World")
        #should have an update and draw function + anything else needed, hard mode should consist of an advanced gameplay with faster cars


def menu():
    screen.fill((0, 0, 0)) 

    line_one = large.render("traffic-dodger", True, (255, 255, 255))
    line_two = small.render("Enter 1: Easy", True, (255, 255, 255))
    line_three = small.render("Enter 2: Hard", True, (255, 0, 0))

    screen.blit(line_one, ((screen_width - line_one.get_width()) // 2, (screen_height - line_one.get_height()) // 2 - 75))
    screen.blit(line_two, ((screen_width - line_two.get_width()) // 2, (screen_height - line_two.get_height()) // 2))
    screen.blit(line_three, ((screen_width - line_three.get_width()) // 2, (screen_height - line_three.get_height()) // 2 + 75))

def game():
    screen.fill((0, 0, 0))
    screen.blit(road_img, (0, 0))
    #should have code to control randomly spawning cars, set up the map and control player speed.

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if menu_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                easy = True
                menu_active = False
            if event.key == pygame.K_2:
                hard = True
                menu_active = False

    if menu_active:
        menu()
    
    elif easy:
        print("Easy")
        game()
    
    elif hard:
        print("Hard")
        game()

    clock.tick(60)
    pygame.display.update()

pygame.quit()