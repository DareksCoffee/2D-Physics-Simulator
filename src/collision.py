def handle_ball_wall_collision(ball, screen_width, screen_height):
    if 'radius' in ball:
        if ball['x'] - ball['radius'] < 0:
            ball['x'] = ball['radius']
            ball['speed_x'] = abs(ball['speed_x'])
        elif ball['x'] + ball['radius'] > screen_width:
            ball['x'] = screen_width - ball['radius']
            ball['speed_x'] = -abs(ball['speed_x'])

        if ball['y'] - ball['radius'] < 0:
            ball['y'] = ball['radius']
            ball['speed_y'] = abs(ball['speed_y'])
        elif ball['y'] + ball['radius'] > screen_height:
            ball['y'] = screen_height - ball['radius']
            ball['speed_y'] = -abs(ball['speed_y'])

    elif 'size' in ball:
        if ball['x'] - ball['size'] // 2 < 0:
            ball['x'] = ball['size'] // 2
            ball['speed_x'] = abs(ball['speed_x'])
        elif ball['x'] + ball['size'] // 2 > screen_width:
            ball['x'] = screen_width - ball['size'] // 2
            ball['speed_x'] = -abs(ball['speed_x'])

        if ball['y'] - ball['size'] // 2 < 0:
            ball['y'] = ball['size'] // 2
            ball['speed_y'] = abs(ball['speed_y'])
        elif ball['y'] + ball['size'] // 2 > screen_height:
            ball['y'] = screen_height - ball['size'] // 2
            ball['speed_y'] = -abs(ball['speed_y'])

def handle_ball_ball_collision(ball, other_ball):
    if 'radius' in ball and 'radius' in other_ball:
        distance_balls = ((ball['x'] - other_ball['x'])**2 + (ball['y'] - other_ball['y'])**2)**0.5
        if distance_balls < ball['radius'] + other_ball['radius'] and distance_balls > 0:
            overlap = (ball['radius'] + other_ball['radius']) - distance_balls
            direction = ((other_ball['x'] - ball['x']) / distance_balls, (other_ball['y'] - ball['y']) / distance_balls)
            ball['x'] -= overlap * direction[0] / 2
            ball['y'] -= overlap * direction[1] / 2
            other_ball['x'] += overlap * direction[0] / 2
            other_ball['y'] += overlap * direction[1] / 2
    elif 'size' in ball and 'size' in other_ball:
        distance_balls = ((ball['x'] - other_ball['x'])**2 + (ball['y'] - other_ball['y'])**2)**0.5
        if distance_balls < ball['size'] / 2 + other_ball['size'] / 2 and distance_balls > 0:
            overlap = (ball['size'] / 2 + other_ball['size'] / 2) - distance_balls
            direction = ((other_ball['x'] - ball['x']) / distance_balls, (other_ball['y'] - ball['y']) / distance_balls)
            ball['x'] -= overlap * direction[0] / 2
            ball['y'] -= overlap * direction[1] / 2
            other_ball['x'] += overlap * direction[0] / 2
            other_ball['y'] += overlap * direction[1] / 2

def handle_square_wall_collision(square, screen_width, screen_height):
    if square['x'] - square['size'] < 0:
        square['x'] = square['size']
        square['speed_x'] = 0

    if square['x'] + square['size'] > screen_width:
        square['x'] = screen_width - square['size']
        square['speed_x'] = 0

    if square['y'] - square['size'] < 0:
        square['y'] = square['size']
        square['speed_y'] = 0

    if square['y'] + square['size'] > screen_height:
        square['y'] = screen_height - square['size']
        square['speed_y'] = 0

def handle_square_ball_collision(square, ball):
    distance_square_ball = ((square['x'] - ball['x'])**2 + (square['y'] - ball['y'])**2)**0.5
    if distance_square_ball < square['size'] + ball['radius']:
        square['speed_x'] = 0
        square['speed_y'] = 0
