input_file = open('input1.txt','r')
output_file = open('output1.txt','w')

from heapq import heappop, heappush


node,edge = tuple(map(int,input_file.readline().split(" ")))

graph = {}

for node in range(node+1):
    graph[node]=[]

for item in range(edge):
    u,v,w = tuple(map(int,input_file.readline().split(" ")))
    graph[u].append((v,w))


def dijkstra(graph,source):
    visited = [0]*(node+1)
    distance = [float("inf")]*(node+1)
    distance[source] = 0
    priority_queue = []
    heappush(priority_queue,(0,source))
    while priority_queue:
        dist, index = heappop(priority_queue)
        visited[index] = 1
        for v in graph[index]:
            if visited[v[0]]==0:
                new_dist = distance[index]+v[1]
                if new_dist<distance[v[0]]:
                    distance[v[0]]=new_dist
                    heappush(priority_queue,(new_dist,v[0]))

    for idx in range(1,len(distance)):
        if distance[idx]==float("inf"):
            output_file.write(f"{-1} ")
        else:
            output_file.write(f"{distance[idx]} ")
    
source = int(input_file.readline())

dijkstra(graph,source)



input_file.close()
output_file.close()