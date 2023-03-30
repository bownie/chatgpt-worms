import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Worms Game')

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the worm
worm_position = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
worm_segments = [[worm_position[0], worm_position[1] + 10],
                 [worm_position[0], worm_position[1] + 20],
                 [worm_position[0], worm_position[1] + 30]]
worm_speed = 10
worm_direction = 'UP'

# Set up the food
food_position = [random.randint(0, WINDOW_WIDTH - 10), random.randint(0, WINDOW_HEIGHT - 10)]
food_radius = 5

# Set up the game loop
game_running = True
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                worm_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                worm_direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                worm_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                worm_direction = 'RIGHT'

    # Move the worm
    if worm_direction == 'UP':
        worm_position[1] -= worm_speed
    elif worm_direction == 'DOWN':
        worm_position[1] += worm_speed
    elif worm_direction == 'LEFT':
        worm_position[0] -= worm_speed
    elif worm_direction == 'RIGHT':
        worm_position[0] += worm_speed

    # Add a new segment to the worm
    worm_segments.insert(0, list(worm_position))

    # Remove the last segment of the worm
    if len(worm_segments) > 3:
        worm_segments.pop()

    # Check for collision with food
    if ((worm_position[0] - food_position[0])**2 + (worm_position[1] - food_position[1])**2)**0.5 <= food_radius:
        food_position = [random.randint(0, WINDOW_WIDTH - 10), random.randint(0, WINDOW_HEIGHT - 10)]
        worm_segments.append([0, 0])

    # Check for collision with walls
    if worm_position[0] < 0 or worm_position[0] > WINDOW_WIDTH - 10 or worm_position[1] < 0 or worm_position[1] > WINDOW_HEIGHT - 10:
        game_running = False

    # Clear the screen
    game_window.fill(WHITE)

    # Draw the food
    pygame.draw.circle(game_window, GREEN, food_position, food_radius)

    # Draw the worm
    for segment in worm_segments:
        pygame.draw.rect(game_window, BLACK, [segment[0], segment[1], 10, 10])

    # Update the screen
    pygame.display.update()

    # Set the game speed
    clock.tick(20)

# Quit Pygame
pygame.quit()