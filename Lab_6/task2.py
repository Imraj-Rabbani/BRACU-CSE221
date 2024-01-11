input_file = open('input2.txt','r')
output_file = open('output2.txt','w')

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

    return(distance[1:])
    
    
s1,s2 = tuple(map(int,input_file.readline().split(" ")))


short_d1 = dijkstra(graph,s1)#returned distance array
short_d2 = dijkstra(graph,s2)


# Storing the common nodes that are traversed by both sources
common=[]
for idx in range(len(short_d1)):
    if short_d1[idx]!=float("inf") and short_d2[idx]!=float("inf") and short_d1[idx]!=0 and short_d2[idx]!=0:
        if short_d1[idx]>=short_d2[idx]:

          common.append([idx+1,short_d1[idx]])
        else:
          common.append([idx+1,short_d2[idx]])

    
if common==[]:
    output_file.write("Impossible")
else:    
    x = float("inf")
    for item in common:
        if item[1]<x:
            x=item[1]
            min_time=item
    output_file.write(f"Time {min_time[1]}\nNode {min_time[0]}")


input_file.close()
output_file.close()