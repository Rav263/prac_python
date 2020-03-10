import sys, pygame, math
pygame.init()

screen_size = width, height = 1280, 720
size = width / 0.1, height / 0.1
DX, DY = 0.1, 0.1
speed = [2, 2]
black = 0, 0, 0


def convert(x, y):
    return (math.floor(x * DX) , math.floor(y * DY))

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
x, y = size[0] / 2, size[1] / 2

ball_rect = ball.get_rect();

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x, y = x + speed[0], y + speed[1]

    new_coords = convert(x, y)
    #print(x, y, new_coords)

    ball_rect.center = new_coords

    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()

