import pygame
import sys
import random

pygame.init()

# Game constants
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 620
CELL_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Font for displaying score
font = pygame.font.SysFont('Arial', 18)


board = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "       ## #      # ##       ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Temporary Styling for Player
pacman_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
pacman_img.fill((255, 255, 0))  # Yellow square
ghost_imgs = [
    pygame.Surface((CELL_SIZE, CELL_SIZE)),
    pygame.Surface((CELL_SIZE, CELL_SIZE)),
    pygame.Surface((CELL_SIZE, CELL_SIZE)),
    pygame.Surface((CELL_SIZE, CELL_SIZE))
]

# Temporary Styling for Ghost
ghost_imgs[0].fill((255, 255, 0))  # Yellow
ghost_imgs[1].fill((255, 0, 0))    # Red
ghost_imgs[2].fill((0, 0, 255))    # Blue
ghost_imgs[3].fill((0, 255, 0))    # Green



# Game variables
pacman_x = 13  # Starting x position (center of board)
pacman_y = 23  # Starting y position (near bottom)
pacman_direction = 'RIGHT'  # Initial direction
score = 0  # Player's score

# Ghost starting positions
ghosts = [
    {'x': 13, 'y': 11},  # Yellow ghost
    {'x': 14, 'y': 11},  # Red ghost
    {'x': 13, 'y': 12},  # Blue ghost
    {'x': 14, 'y': 12}   # Green ghost
]



# Draw the game board
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '.':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 3)
            elif cell == 'o':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 7)

# Draw Pac-Man
def draw_pacman():
    screen.blit(pacman_img, (pacman_x * CELL_SIZE, pacman_y * CELL_SIZE))

# Draw ghosts
def draw_ghosts():
    for i, ghost in enumerate(ghosts):
        screen.blit(ghost_imgs[i], (ghost['x'] * CELL_SIZE, ghost['y'] * CELL_SIZE))

# Move Pac-Man
def move_pacman():
    global pacman_x, pacman_y, score
    if pacman_direction == 'LEFT' and board[pacman_y][pacman_x - 1] != '#':
        pacman_x -= 1
    elif pacman_direction == 'RIGHT' and board[pacman_y][pacman_x + 1] != '#':
        pacman_x += 1
    elif pacman_direction == 'UP' and board[pacman_y - 1][pacman_x] != '#':
        pacman_y -= 1
    elif pacman_direction == 'DOWN' and board[pacman_y + 1][pacman_x] != '#':
        pacman_y += 1
    
    if board[pacman_y][pacman_x] == '.':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 10
    elif board[pacman_y][pacman_x] == 'o':
        board[pacman_y] = board[pacman_y][:pacman_x] + ' ' + board[pacman_y][pacman_x + 1:]
        score += 50

# Move ghosts
def move_ghosts():
    for ghost in ghosts:
        direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
        if direction == 'LEFT' and board[ghost['y']][ghost['x'] - 1] != '#':
            ghost['x'] -= 1
        elif direction == 'RIGHT' and board[ghost['y']][ghost['x'] + 1] != '#':
            ghost['x'] += 1
        elif direction == 'UP' and board[ghost['y'] - 1][ghost['x']] != '#':
            ghost['y'] -= 1
        elif direction == 'DOWN' and board[ghost['y'] + 1][ghost['x']] != '#':
            ghost['y'] += 1

# Check for collisions
def check_collisions():
    for ghost in ghosts:
        if ghost['x'] == pacman_x and ghost['y'] == pacman_y:
            return True
    return False

# Check if all pellets are eaten
def check_all_pellets_eaten():
    for row in board:
        if '.' in row or 'o' in row:
            return False
    return True

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                pacman_direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                pacman_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                pacman_direction = 'DOWN'

    move_pacman()
    move_ghosts()

    if check_collisions():
        print("Game Over!")
        running = False

    if check_all_pellets_eaten():
        print("You Win!")
        running = False

    screen.fill(BLACK)
    draw_board()
    draw_pacman()
    draw_ghosts()

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, SCREEN_HEIGHT - 30))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()