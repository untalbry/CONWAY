import pygame 
import numpy as np
#Initial configuration 
width, height = 1280, 720
bg = 25, 25, 25
running = True
pause = False

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(bg)
clock = pygame.time.Clock()

cell_size = 40  # Tamaño fijo de cada celda
num_columns = width // cell_size
num_rows = height // cell_size

#cells flags : alive = 1 death = 0 
gameState = np.zeros((num_rows, num_columns))

#My first automata
gameState[1,1]=1
gameState[2,2]=1
gameState[2,3]=1
gameState[1,3]=1
gameState[0,3]=1

#Main loop 
while running:
    #Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
    newGameState = np.copy(gameState)
    screen.fill(bg)
    #Draw grid
    for y in range(0, num_rows):
        for x in range(0, num_columns):
            if not pause: 
                num_neighbors = (
                    gameState[(y - 1) % num_rows, (x - 1) % num_columns] + 
                    gameState[(y - 1) % num_rows, (x) % num_columns] + 
                    gameState[(y - 1) % num_rows, (x + 1) % num_columns] + 
                    gameState[(y) % num_rows, (x - 1) % num_columns] + 
                    gameState[(y) % num_rows, (x + 1) % num_columns] + 
                    gameState[(y + 1) % num_rows, (x - 1) % num_columns] + 
                    gameState[(y + 1) % num_rows, (x) % num_columns] + 
                    gameState[(y + 1) % num_rows, (x + 1) % num_columns]
                )
        
                # Rule 1: A death cell with 3 living neighbors cells can be revived
                if gameState[y, x] == 0 and num_neighbors == 3:
                    newGameState[y, x] = 1 
                # Rule 2: A living cell with less than 2 living neighboring cells or more than 3 living neighboring cells dies...
                elif gameState[y,x] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                    newGameState[y,x] = 0
                # Definition of a polygon    
            poly = [((x)    *   cell_size, y       * cell_size),
                    ((x+1)  *   cell_size, y       * cell_size),
                    ((x+1)  *   cell_size, (y+1)   * cell_size),
                    ((x)    *   cell_size, (y+1)   * cell_size)
            ]
            #Drawing things 
            if newGameState[y,x] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else: 
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = newGameState
    pygame.display.flip()
    clock.tick(10)
pygame.quit() 