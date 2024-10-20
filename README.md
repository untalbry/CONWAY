# CONWAY GAME  

To run please run the following commands 
```
 python3 -m venv venv
```
```
source venv/bin/activate
```
```
 pip install -r requirements.txt 
```
```
 python main.py
```


# Explanation 

To draw the grid, I use a fixed cell size and loop over the screen to paint each cell based on its coordinates. The grid is made up of squares, and each square is defined by its four corners using `pygame.draw.polygon`, calculated using the current position in the grid `(x, y)`, and adjusted for the size of the cells: 
```
 (x, y)--------------------(x+1, y)
    |                           |
    |                           |
    |                           |
 (x, y+1)------------------(x+1, y+1)
```