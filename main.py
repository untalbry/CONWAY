import pygame 

#Initial configuration 
width, height = 1280, 720
bg = 25, 25, 25
running = True


pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(bg)
clock = pygame.time.Clock()

cell_size = 40  # Tamaño fijo de cada celda
num_columns = width // cell_size
num_rows = height // cell_size

#Main loop 
while running:
    #EXIT 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Draw grid
    for y in range(0, num_rows):
        for x in range(0, num_columns): 
            poly = [((x)    *   cell_size, y       * cell_size),
                    ((x+1)  *   cell_size, y       * cell_size),
                    ((x+1)  *   cell_size, (y+1)   * cell_size),
                    ((x)    *   cell_size, (y+1)   * cell_size)
            ]
            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    pygame.display.flip()
    clock.tick(60)
pygame.quit() 