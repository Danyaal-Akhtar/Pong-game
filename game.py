def update_score(ball_x, window_width, score_j1, score_j2):
    if ball_x < 0:
        score_j2 += 1
    elif ball_x > window_width:
        score_j1 += 1
    return score_j1, score_j2


def reset_ball(window_resolution, ball_speed_x):
    x = window_resolution[0] / 2
    y = window_resolution[1] / 2
    ball_speed_x = -ball_speed_x
    return x, y, ball_speed_x
