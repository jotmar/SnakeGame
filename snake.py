import pygame
from pygame.locals import *
from sys import exit
from random import randint


def gen_apple():
    x = (randint(0, 800) // 10 * 10)
    y = (randint(0,600) // 10 * 10)
    apple_pos = (x, y)
    apple = pygame.Surface((10, 10))
    apple.fill('red')
    return (apple, apple_pos)


def show_score(score):
    game_score = game_score_font.render(f'Score: {score}', True, 'White')
    game_score_rect = game_score.get_rect(midtop = (400, 20))
    screen.blit(game_score, game_score_rect)

WIDTH = 800
HEIGTH = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Snake Game')
game_name_font = pygame.font.SysFont('Arial', 60)
game_press_font = pygame.font.SysFont('Aria', 30)
game_score_font = pygame.font.SysFont('Arial', 20)
score = 0
clock = pygame.time.Clock()

background = pygame.Surface((WIDTH, HEIGTH))
background.fill('black')

#Snake Var
snake = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGTH'

#Game Text
game_name = game_name_font.render('Snake game', True, 'Cyan')
game_name_rect = game_name.get_rect(center = (400, 300))
game_press = game_press_font.render('Press Space to Start', True, 'Cyan')
game_press_rect = game_press.get_rect(midbottom = (400, 500))


apple = gen_apple()
game_state = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and direction != 'LEFT':
                direction = 'RIGTH'
            elif event.key == K_a and direction != 'RIGTH':
                direction = 'LEFT'
            elif event.key == K_w and direction != 'DOWN':
                direction = 'UP'
            elif event.key == K_s and direction != 'UP':
                direction = 'DOWN'
            elif event.key == K_SPACE and game_state == 0:
                game_state = 1
        
    screen.blit(background, (0, 0))

    if game_state == 1:

        for i in range(len(snake)):
            if i != 0:
                if snake[0] == snake[i]:
                    game_state = 0
        
        if snake[0][0] > 800 or snake[0][0] < 0:
            game_state = 0
        if snake[0][1] > 600 or snake[0][1] < 0:
            game_state = 0

        
        for i in range(len(snake)-1, 0, -1):
            pygame.draw.rect(screen, 'green', (snake[i][0], snake[i][1], 10, 10))
            snake[i] = snake[i-1].copy()


        screen.blit(apple[0], apple[1])
        show_score(score)

        if snake[0][0] == apple[1][0] and snake[0][1] == apple[1][1]:
            apple = gen_apple()
            snake.append([-10,-10])
            score += 1

       
        if direction == 'RIGTH':
            snake[0][0] += 10
        elif direction == 'LEFT':
            snake[0][0] -= 10
        elif direction == 'DOWN':
            snake[0][1] += 10
        elif direction == 'UP':
            snake[0][1] -= 10

    else:
        score = 0
        screen.blit(game_name, game_name_rect)
        screen.blit(game_press, game_press_rect)
        snake = [[100, 50], [90, 50], [80, 50]]
        apple = gen_apple()
        direction = 'RIGTH'
    
    clock.tick(25)

    pygame.display.update()