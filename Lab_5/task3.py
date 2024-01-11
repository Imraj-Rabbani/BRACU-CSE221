input_file = open("input3.txt","r")
output_file = open("output3.txt","w")

nodes, edges = tuple(map(int,input_file.readline().split(" ")))

graph = {}
trans_graph = {}
for node in range(1,nodes+1):
    graph[node]=[]
    trans_graph[node]=[]

for edge in range(edges):
    u,v = tuple(map(int,input_file.readline().split(" ")))
    graph[u].append(v)
    trans_graph[v].append(u)

print(graph,"graph")
print(trans_graph,"trans")


visited = [0]*(nodes+1)
stack = []
def dfs(graph,source):
    visited[source]=1
    for v in graph[source]:
        if visited[v]==0:
            dfs(graph,v)

    stack.append(source)

def connected(trans_graph,source):
    travelled[source]=1
    scc.append(source)
    for v in trans_graph[source]:
        if travelled[v]==0:
            connected(trans_graph,v)

for u in graph.keys():
    if visited[u]==0:
        dfs(graph,u)

print(stack)

travelled = [0]*(nodes+1)
all_scc=[]
while stack:
    u = stack.pop()
    if travelled[u]==0:
        scc=[]
        connected(trans_graph,u)
        all_scc.append(scc)

for item in all_scc:
    output_file.write(f'{item}\n')


input_file.close()
output_file.close()