input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")

first_line = list(map(int,input_file.readline().split(" ")))
num = first_line[0]
count = first_line[1]
arr = list(map(int,input_file.readline().split(" ")))

flag = True
for i in range(num):
    for j in range(i+1,num):
        if arr[i]+arr[j]==count:
            output_file.write(f"{i+1} {j+1}")
            flag = False
            break
    if flag==False:
        break

if flag:
    output_file.write(f"Impossible")


input_file.close()
output_file.close()