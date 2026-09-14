import pygame
import random
import sys

pygame.init()

# -----------------------------
# Basic game settings
# -----------------------------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Driving Game")

clock = pygame.time.Clock()

# Colors
GREEN = (34, 139, 34)
GRAY = (70, 70, 70)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 100, 220)
RED = (220, 40, 40)
YELLOW = (255, 220, 0)
ORANGE = (255, 140, 0)
PURPLE = (150, 50, 180)


# -----------------------------
# Road settings
# -----------------------------

road_left = 200
road_right = 600
road_width = road_right - road_left

number_of_lanes = 4
lane_width = road_width // number_of_lanes


# -----------------------------
# Player car
# -----------------------------

car_width = 50
car_height = 90

car_x = road_left + lane_width * 2
car_y = HEIGHT - 130

car_speed = 6


# -----------------------------
# Enemy cars
# -----------------------------

enemy_width = 50
enemy_height = 90

enemy_speed = 5
enemy_cars = []


# -----------------------------
# Game variables
# -----------------------------

score = 0
game_over = False

road_lines = 0
spawn_timer = 0

font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 60)


def draw_player():
    # Main body of the player's car
    pygame.draw.rect(
        screen,
        BLUE,
        (car_x, car_y, car_width, car_height)
    )

    # Front window
    pygame.draw.rect(
        screen,
        (150, 220, 255),
        (car_x + 8, car_y + 10, car_width - 16, 25)
    )

    # Back window
    pygame.draw.rect(
        screen,
        (100, 180, 230),
        (car_x + 8, car_y + 55, car_width - 16, 20)
    )

    # Four wheels
    pygame.draw.rect(screen, BLACK, (car_x - 5, car_y + 10, 8, 25))
    pygame.draw.rect(screen, BLACK, (car_x + car_width - 3, car_y + 10, 8, 25))
    pygame.draw.rect(screen, BLACK, (car_x - 5, car_y + 55, 8, 25))
    pygame.draw.rect(screen, BLACK, (car_x + car_width - 3, car_y + 55, 8, 25))


def draw_enemy(enemy):
    x = enemy["x"]
    y = enemy["y"]
    color = enemy["color"]

    pygame.draw.rect(
        screen,
        color,
        (x, y, enemy_width, enemy_height)
    )

    # Windows
    pygame.draw.rect(
        screen,
        (180, 230, 255),
        (x + 8, y + 10, enemy_width - 16, 25)
    )

    pygame.draw.rect(
        screen,
        (120, 190, 230),
        (x + 8, y + 55, enemy_width - 16, 20)
    )

    # Wheels
    pygame.draw.rect(screen, BLACK, (x - 5, y + 10, 8, 25))
    pygame.draw.rect(screen, BLACK, (x + enemy_width - 3, y + 10, 8, 25))
    pygame.draw.rect(screen, BLACK, (x - 5, y + 55, 8, 25))
    pygame.draw.rect(screen, BLACK, (x + enemy_width - 3, y + 55, 8, 25))


def draw_road():
    global road_lines

    # Grass
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(
        screen,
        GRAY,
        (road_left, 0, road_width, HEIGHT)
    )

    # White lines on the sides of the road
    pygame.draw.rect(
        screen,
        WHITE,
        (road_left, 0, 8, HEIGHT)
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (road_right - 8, 0, 8, HEIGHT)
    )

    # Dashed lines between lanes
    for lane in range(1, number_of_lanes):
        line_x = road_left + lane * lane_width

        for y in range(-100, HEIGHT, 100):
            pygame.draw.rect(
                screen,
                WHITE,
                (line_x - 3, y + road_lines, 6, 50)
            )


def add_enemy():
    # Pick one of the four lanes
    lane = random.randint(0, number_of_lanes - 1)

    enemy_x = road_left + lane * lane_width
    enemy_x += (lane_width - enemy_width) // 2

    possible_colors = [
        RED,
        YELLOW,
        ORANGE,
        PURPLE
    ]

    new_enemy = {
        "x": enemy_x,
        "y": -enemy_height,
        "color": random.choice(possible_colors)
    }

    enemy_cars.append(new_enemy)


