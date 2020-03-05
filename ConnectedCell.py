

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1,0]

visited = []

length = 0
current_length = 0

def initialize(matrix):

    global visited

    height = len(matrix)
    width = len(matrix[0])

    visited = [ ([0] * width) for i in range(height) ]


#Checks If cell is valid or not
def isValid(y,x,matrix):

    height = len(matrix)
    width = len(matrix[0])

    if x >= 0 and x < width and y >= 0 and y < height:
        return True
    else: 
        return False



def dfs(y,x,matrix):

    global current_length 
    current_length += 1

    global visited
    visited[y][x] = 1

    print('Current Cell: %s,%s >>> length %s'%(y,x,current_length))

    for i in range(0,8):

        targetY = y + dy[i]
        targetX = x + dx[i]

        if isValid(targetY, targetX, matrix) and matrix[targetY][targetX] == 1 and visited[targetY][targetX] == 0: 
            return dfs(targetY, targetX, matrix)


def connectedCell(matrix):

    initialize(matrix)
    height = len(matrix)
    width = len(matrix[0])

    global visited 
    global current_length
    global length

    for y in range(0,height):
        for x in range(0,width):

            print('--- START DFS at (%s,%s) ---'%(y,x))
            current_length = 0
            initialize(matrix)
            if matrix[y][x] == 1 :
                dfs(y,x,matrix)

                if current_length > length :
                    length = current_length

            print('--- END DFS at (%s,%s) LENGTH: %s---\n\n'%(y,x,current_length))

        print('--- END LOOP ---')

    return length

#matrix = [[0,0,1,1], [0,1,0,0], [0,1,1,0], [0,1,0,0], [1,1,0,0]]

matrix = [[0,1,0, 0, 0, 0, 1, 1, 0], [1, 1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 0, 0]]

#matrix = [[1,0,0,1,0,1,0,0],[0,0,0,0,0,0,0,1],[1,0,1,0,1,0,0,0],[0,0,0,0,0,0,1,0], [1,0,0,1,0,0,0,0], [0,0,0,0,0,0,0,1], [0,1,0,0,0,1,0,0]]

print(connectedCell(matrix))