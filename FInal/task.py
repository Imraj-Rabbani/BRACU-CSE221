input_file = open("input.txt","r")
output_file = open("output.txt","w")
from collections import deque

nodes, edges = list(map(int,input_file.readline().split(" ")))
# print(nodes,edges)

vertices = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]


graph = {}
for vertex in vertices:
    graph[vertex]=[]

for edge in range(edges):
    u,v = list(map(str,input_file.readline().split("*")))
    v = v[0]
    graph[u].append(v)

# print(graph)

output_file.write(f"Adjacency List: {graph}\n")
#Q1 & 2 done

visited = []
lift1 = []
lift2 = []
def bfs(graph,source):
    level = 0
    queue = deque([(source,level)])
    while queue:
        u,lev = queue.popleft()
        visited.append(u)
        # print(u,lev)
        if lev%2==0 and lev!=0 and u not in lift1 and u not in lift2:
            lift2.append(u)
        elif lev%2==1 and u not in lift1 and u not in lift2:
            lift1.append(u)

        for v in graph[u]:
            if v not in visited:
                queue.append((v,lev+1))


bfs(graph,"a")
print(lift1,lift2)
output_file.write(f"Lift 1: {lift1}\nLift 2: {lift2} ")


input_file.close()
output_file.close()