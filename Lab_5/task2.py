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

print(in_degrees,"degree")



result = []
'''
To have a top_sort in lexological order, the approach is we start from a source that has 
zero in_degrees, we will append it our result list. Then we reduce the in-degree of the vertex
that our source can move to. If any of the vertex it can move now have an in-degree of 0 after
reducing, we will append it our queue. Then we will sort the queue in ascending order. So now
everytime a source is passed to top_sort it will be the smallest one
'''

def top_sort(graph,source):
    result.append(source)
    
    for v in graph[source]:
        in_degrees[v]-=1 
        if in_degrees[v]==0:
            queue.append(v)

for u in graph.keys():
    visited = [0]*(node+1)
    isCyclic(graph,u)

if flag:
    while queue:
        queue = deque(sorted(queue))
        #Before call the top_sort function we sort the queue so that the source is always the smallest one.
        u = queue.popleft()
        top_sort(graph,u)
    output_file.write(f"{result}")
    print(result)
else:
    output_file.write("Impossible")



input_file.close()
output_file.close()