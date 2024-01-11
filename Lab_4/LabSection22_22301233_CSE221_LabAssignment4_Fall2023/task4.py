input_file = open('input4.txt','r')
output_file = open('output4.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))

adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

#storing the edges for each nodes
for i in range(edge):
    u,v = tuple(map(int,input_file.readline().split(" ")))
    adj_list[u].append((v))

print(adj_list)

color={}
for i,j in adj_list.items():
    if j!=[]:
        color[i]=0

print(color,"color")

flag = False
def isCyclic(graph,s,edge,count):
    global color, flag
    if edge==count:
        return
    if s not in color.keys():
        for u in color.keys():
            color[u]=0
            print(color)
    else:
        color[s]=1
        for u in graph[s]:
            if u in color.keys():
                if color[u]==1:
                    flag = True
                    
        for u in graph[s]:
            if u in color.keys():
                if color[u]!=1:
                    print(u,end=", ")
                    isCyclic(graph,u,edge,count+1)
                    
            else:
                for u in color.keys():
                    color[u]=0

isCyclic(adj_list,1,edge,0)
print(flag)
if flag:
    output_file.write("Yes")
else:
    output_file.write("No")

input_file.close()
output_file.close()