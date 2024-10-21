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

cell_size = 20 
num_columns = width // cell_size
num_rows = height // cell_size

gameState = np.zeros((num_rows, num_columns))

#My first automata
gameState[1,1]=1
gameState[2,2]=1
gameState[2,3]=1
gameState[1,3]=1
gameState[0,3]=1

#Main loop 
while running:
    newGameState = np.copy(gameState)
    screen.fill(bg)
    #Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pause = not pause
        if pause: 
            mouse_click = pygame.mouse.get_pressed()
            if sum(mouse_click) > 0:
                pos_x, pos_y = pygame.mouse.get_pos()  
                cel_x, cel_y = int(pos_x / cell_size), int(pos_y / cell_size) 
                if 0 <= cel_x < num_columns and 0 <= cel_y < num_rows:
                    newGameState[cel_y, cel_x] = not mouse_click[2]

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