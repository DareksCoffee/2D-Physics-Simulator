import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

def draw_pool(screen, pool_rectangles):
    for rect in pool_rectangles:
        pygame.draw.rect(screen, BLUE, rect)

def create_scene_elements(screen_width, screen_height):
    pool_rectangles = [
        pygame.Rect(50, screen_height - 20, 100, 20),
        pygame.Rect(200, screen_height - 20, 100, 20),
        pygame.Rect(350, screen_height - 20, 100, 20),
    ]

    return pool_rectangles