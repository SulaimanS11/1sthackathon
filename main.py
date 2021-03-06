import pygame
from pygame.locals import *
import sys


pygame.init()
# FUNCTIONS
def index_indexer():
    global index
    index += 1
    if index > 5000:
        index = 1


def wilfird_movement():
    global bob
    if index % 10 == 0:
        if bob == 0:
            bob = 1
        elif bob == 1:
            bob = 0


def wayly_movement():
    global wayly1Rect, rob
    if index % 15 == 0:
        if rob == 0:
            rob = 3
        rob -= 1


# def player_walk_animation():
#     global wilfridRect, SCREEN_LENGTH

#     if wilfridRect.x >= SCREEN_LENGTH:
#         wilfridRect.x = SCREEN_LENGTH
#     if wilfridRect.x <= 0:
#         wilfridRect.x = 0


# WINDOW & DISPLAY SETTINGS
SCREEN_HEIGHT = 384
SCREEN_LENGTH = 1270
windowSurface = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT), 0, 32)
windowSurface.fill((255, 255, 255))
windowRect = windowSurface.get_rect()
windowCenter = windowRect.center
pygame.display.set_caption("Travel to Monaco")


# INDEX
index = 0


# CHARACTERS
wilfrid_walk2 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\character\sandbox_walk.png"
)
wilfrid_walk1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\character\sandbox_result_i.png"
)
wilfrid_walks = [wilfrid_walk1, wilfrid_walk2]
wilfridRect = wilfrid_walk1.get_rect(bottomleft=(0, 384))
bob = 0
player_speed = 0


wayly_still = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun.png"
).convert_alpha()
wayly_run1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun2.png"
).convert_alpha()
wayly_run2 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\enemies\enemyuno\gorlrun3.png"
).convert_alpha()
wayly = [wayly_still, wayly_run1, wayly_run2, wayly_still]
wayly1Rect = wayly_still.get_rect(bottomleft=(1300, 384))
rob = 0

# LANDSCAPE
background1 = pygame.image.load(
    r"P\hackathons\1sthackathon\Pixel_Art\scene4\bobsandvegen.jpg"
)
background1rect = background1.get_rect(topleft=(0, 0))

# EXTRA
clock = pygame.time.Clock()


# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # PLAYER CONTROLS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_speed += 5
            if event.key == pygame.K_a:
                player_speed -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_speed -= 5
            if event.key == pygame.K_a:
                player_speed += 5

    # STATIC BLITS

    # BACKGROUND BLITS
    windowSurface.blit(background1, background1rect)

    # NON STATIC BLITS (CHARACTERS +)
    windowSurface.blit(wilfrid_walks[bob], wilfridRect)
    windowSurface.blit(wayly[rob], wayly1Rect)

    ### WAYLY MOVEMENT
    wayly1Rect.x -= 4

    ### WILFRID MOVEMENT
    wilfridRect.x += player_speed

    # COLLISIONS & LOGIC
    if background1rect.right < 900:
        background1rect.topleft = (0, 0)

    ### main char movement code
    index_indexer()
    wilfird_movement()
    wayly_movement()
    # player_walk_animation()

    # NECESSITIES
    clock.tick(60)
    pygame.display.update()
