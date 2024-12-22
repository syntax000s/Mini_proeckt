import pygame
import random

# Инициализация Pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Определение параметров окна игры
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Создание окна игры

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Инициализация переменных
snake = [(WIDTH/2, HEIGHT/2)]
direction = "RIGHT"
food = (random.randint(0, WIDTH/CELL_SIZE-1) * CELL_SIZE, random.randint(0, HEIGHT/CELL_SIZE-1) * CELL_SIZE)
score = 0

clock = pygame.time.Clock()

# Функция отрисовки змейки
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Функция отрисовки пищи
def draw_food():
    pygame.draw.rect(screen, WHITE, (food[0], food[1], CELL_SIZE, CELL_SIZE))

# Функция проверки столкновения с пищей
def check_food_collision():
    global score
    if snake[0] == food:
        score += 1
        generate_food()

# Функция генерации новой пищи
def generate_food():
    global food
    food = (random.randint(0, WIDTH/CELL_SIZE-1) * CELL_SIZE, random.randint(0, HEIGHT/CELL_SIZE-1) * CELL_SIZE)

# Основной игровой цик

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    elif keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake.insert(0, (snake[0][0] + CELL_SIZE, snake[0][1]))
    elif direction == "LEFT":
        snake.insert(0, (snake[0][0] - CELL_SIZE, snake[0][1]))
    elif direction == "UP":
        snake.insert(0, (snake[0][0], snake[0][1] - CELL_SIZE))
    elif direction == "DOWN":
        snake.insert(0, (snake[0][0], snake[0][1] + CELL_SIZE))

    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT or snake[0] in snake[1:]:
        pygame.quit()
        quit()

    check_food_collision()

    if len(snake) > score + 1:
        snake.pop()

    screen.fill(BLACK)
    draw_snake()
    draw_food()

    pygame.display.update()

    clock.tick(10)
start()