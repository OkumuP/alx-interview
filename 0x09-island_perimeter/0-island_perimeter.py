#!/usr/bin/python3
'''
Island is Perimeter function
'''
def island_perimeter(grid):
    '''
    Calculates and returns the perimeter of an island
    '''
    width = len(grid[0])
    height = len(grid)
    perimeter = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
