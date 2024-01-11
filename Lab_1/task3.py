input_file = open("input3.txt","r")
output_file = open("output3.txt","w")

num = int(input_file.readline())

second_line = input_file.readline().split(" ")
id = list(map(int,second_line))

third_line = input_file.readline().split(" ")
marks = list(map(int,third_line))

def sort(marks,id):
    for i in range(len(marks)):
        flag = True
        for j in range(len(marks)-1-i):
            if marks[j]<marks[j+1]:
                marks[j], marks[j+1] = marks[j+1], marks[j]
                id[j], id[j+1] = id[j+1], id[j]
                flag=False
        if flag == True:
            break


def output(marks,id):
    for i in range(num):
        if i == num-1:
            output_file.write(f"ID: {id[i]} Mark: {marks[i]}")
            break
        if marks[i]==marks[i+1]: 
            for j in range(i,num):
                for k in range(j+1,num):
                    if marks[j]==marks[k]:
                        if id[j]>id[k]:
                            id[j],id[k]=id[k],id[j]
        output_file.write(f"ID: {id[i]} Mark: {marks[i]}\n")

sort(marks,id)
output(marks,id)

input_file.close()
output_file.close()