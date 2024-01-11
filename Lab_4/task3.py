input_file = open('input3.txt','r')
output_file = open('output3.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

adj_list ={}
for n in range(node+1):
    adj_list[n]=[]


for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))

    adj_list[u].append((v))
    adj_list[v].append((u))


visited = [0]*(node+1)
def dfs(graph,source):
    visited[source]=1
    print(source)
    for v in graph[source]:
        if visited[v]==0:
            dfs(graph,v)
    
dfs(adj_list,1)

input_file.close()
output_file.close()