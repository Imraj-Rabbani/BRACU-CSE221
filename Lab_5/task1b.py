input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")

from collections import deque

num , preq = list(map(int,input_file.readline().split(" ")))

graph = {}
 
for node in range(1,num+1):
    graph[node] = []

for i in range(preq):
    u, v = list(map(int,input_file.readline().split(" ")))
    graph[u].append(v)

print(graph,"graph")

#Checking if the graph is cyclic or not
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

#Calculating the in-degrees for each node
in_degrees = [0]*(num+1)
for key,values in graph.items():
    for v in values:
        in_degrees[v]+=1

queue = deque()
#storing the nodes with 0 in-degree in a queue
for i in range(1,len(in_degrees)):
    if in_degrees[i]==0:
        queue.append(i)

print(queue)
print(in_degrees)

result = []
#Using bfs to traverse through the path and reducing in-degrees for each node
def top_sort(graph,source):
    #appending the source into the result as it has 0 in-degrees meaning no pre-requisite 
    result.append(source)
    q = deque()
    q.append(source)
    while q:
        u = q.popleft()
        for v in graph[u]:
            q.append(v)
            in_degrees[v]-=1
            if in_degrees[v]==0:
                result.append(v)
            #when a node has 0 in-degree it has no pre-requisite so can be appended to result

for u in graph.keys():
    visited = [0]*(node+1)
    isCyclic(graph,u)

if flag:
    while queue:
        #Only the nodes with 0 in-degrees are send to top_sort
        u = queue.popleft()
        top_sort(graph,u)
    output_file.write(f"{result}")
else:
    output_file.write("Impossible")



input_file.close()
output_file.close()