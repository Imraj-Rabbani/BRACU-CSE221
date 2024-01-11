input_file = open('input4.txt','r')
output_file = open('output4.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

graph ={}
for n in range(node+1):
    graph[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))
    graph[u].append((v))
print(graph,"graph")


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


for u in graph.keys():
    visited = [0]*(node+1)
    isCyclic(graph,u)

if flag:
    print("not cyclic")
else:
    print("cyclic")
input_file.close()
output_file.close()