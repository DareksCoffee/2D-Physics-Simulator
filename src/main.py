import pygame
from physics_simulation import simulate_gravity
from scene import create_scene_elements, draw_pool

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

simulate_gravity(screen, clock, screen_width, screen_height)
pool_rectangles = create_scene_elements(screen_width, screen_height)

print("Simulation Ended.")