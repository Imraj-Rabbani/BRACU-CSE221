input_file = open('input6.txt','r')
output_file = open('output6.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

# Reading the grid from the input file and converting it into a nested list(matrix)

grid=[list(input_file.readline().strip())]
for i in range(node-1):
    grid.append(list(input_file.readline().strip()))
print(grid)


# Depth-First Search (DFS) function to count diamonds
def dfs(grid, row, col, visited):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    if grid[row][col] == 'D':
        visited[row][col] = 1
        diamonds = 1
    else:
        diamonds = 0

    visited[row][col] = 1
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:#As the edges can form only to the adjacent points
        diamonds += dfs(grid, row + dr, col + dc, visited)

    return diamonds


# Function to find the maximum number of diamonds
def max_diamonds(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = []
    #Creating a nested list to keep track of the visited vertices
    for num in range(rows):
        visited.append([0]*cols)
    # print(visited)
    max_diamond_count = 0

    #Traversing through the matrix
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                diamonds_collected = dfs(grid, i, j, visited)
                max_diamond_count = max(max_diamond_count, diamonds_collected)
    print(visited)
    return max_diamond_count

result = max_diamonds(grid)
print(result)
output_file.write(f"{result}")



input_file.close()
output_file.close()