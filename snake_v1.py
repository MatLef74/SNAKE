"""
    ===== A simple "snake" game to learn 1 dimension tuples or lists =====
                                   v.1

A snake tries to eat an apple without crossing the edges, nor itself.
Select direction with arrow keys.

. `direction` is one of the key values LEFT, RIGHT, UP, and DOWN.
. IN THIS VERSION, `snake` is describe by 2 lists of integers, `x_snake` and
  `y_snake`, each one giving the coordinates of the i-th block of the snake.
  There lengthes are both 3 at the beggining, then they increase at the same
  time when an apple is eaten.

Some functions are imported from the `snake_tools` module you have to code...
"""
import pygame

from snake_params import (LEFT, RIGHT, UP, DOWN,
                          RED, GREEN, BLUE, BACK,
                          WIDTH, HEIGHT, BLOCK_SIZE,
                          INIT_SPEED
                         )
from snake_tools_v1 import new_apple, new_head, next_snake, lost


def draw(x_snake, y_snake, x_apple, y_apple, score, canvas) -> None:
    """
    Update the canvas (redraw the snake & the apple, rewrite the score...)
    """
    # Fill background
    canvas.fill(BACK)
    # Draw snake
    assert len(x_snake) == len(y_snake)
    for i in range(len(x_snake)):
        color = BLUE if i == 0 else GREEN
        pygame.draw.rect(canvas,
                         color,
                         pygame.Rect(x_snake[i],
                                     y_snake[i],
                                     BLOCK_SIZE,
                                     BLOCK_SIZE))
    # Draw apple
    pygame.draw.rect(canvas,
                     RED,
                     pygame.Rect(x_apple, y_apple, BLOCK_SIZE, BLOCK_SIZE))
    # Write score and speed
    pygame.display.set_caption(f"SCORE: {score} pt (Speed = {int(10 * speed)})")
    # Update drawing
    pygame.display.flip()


# ===== Main Programm ==========================================================

# INIT
score = 0

pygame.init()
font = pygame.font.SysFont('Arial', 20)
background = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

direction = RIGHT
speed = INIT_SPEED
# Initially a centered snake made up of 3 blocks
x_head = WIDTH // 2
y_head = HEIGHT // 2

x_snake = [x_head, x_head - BLOCK_SIZE, x_head - 2 * BLOCK_SIZE]
y_snake = [y_head, y_head, y_head]

x_apple, y_apple = new_apple(x_snake, y_snake)

# QUASI-INFINITE GAME LOOP
game_over = False
while not game_over:
    draw(x_snake, y_snake, x_apple, y_apple, score, background)
    # Look for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
            elif event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
    if game_over:
        break

    # Compute next positions, score and speed
    x_head, y_head = new_head(x_snake, y_snake, direction)

    if (x_head, y_head) == (x_apple, y_apple):
        score += 1
        # 10 % speedup
        speed *= 1.1
        x_apple, y_apple = new_apple(x_snake, y_snake)
        # Snake one block larger
        x_snake.append(None)
        y_snake.append(None)

    x_snake, y_snake = next_snake(x_snake, y_snake, x_head, y_head)

    # Check if edges or snake is reached by snake's head
    game_over = lost(x_snake, y_snake)
    # Redraw the canvas after a short pause
    clock.tick(speed)


# THE END
pygame.display.set_caption('GAME OVER !')
text = font.render( f"FINAL SCORE: {score}", True, RED)
text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 3))
background.blit(text, text_rect)
pygame.display.flip()

# Waiting for a click to close the window
display_score = True
while display_score:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            display_score = False