import pygame

def render_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 20)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def render_velocity_text(screen, x, y, speed_x, speed_y):
    font = pygame.font.Font(None, 20)
    velocity_text = f"Velocity: ({speed_x:.2f}, {speed_y:.2f})"
    text_surface = font.render(velocity_text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y - 30))