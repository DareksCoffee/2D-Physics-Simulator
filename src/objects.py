import random

def spawn_random_ball(balls, x, y):
    random_ball_radius = 20
    random_ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    balls.append({
        'radius': random_ball_radius,
        'color': random_ball_color,
        'x': x,
        'y': y,
        'speed_x': random.uniform(-2, 2),
        'speed_y': random.uniform(-2, 2),
        'dragging': False,
        'drag_offset_x': 0,
        'drag_offset_y': 0
    })

def spawn_physics_square(balls, x, y):
    physics_square_size = 30
    physics_square_color = (255, 255, 255)

    balls.append({
        'size': physics_square_size,
        'color': physics_square_color,
        'x': x,
        'y': y,
        'speed_x': 0,
        'speed_y': 0,
        'dragging': False,
        'drag_offset_x': 0,
        'drag_offset_y': 0
    })