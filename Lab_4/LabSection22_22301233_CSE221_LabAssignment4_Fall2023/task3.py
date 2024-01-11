input_file = open('input3.txt','r')
output_file = open('output3.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))

    adj_list[u].append((v))
    adj_list[v].append((u))

# print(adj_list)

color={}
for i,j in adj_list.items():
    if j!=[]:
        color[i]=0

# print(color)

def DFS(graph,u):
    #visited vertices are marked as 1
    color[u]=1
    # print(u)
    output_file.write(f"{u} ")
    for v in graph[u]:
        if color[v]==0:
            DFS(graph,v)
    
    
DFS(adj_list,1)

input_file.close()
output_file.close()