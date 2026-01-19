def ball(
    ball_position_x,
    ball_position_y,
    ball_speed_x,
    ball_speed_y,
    width_joueur1,
    height_joueur1,
    position_x_joueur1,
    position_y_joueur1,
    position_x_joueur2,
    position_y_joueur2,
    window_resolution
):
    ball_radius = 20
    SPEED = 6
    rebond = False 

    # Rebond sur les bords haut et bas
    if ball_position_y - ball_radius <= 0 or ball_position_y + ball_radius >= window_resolution[1]:
        ball_speed_y = -ball_speed_y

    
    # Collision avec le joueur 1    
    if (ball_position_x - ball_radius <= position_x_joueur1 + width_joueur1
        and position_y_joueur1 <= ball_position_y <= position_y_joueur1 + height_joueur1):
        ball_speed_x = -ball_speed_x
        rebond = True  

   
    # Collision avec le joueur 2
    elif (ball_position_x + ball_radius >= position_x_joueur2
          and position_y_joueur2 <= ball_position_y <= position_y_joueur2 + height_joueur1):
        ball_speed_x = -ball_speed_x
        rebond = True  


    if ball_position_x < 0 or ball_position_x > window_resolution[0]:
        ball_position_x = window_resolution[0] / 2
        ball_position_y = window_resolution[1] / 2
        ball_speed_x = SPEED if ball_speed_x > 0 else -SPEED
        ball_speed_y = SPEED if ball_speed_y > 0 else -SPEED

    ball_position_x += ball_speed_x
    ball_position_y += ball_speed_y

    return ball_position_x, ball_position_y, ball_speed_x, ball_speed_y, rebond