def player_hit():
    player_rect = pygame.Rect(
        car_x,
        car_y,
        car_width,
        car_height
    )

    for enemy in enemy_cars:
        enemy_rect = pygame.Rect(
            enemy["x"],
            enemy["y"],
            enemy_width,
            enemy_height
        )

        if player_rect.colliderect(enemy_rect):
            return True

    return False


def show_score():
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (20, 20))


def show_game_over():
    # Make the screen darker
    dark = pygame.Surface((WIDTH, HEIGHT))
    dark.set_alpha(180)
    dark.fill(BLACK)

    screen.blit(dark, (0, 0))

    title = big_font.render(
        "GAME OVER",
        True,
        RED
    )

    score_text = font.render(
        "Final Score: " + str(score),
        True,
        WHITE
    )

    restart_text = font.render(
        "Press R to Restart",
        True,
        WHITE
    )

    quit_text = font.render(
        "Press Q to Quit",
        True,
        WHITE
    )

    screen.blit(
        title,
        (
            WIDTH // 2 - title.get_width() // 2,
            180
        )
    )

    screen.blit(
        score_text,
        (
            WIDTH // 2 - score_text.get_width() // 2,
            270
        )
    )

    screen.blit(
        restart_text,
        (
            WIDTH // 2 - restart_text.get_width() // 2,
            330
        )
    )

    screen.blit(
        quit_text,
        (
            WIDTH // 2 - quit_text.get_width() // 2,
            380
        )
    )


def restart_game():
    global car_x
    global car_y
    global enemy_cars
    global enemy_speed
    global score
    global game_over
    global road_lines
    global spawn_timer

    car_x = road_left + lane_width * 2
    car_y = HEIGHT - 130

    enemy_cars = []

    enemy_speed = 5
    score = 0

    game_over = False
    road_lines = 0
    spawn_timer = 0


# -----------------------------
# Main game loop
# -----------------------------

running = True

while running:

    # Game runs at 60 FPS
    clock.tick(60)

    # Check for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                restart_game()

            if event.key == pygame.K_q:
                running = False

    # Only update the game when it is not over
    if not game_over:

        keys = pygame.key.get_pressed()

        # Move the player's car
        if keys[pygame.K_LEFT]:
            car_x -= car_speed

        if keys[pygame.K_RIGHT]:
            car_x += car_speed

        if keys[pygame.K_UP]:
            car_y -= car_speed

        if keys[pygame.K_DOWN]:
            car_y += car_speed

        # Stop the car from leaving the road
        if car_x < road_left + 10:
            car_x = road_left + 10

        if car_x > road_right - car_width - 10:
            car_x = road_right - car_width - 10

        if car_y < 0:
            car_y = 0

        if car_y > HEIGHT - car_height:
            car_y = HEIGHT - car_height

        # Move the road markings
        road_lines += enemy_speed

        if road_lines >= 100:
            road_lines = 0

        # Decide when to create another enemy
        spawn_timer += 1

        spawn_rate = max(25, 70 - score)

        if spawn_timer >= spawn_rate:
            add_enemy()
            spawn_timer = 0

        # Move all enemy cars
        for enemy in enemy_cars:
            enemy["y"] += enemy_speed

        # Remove cars that have gone off the screen
        for enemy in enemy_cars[:]:

            if enemy["y"] > HEIGHT:
                enemy_cars.remove(enemy)
                score += 1

        # Make the game gradually faster
        enemy_speed = 5 + score * 0.05

        if enemy_speed > 12:
            enemy_speed = 12

        # Check if the player crashed
        if player_hit():
            game_over = True

    # -------------------------
    # Draw the game
    # -------------------------

    draw_road()

    for enemy in enemy_cars:
        draw_enemy(enemy)

    draw_player()
    show_score()

    if game_over:
        show_game_over()

    pygame.display.update()


pygame.quit()
sys.exit()
