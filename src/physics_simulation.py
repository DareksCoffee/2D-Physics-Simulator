# physics_simulation.py
import pygame
import random
from objects import spawn_random_ball, spawn_physics_square
from rendering import render_text, render_velocity_text
from collision import handle_ball_wall_collision, handle_ball_ball_collision, handle_square_wall_collision, handle_square_ball_collision
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWNISH = (139, 69, 19)

def simulate_gravity(screen, clock, screen_width, screen_height):
    balls = []
    print("Simulation Started.")
    user_ball_radius = 20
    user_ball_color = WHITE
    user_ball_x = screen_width // 2
    user_ball_y = screen_height // 2
    user_ball_speed_x = 0
    user_ball_speed_y = 0
    gravity = 0.1
    bounce_factor = 0.8

    square_size = 30
    square_color = WHITE
    square_x = 400
    square_y = 300
    square_speed_x = 0
    square_speed_y = 0
    square_dragging = False
    square_drag_offset_x = 0
    square_drag_offset_y = 0
    square_drag_damping = 0.98

    square = {
    'size': square_size,
    'color': square_color,
    'x': square_x,
    'y': square_y,
    'speed_x': square_speed_x,
    'speed_y': square_speed_y,
    'dragging': square_dragging,
    'drag_offset_x': square_drag_offset_x,
    'drag_offset_y': square_drag_offset_y,
                                  }    
    time_scale = 1.0
    paused = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    spawn_random_ball(balls, mouse_x, mouse_y)
                elif event.key == pygame.K_c:
                    balls = []
                elif event.key == pygame.K_o:
                    for ball in balls:
                        ball['speed_y'] -= random.randint(-15, 15) * 0.5
                        ball['speed_x'] -= random.randint(-2, 3)
                elif event.key == pygame.K_y:
                    if time_scale == 1.0:
                        time_scale = 0.5
                    else:
                        time_scale = 1.0
                elif event.key == pygame.K_a:
                    for ball in balls:
                        render_velocity_text(screen, int(ball['x']), int(ball['y']), ball['speed_x'], ball['speed_y'])

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ball in balls:
                        distance = ((event.pos[0] - ball['x'])**2 + (event.pos[1] - ball['y'])**2)**0.5
                        if 'radius' in ball and distance < ball['radius']:
                            ball['dragging'] = True
                            ball['drag_offset_x'] = ball['x'] - event.pos[0]
                            ball['drag_offset_y'] = ball['y'] - event.pos[1]

                    distance_square = ((event.pos[0] - square_x)**2 + (event.pos[1] - square_y)**2)**0.5
                    if distance_square < square_size:
                        square_dragging = True
                        square_drag_offset_x = square_x - event.pos[0]
                        square_drag_offset_y = square_y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for ball in balls:
                        ball['dragging'] = False
                    square_dragging = False

        pygame.display.set_caption(f"Physics Sandbox - FPS : {int(clock.get_fps())}")

        if not paused:
            user_ball_speed_y += gravity * time_scale
            user_ball_x += user_ball_speed_x * time_scale
            user_ball_y += user_ball_speed_y * time_scale

        if user_ball_x - user_ball_radius < 0 or user_ball_x + user_ball_radius > screen_width:
            user_ball_speed_x *= -1

        if user_ball_y - user_ball_radius < 0:
            user_ball_y = user_ball_radius
            user_ball_speed_y = abs(user_ball_speed_y) * bounce_factor

        if user_ball_y + user_ball_radius > screen_height:
            user_ball_y = screen_height - user_ball_radius
            user_ball_speed_y = -abs(user_ball_speed_y) * bounce_factor

        for ball in balls:
            if ball['dragging']:
                ball['x'] = event.pos[0] + ball['drag_offset_x']
                ball['y'] = event.pos[1] + ball['drag_offset_y']

            handle_ball_wall_collision(ball, screen_width, screen_height)

            ball['speed_y'] += gravity
            ball['x'] += ball['speed_x']
            ball['y'] += ball['speed_y']

            if 'radius' in ball:
                if ball['x'] - ball['radius'] < 0 or ball['x'] + ball['radius'] > screen_width:
                    ball['x'] = ball['radius'] if ball['x'] < ball['radius'] else screen_width - ball['radius']
                    ball['speed_x'] = 0

                if ball['y'] - ball['radius'] < 0:
                    ball['y'] = ball['radius']
                    ball['speed_y'] = abs(ball['speed_y']) * bounce_factor

                if ball['y'] + ball['radius'] > screen_height:
                    ball['y'] = screen_height - ball['radius']
                    ball['speed_y'] = -abs(ball['speed_y']) * bounce_factor

            elif 'size' in ball:
                if ball['x'] - ball['size'] // 2 < 0 or ball['x'] + ball['size'] // 2 > screen_width:
                    ball['x'] = ball['size'] // 2 if ball['x'] < ball['size'] // 2 else screen_width - ball['size'] // 2
                    ball['speed_x'] = 0

                if ball['y'] - ball['size'] // 2 < 0:
                    ball['y'] = ball['size'] // 2
                    ball['speed_y'] = abs(ball['speed_y']) * bounce_factor

                if ball['y'] + ball['size'] // 2 > screen_height:
                    ball['y'] = screen_height - ball['size'] // 2
                    ball['speed_y'] = -abs(ball['speed_y']) * bounce_factor

            distance_user_ball = ((user_ball_x - ball['x'])**2 + (user_ball_y - ball['y'])**2)**0.5
            if distance_user_ball < user_ball_radius + ball.get('radius', 0):
                user_ball_speed_x = -user_ball_speed_x
                user_ball_speed_y = -user_ball_speed_y
                ball['speed_x'] = -ball['speed_x']
                ball['speed_y'] = -ball['speed_y']

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                handle_ball_ball_collision(balls[i], balls[j])

        if square_dragging:
            square_speed_x = (event.pos[0] + square_drag_offset_x - square_x) * 0.0
            square_speed_y = (event.pos[1] + square_drag_offset_y - square_y) * 0.0
        else:
            handle_square_wall_collision(square, screen_width, screen_height)

            square_speed_y += gravity
            square_x += square_speed_x
            square_y += square_speed_y

            if square_x - square_size < 0:
                square_x = square_size
                square_speed_x = 0

            if square_x + square_size > screen_width:
                square_x = screen_width - square_size
                square_speed_x = 0

            if square_y - square_size < 0:
                square_y = square_size
                square_speed_y = 0

            if square_y + square_size > screen_height:
                square_y = screen_height - square_size
                square_speed_y = 0

            for ball in balls:
                handle_square_ball_collision(square, ball)

        square_speed_x *= square_drag_damping
        square_speed_y *= square_drag_damping

        screen.fill(BLACK)

        for ball in balls:
            if 'radius' in ball:
                pygame.draw.circle(screen, WHITE, (int(ball['x']), int(ball['y'])), ball['radius'] + 1)
                pygame.draw.circle(screen, ball['color'], (int(ball['x']), int(ball['y'])), ball['radius'])
            elif 'size' in ball:
                pygame.draw.rect(screen, WHITE, (int(ball['x'] - ball['size'] // 5) - 1, int(ball['y'] - ball['size'] // 5) - 1, ball['size'] + 2, ball['size'] + 2))
        render_text(screen, "S - Spawn ball      C - Clear everything      B - Spawn physics square      O - Explosion", WHITE, 10, 10)
        pygame.display.flip()

        clock.tick(120)
    pygame.quit()
