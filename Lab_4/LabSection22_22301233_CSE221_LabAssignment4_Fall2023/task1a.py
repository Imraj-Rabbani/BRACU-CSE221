input_file = open('input1a.txt','r')
output_file = open('output1a.txt','w')

node,edge = tuple(map(int,input_file.readline().split(" ")))


#Creating an Empty N*N matrix where N=number of vertices 
adj_mat =[]
for n in range(node+1):
    adj_mat.append([0]*(node+1))


#Inserting the weight and the edge
for num in range(edge):
    u,v,w = tuple(map(int,input_file.readline().split(" ")))
    adj_mat[u][v]=w  

for items in adj_mat:
    output_file.write(f"{items}\n")

input_file.close()
output_file.close()