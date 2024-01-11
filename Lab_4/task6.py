input_file = open('input6.txt','r')
output_file = open('output6.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

grid=[]
for i in range(node):
    grid.append(list(input_file.readline().strip()))
print(grid)


def dfs(grid, row, col, visited):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0
    
    if grid[row][col] == 'D':
        diamonds = 1
    else:
        diamonds = 0
    visited[row][col] = 1
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        diamonds += dfs(grid, row + dr, col + dc, visited)

    return diamonds



def max_diamonds(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = []

    for num in range(rows):
        visited.append([0]*cols)
    max_diamond_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                diamonds_collected = dfs(grid, i, j, visited)
                max_diamond_count = max(max_diamond_count, diamonds_collected)

    return max_diamond_count

result = max_diamonds(grid)
print(result)
output_file.write(f"{result}")



input_file.close()
output_file.close()

#GPT's code :P