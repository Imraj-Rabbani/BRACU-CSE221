input_file = open("input1b.txt","r")
output_file = open("output1b.txt","w")

first_line = list(map(int,input_file.readline().split(" ")))
i = 0
j = first_line[0] - 1
count = first_line[1]
arr = list(map(int,input_file.readline().split(" ")))

flag = True
while i<j:
    if arr[i]+arr[j]==count:
        output_file.write(f"{i+1} {j+1}")
        flag = False
        break
    elif arr[i]+arr[j]<count:
        i+=1
    elif arr[i]+arr[j]>count:
        j-=1
    
if flag:
    output_file.write(f"Impossible")


input_file.close()
output_file.close()