from collections import deque

input_file = open('input2.txt','r')
output_file = open('output2.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

#creating a dictionary to store the nodes and its edges
graph ={}
for n in range(node+1):
    graph[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))

    graph[u].append((v))
    graph[v].append((u))
    #bidirectional paths

print(graph)


def bfs(graph,s):
    visited={}
    for i,j in graph.items():
        if j!=[]:
            visited[i]=0
    print(visited)

    queue = deque()
    queue.append(s)
    visited[s]=1
    while queue:
        u = queue.popleft()
        output_file.write(f"{u} ")
        for v in graph[u]:
            if visited[v]==0:
                visited[v]=1
                queue.append(v)

bfs(graph,1)


input_file.close()
output_file.close()




