import pygame
import random
import sys

pygame.init()

running = True
game_active = False
menu_active = True
game_over = False
easy = False
medium = False
hard = False
impossible = False

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

def menu():
    screen.fill((0, 0, 0)) 
    line_one = large.render("traffic-dodger", True, (255, 255, 255))
    line_two = small.render("Enter 1: Easy", True, (255, 255, 255))
    line_three = small.render("2: Medium", True, (255, 255, 255))
    line_four = small.render("3: Hard", True, (255, 255, 255))
    line_five = small.render("4: Impossible", True, (255, 0, 0))
    screen.blit(line_one, ((screen_width - line_one.get_width()) // 2, (screen_height - line_one.get_height()) // 2 - 75))
    screen.blit(line_two, ((screen_width - line_two.get_width()) // 2, (screen_height - line_two.get_height()) // 2))
    screen.blit(line_three, ((screen_width - line_three.get_width()) // 2, (screen_height - line_three.get_height()) // 2 + 75))
    screen.blit(line_four, ((screen_width - line_four.get_width()) // 2, (screen_height - line_four.get_height()) // 2 + 150))
    screen.blit(line_five, ((screen_width - line_five.get_width()) // 2, (screen_height - line_five.get_height()) // 2 + 225))


def game():
    screen.fill((0, 0, 0))
    screen.blit(road_img, (0, 0))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    if menu_active:
        menu()
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()