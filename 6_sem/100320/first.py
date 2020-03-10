import sys, pygame, math
pygame.init()

screen_size = width, height = 1280, 720
size = width / 0.1, height / 0.1
DX, DY = 0.1, 0.1
speed = [4, 4]
black = 0, 0, 0


def convert(x, y):
    return (math.floor(x * DX) , math.floor(y * DY))


pygame.time.set_timer(pygame.USEREVENT, 10)

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
x, y = size[0] / 2, size[1] / 2

ball_rect = ball.get_rect();

pull = False
was = [False, False]

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: 
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and ball_rect.collidepoint(event.pos) and not pull:
            pull = True
    elif event.type == pygame.MOUSEMOTION and pull:
        x, y = event.pos[0] / DX, event.pos[1] / DY
    elif event.type == pygame.MOUSEBUTTONUP and pull:
        pull = False
    elif event.type == pygame.USEREVENT:
        x, y = x + speed[0], y + speed[1]

        if ball_rect.left < 0 or ball_rect.right > width:
            if not was[0]:
                speed[0] = -speed[0]
                was[0] = True
        else:
            was[0] = False
        if ball_rect.top < 0 or ball_rect.bottom > height:
            if not was[1]:
                speed[1] = -speed[1]
                was[1] = True
        else:
            was[1] = False

    new_coords = convert(x, y)
    ball_rect.center = new_coords
    
    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()

