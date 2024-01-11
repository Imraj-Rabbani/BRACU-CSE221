input_file = open('input4.txt','r')
output_file = open('output4.txt','w')

from heapq import heappop, heappush


node,edge = tuple(map(int,input_file.readline().split(" ")))

graph = {}
mst_graph = {}
for node in range(node+1):
    graph[node]=[]
    mst_graph[node]=[]



priority_queue = []
for item in range(edge):
    u,v,w = tuple(map(int,input_file.readline().split(" ")))
    graph[u].append((v,w))
    graph[v].append((u,w))
    heappush(priority_queue,(w,(u,v)))

parents = [-1]*(node+1)
def root(vertex):
    if parents[vertex]==-1:
        return vertex
    else:
        return root(parents[vertex])

count = 0
while priority_queue:
    w,edge = heappop(priority_queue)
    a,b = edge
    u = root(a)
    v = root(b)
    if u!=v:
        count += w
        parents[v] = u
        mst_graph[a].append((b,w))


print(mst_graph)
output_file.write(f"{count}")
input_file.close()
output_file.close()