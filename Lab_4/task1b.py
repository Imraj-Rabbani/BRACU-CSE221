input_file = open('input1b.txt','r')
output_file = open('output1b.txt','w')


node,edge = tuple(map(int,input_file.readline().split(" ")))

#Creating a dictionary to store the nodes and its edges
adj_list ={}
for n in range(node+1):
    adj_list[n]=[]

#storing the edges,weight for each nodes
for i in range(edge):
    u,v,w = tuple(map(int,input_file.readline().split(" ")))
    adj_list[u].append((v,w))


print(adj_list)


#string formatting according to the question
for j in range(node+1):
    output_file.write(f"{j} : ")

    for item in adj_list[j]:
        output_file.write(f"{item} ")

    output_file.write(f"\n")


input_file.close()
output_file.close()