input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")

num , preq = list(map(int,input_file.readline().split(" ")))

graph = {}
 
for node in range(num+1):
    graph[node] = []

for i in range(preq):
    u, v = list(map(int,input_file.readline().split(" ")))
    graph[u].append(v)

print(graph)

flag = True
def isCyclic(graph,source):
    global visited,flag
    if flag==True:
        visited[source]=1
        for v in graph[source]:
            if visited[v]==0:
                isCyclic(graph,v)
                visited[v]=0
            elif visited[v]==1:
                flag = False

stack = []
def top_sort(graph,source):
    if ([source] in graph.values()) or (graph[source]!=[]):
        visited[source]=1
        for v in graph[source]:
            if visited[v]==0:
                top_sort(graph,v)
        stack.append(source)
        
for u in graph.keys():
    visited = [0]*(node+1)
    isCyclic(graph,u)

visited = [0]*(num+1)
if flag:
    for node in graph.keys():
        if visited[node]==0:
            top_sort(graph,node)
    output_file.write(f"{stack[-1::-1]}")
    print(stack[-1::-1])
else:
    output_file.write("Impossible")



input_file.close()
output_file.close()