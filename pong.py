import pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ping Pong GAME")

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 8
paddle_left_x = 30
paddle_left_y = screen_height / 2 - paddle_height / 2
paddle_right_x = screen_width - 30 - paddle_width
paddle_right_y = screen_height / 2 - paddle_height / 2

# Set up the ball
ball_size = 15
ball_speed = 6
ball_x = screen_width / 2 - ball_size / 2
ball_y = screen_height / 2 - ball_size / 2
ball_dx = ball_speed
ball_dy = ball_speed

# Set up the score
score_left = 0
score_right = 0
font = pygame.font.Font(None, 36)

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_left_y > 0:
        paddle_left_y -= paddle_speed
    if keys[pygame.K_s] and paddle_left_y < screen_height - paddle_height:
        paddle_left_y += paddle_speed
    if keys[pygame.K_UP] and paddle_right_y > 0:
        paddle_right_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_right_y < screen_height - paddle_height:
        paddle_right_y += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off walls
    if ball_y < 0 or ball_y + ball_size > screen_height:
        ball_dy = -ball_dy
    if ball_x < 0:
        score_right += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_dx = ball_speed
        ball_dy = ball_speed
    if ball_x + ball_size > screen_width:
        score_left += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_dx = -ball_speed
        ball_dy = -ball_speed

    # Bounce off paddles
    if ball_x < paddle_left_x + paddle_width and ball_y + ball_size > paddle_left_y and ball_y < paddle_left_y + paddle_height:
        ball_dx = ball_speed
    if ball_x + ball_size > paddle_right_x and ball_y + ball_size > paddle_right_y and ball_y < paddle_right_y + paddle_height:
        ball_dx = -ball_speed

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_left_x, paddle_left_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right_x, paddle_right_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x + ball_size / 2), int(ball_y + ball_size / 2)), int(ball_size / 2))
    left_score_text = font.render(str(score_left), True, (255, 255, 255))
    right_score_text = font.render(str(score_right), True, (255, 255, 255))
    screen.blit(left_score_text, (screen_width / 4 - left_score_text.get_width() / 2, 10))
    screen.blit(right_score_text, (screen_width * 3 / 4 - right_score_text.get_width() / 2, 10))
    pygame.display.update()

    # Check for game over
    if score_left >= 10 or score_right >= 10:
        game_over = True

    # Limit the frame rate
    clock.tick(60)

# Show the winner
if score_left > score_right:
    winner_text = font.render("Left player wins!", True, (255, 255, 255))
else:
    winner_text = font.render("Right player wins!", True, (255, 255, 255))
screen.blit(winner_text, (screen_width / 2 - winner_text.get_width() / 2, screen_height / 2 - winner_text.get_height() / 2))
pygame.display.update()

# Wait for user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()