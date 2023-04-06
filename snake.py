import pygame, random
from pygame.locals import *

# function to align apples to the grid
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10 )

# define movement constants
UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

# define global variables
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))
apple_pos = on_grid_random()
my_direction = LEFT

# create game window
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

# game clock
clock = pygame.time.Clock()

# configuration of apple
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

# collision test function
def collision(c1,c2):
    return(c1[0]==c2[0] ) and (c1[1]==c2[1])

# reset game function
def reset_game():
    global snake, snake_skin, apple_pos, my_direction
    snake = [(200,200), (210,200), (220,200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))
    apple_pos = on_grid_random()
    my_direction = LEFT

# game loop
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            # exit game
        if event.type == KEYDOWN:
            # key detection for snake movement
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    # collision test and snake growth
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

        
    # check for collision of the snake with itself
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            reset_game()

    if snake[0][0] < 0 or snake[0][0] > 590 or snake[0][1] < 0 or snake[0][1] > 590:
        reset_game() 
        
    # snake movement
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # check if snake collided with itself or wall
    if snake[0][0] < 0 or snake[0][0] > 590 or snake[0][1] < 0 or snake[0][1] > 590:
        reset_game()

    for i in range(1, len(snake) - 1):
        if snake[0] == snake[i]:
            reset_game()
    
    # fill background
    screen.fill((0,0,0))

    # draw apple and snake
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin,pos)
    
    pygame.display.update()