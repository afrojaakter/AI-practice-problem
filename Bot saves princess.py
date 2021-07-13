'''
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input

3
---
-m-
p--
Sample output

DOWN
LEFT
'''
#!/usr/bin/python
'''
    Matrix Convention:A board of size m x n has top left indexed (0,0) and bottom right indexed (m-1,n-1). The row index increases
    from top to bottom, and the column index increases from left to right.
    So, 
    - negative row difference implies bot needs to go UP
    - negative col difference implies bot needs to go LEFT'''

def displayPathtoPrincess(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot = (i, j)
            if grid[i][j] == 'p':
                princes = (i, j)
    steps_x = princes[1] - bot[1]
    steps_y = princes[0] - bot[0]
    return ''.join(['LEFT\n'*abs(steps_x) if steps_x < 0 else 'RIGHT\n'*steps_x,
                    'UP\n'*abs(steps_y) if steps_y < 0 else 'DOWN\n'*steps_y])

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

print(displayPathtoPrincess(m,grid))
