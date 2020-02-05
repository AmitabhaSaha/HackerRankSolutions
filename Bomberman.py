

def transform(current, target, grid):

    if target%2 == 0: 
        
        height = len(grid)
        width = len(grid[0])

        strap = ['O'] * width
        res = []
        for _ in range(height):
            res.append(''.join(strap))

        return res

    else: 
        if current+1 == target or current == target:
            return grid
        else: 
            return transform(current+2, target, step(grid))


def step(grid):

    height = len(grid)
    width = len(grid[0])

    res = []
    for i in range(height):
        strap = []

        for j in range(width):

            left_cell = checlleftCellFor(i,j,grid)
            right_cell = checkRightCellFor(i,j,grid)
            top_cell = checkTopCellFor(i,j,grid)
            bottom_cell = checkBottomCellFor(i,j,grid)
            self_cell = checkSelf(i,j,grid)

            if left_cell or right_cell or top_cell or bottom_cell or self_cell:
                strap.append('.')
            else:
                strap.append('O')    

        res.append(''.join(strap))

    return res


def checkTopCellFor(i, j, grid):

    if i == 0:
        return False
    elif ord(grid[i-1][j]) == 79:
        return True
    else :
        return False

def checlleftCellFor(i, j, grid):

    if j == 0:
        return False
    elif ord(grid[i][j-1]) == 79:
        return True
    else :
        return False

def checkRightCellFor(i, j, grid):

    width = len(grid[0])

    if j == width-1:
        return False
    elif ord(grid[i][j+1]) == 79:
        return True
    else :
        return False

def checkBottomCellFor(i, j, grid):

    height = len(grid)

    if i == height-1:
        return False
    elif ord(grid[i+1][j]) == 79:
        return True
    else :
        return False

def checkSelf(i, j, grid):

    if ord(grid[i][j]) == 79:
        return True
    else :
        return False

def bomberMan(n, grid):
    x = n%4 
    if x == 1 and n>1: 
        x += 4
    return transform(1, x, grid)


grid= ['O..OO........O..O........OO.O.OO.OO...O.....OOO...OO.O..OOOOO...O.O..O..O.O..OOO..O..O..O....O...O....O...O..O..O....O.O.O.O.....O.....OOOO..O......O.O.....OOO....OO....OO....O.O...O..OO....OO..O...O']
print(bomberMan(19, grid))
