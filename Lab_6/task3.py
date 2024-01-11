input_file = open('input3.txt','r')
output_file = open('output3.txt','w')
from collections import deque

nodes,queries = tuple(map(int,input_file.readline().split(" ")))


#Keeping track of the parent node so that we can find root node from any node
parent = [-1]*(nodes+1)


graph = {}
for i in range(1,nodes+1):
    graph[i]=[]


def dfs(graph,source):
    global count
    visited[source]=1
    for v in graph[source]:
        if visited[v]==0:
            count += 1
            dfs(graph,v)

#This function returns the root of any node
def root(vertex):
    if parent[vertex]==-1:
        return vertex
    else:
        return root(parent[vertex])

for query in range(queries):
    u,v = tuple(map(int,input_file.readline().split(" ")))
    #At first we find the roots of the given nodes
    a = root(u)
    b = root(v)
    #If the roots are not same, meaning they are not cyclic
    if a!=b:
        #We can join v's root to u's root
        parent[b]=a
        graph[a].append(b)
    count = 1
    visited=[0]*(nodes+1)
    dfs(graph,a)
    # print(count)
    output_file.write(f"{count}\n")

input_file.close()
output_file.close()