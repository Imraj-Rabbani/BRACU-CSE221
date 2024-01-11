input_file = open('input2.txt','r')
output_file = open('output2.txt','w')

from collections import deque

node,edge = tuple(map(int,input_file.readline().split(" ")))

#creating a dictionary to store the nodes and its edges
adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))

    adj_list[u].append((v))
    adj_list[v].append((u))
    #bidirectional paths

print(adj_list)

def bfs(graph,s):
    color={}

    for i,j in graph.items():
        if j!=[]:
            color[i]=0
    print(color)

    queue = deque()
    queue.append(s)
    color[s]=1
    while queue:
        u = queue.popleft()
        output_file.write(f"{u} ")
        for v in graph[u]:
            if color[v]==0:
                color[v]=1
                queue.append(v)

bfs(adj_list,1)


input_file.close()
output_file.close()