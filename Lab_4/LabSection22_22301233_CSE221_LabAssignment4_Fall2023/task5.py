input_file = open('input5.txt','r')
output_file = open('output5.txt','w')

from collections import deque

node,edge,dest = tuple(map(int,input_file.readline().split(" ")))

#creating a dictionary to store the nodes and its edges
adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))
    adj_list[u].append((v))
    adj_list[v].append((u))

print(adj_list)


def shortest_path(graph, s, dest):
    if s == dest:
        return [s], 0  # Return the start node and 0 vertices passed

    queue = deque([(s, [s], 0)])  # Initialize the count to 0
    visited = []#storing all the visited vertices

    while queue:
        u, path, time = queue.popleft()

        if u == dest:
            return path, time

        visited.append(u)

        for v in graph[u]:
            if v not in visited:
                queue.append((v, path + [v], time + 1))#storing the path and time for each new vertices
                visited.append(v)


path,time = shortest_path(adj_list, 1, dest)
# print(path)
# print(time)
output_file.write(f"Time: {time}\n")
output_file.write(f"Shortest Path:")
for item in path:
    output_file.write(f" {item}")

input_file.close()
output_file.close()