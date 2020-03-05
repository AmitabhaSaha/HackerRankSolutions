
dRow =    [0,2,2,0,-2,-2]
dColumn = [2,1,-1,-2,-1,1]

graph = []
nodes = []
visited_nodes = []

length = 0
current_length = 0

start_node = (0,0)
target_node = (0,0)

isFeasible = False

def isValid(row, column, depth):

    if row >= 0 and row < depth and column >= 0 and column < depth:
        return True
    else: 
        return False

def initializeVisited(depth):

    global visited_nodes
    visited_nodes = [ ([0] * depth) for i in range(depth) ]


def initialize(depth):

    global graph
    graph = [ ([0] * depth) for i in range(depth) ]


def bfs(depth):

    while len(nodes) != 0:
        ((row, column)) = nodes[0]

        if isValid(row, column, depth) :

            global graph
            global target_node

            nodes.remove((row, column))

            for i in range(6):

                target_row = row+dRow[i]
                target_column = column+dColumn[i]

                (target_node_row, target_node_column) = target_node

                if isValid(target_row, target_column, depth) :

                    if graph[target_row][target_column] == 0 :
                        graph[target_row][target_column] = 1

                        nodes.append((target_row, target_column))
                        
                        if target_node_row == target_row and target_node_column == target_column :
                            global isFeasible
                            isFeasible = True

            if len(nodes) > 0 :
                return bfs(depth)


def dfs(row,column,depth, path):

    global visited_nodes
    print(path)

    for i in range(6):

        print('Node : %s, %s >>> LOOP: %s >>> Path : %s'%(row, column,i,path))

        #visited_nodes[row][column] == 1

        target_row = row+dRow[i]
        target_column = column+dColumn[i]

        if (target_row, target_column) not in path :

            global target_node
            (target_node_row, target_node_column) = target_node

            if target_node_row == target_row and target_node_column == target_column:
                print('Found')
                print('Path: %s'%(path))
                path.clear()
            
            # and visited_nodes[target_row][target_column] == 0 
            if isValid(target_row, target_column, depth) :
                path.append((target_row, target_column))
                
                dfs(target_row, target_column, depth, path)
        
        else: 
            print('Node Exists: %s, %s'%(target_row, target_column))


def printShortestPath(n, i_start, j_start, i_end, j_end):

    # Empty Graph
    initialize(n)
    initializeVisited(n)

    # Inilialise with start point
    global graph
    
    graph[i_start][j_start] = 1
    nodes.append((i_start,j_start))

    # set start and target node
    global target_node
    global start_node

    target_node = (i_end,j_end)
    start_node = (i_start,j_start)

    # Start traversing
    bfs(n)

    if isFeasible :
        path = [(i_start, j_start)]
        print('Possible')
        initializeVisited(n)
        dfs(i_start, j_start, n, path)
        #shortestPath(start_node, target_node)
    else: 
        print('Impossible')


printShortestPath(7, 6, 6, 0,1)