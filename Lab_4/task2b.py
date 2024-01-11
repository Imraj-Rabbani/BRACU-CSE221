input_file = open('input2.txt','r')
output_file = open('output2.txt','w')

from collections import deque

node,edge = tuple(map(int,input_file.readline().split(" ")))

graph ={}
for n in range(node+1):
    graph[n]=[]

for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))

    graph[u].append((v))
    graph[v].append((u))

print(graph)

visited = [0]*(node+1)
def bfs(graph,source):
    visited[source]=1
    queue = deque([source])
    print(queue)
    while queue:
        u = queue.popleft()
        print(u)
        for v in graph[u]:
            if visited[v]==0:
                queue.append(v)
                visited[v]=1
                
bfs(graph,1)