import pygame 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
square_size = 25

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    # Rect(x, y, width, heigth)
    square_rect = pygame.Rect((screen.get_width() / 2) - square_size / 2,(screen.get_height() / 2) - square_size / 2,square_size,square_size)
    pygame.draw.rect(screen, "white", square_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
