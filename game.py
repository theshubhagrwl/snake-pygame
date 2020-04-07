import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (42, 212, 48)
RED = (240, 81, 60)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCKSIZE = 20


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Snake Game")
    SCREEN.fill(BLACK)

    x = 0
    y = 0
    velocity = 4
    x_change = 0
    y_change = 0
    snake_length = 1
    snake_list = []

    food_y = round(random.randrange(20, WINDOW_HEIGHT-velocity, 10))
    food_x = round(random.randrange(20, WINDOW_WIDTH-velocity, 10))

    while True:
        # drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -velocity
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = velocity
                    x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = -velocity
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = velocity
                    y_change = 0

        x += x_change
        y += y_change

        # Check for boundary condition
        if x < 0:
            x = 0
        elif x >= WINDOW_WIDTH-10:
            x = WINDOW_WIDTH-BLOCKSIZE
        if y < 0:
            y = 0
        elif y >= WINDOW_HEIGHT-10:
            y = WINDOW_HEIGHT-BLOCKSIZE

        # Collision
        if x > food_x and x < food_x + BLOCKSIZE or x+BLOCKSIZE > food_x and x + BLOCKSIZE < food_x + BLOCKSIZE:
            if y > food_y and y < food_y + BLOCKSIZE or y+BLOCKSIZE > food_y and y + BLOCKSIZE < food_y + BLOCKSIZE:
                food_y = round(random.randrange(
                    20, WINDOW_HEIGHT-velocity, 10))
                food_x = round(random.randrange(20, WINDOW_WIDTH-velocity, 10))
                snake_length += 1

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        if snake_list[-1] == snake_head:
            print("game over")

        snake(snake_list)
        food(food_x, food_y)
        pygame.display.update()
        SCREEN.fill(BLACK)
        CLOCK.tick(60)


def food(food_x, food_y):
    food_size = BLOCKSIZE
    food_rect = pygame.Rect(food_x, food_y, food_size, food_size)
    pygame.draw.rect(SCREEN, RED, food_rect)


def snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(SCREEN, GREEN, (i[0], i[1], BLOCKSIZE, BLOCKSIZE))
    # head_rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)

    # pygame.draw.rect(SCREEN, GREEN, head_rect)


# def drawGrid():
#     BLOCKSIZE = 20
#     for x in range(WINDOW_WIDTH//BLOCKSIZE):
#         for y in range(WINDOW_HEIGHT//BLOCKSIZE):
#             rect = pygame.Rect(x*BLOCKSIZE, y*BLOCKSIZE,
#                                BLOCKSIZE, BLOCKSIZE)
#             pygame.draw.rect(SCREEN, WHITE, rect, 1)


if __name__ == "__main__":
    main()
