input_file = open("input4.txt","r")
output_file = open("output4.txt","w")


line = list(map(int,input_file.readline().split(" ")))
num = line[0]#Number of inputs
person = [[0]*2]*line[1] #2D array, it contains the time slots if assigned to each person


#appending the given task's time slots in the time list
time = []
for item in range(num):
    line = list(map(int,input_file.readline().split(" ")))
    time.append(line)

print(time)

def mergesort(arr):
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        a = mergesort(arr[:mid])
        b = mergesort(arr[mid:])
        return merge(a,b)

def merge(a,b):
    i = 0
    j = 0 
    new_arr=[]
    while i<len(a) and j<len(b):
        if a[i][1]<=b[j][1]:
            new_arr.append(a[i])
            i+=1
        else:
            new_arr.append(b[j])
            j+=1
    if i==len(a):
        for item in range(j,len(b)):
            new_arr.append(b[item])
    else:
        for item in range(i,len(a)):
            new_arr.append(a[item])
    return new_arr


sorted_time=mergesort(time)
print(sorted_time)
print(person)

#storing the difference of each person's current task's ending time with the next task's starting time
count = 0
for i in range(num):
    flag = False
    diff = [-1]*len(person)

    for j in range(len(person)):
        if person[j][1]<=sorted_time[i][0]:
            diff[j]=sorted_time[i][0]-person[j][1]
            flag = True

#if the task is assigned we increase the count
    if flag:
        count+=1
        min = float('inf')
        k = 0
        idx = 0
#assigning the task to the person who has the smallest time difference 
        for value in diff:
            if value<min and value!=-1:
                min=value
                idx=k
            k+=1
        person[idx]=sorted_time[i]    



output_file.write(f'{count}')

input_file.close()
output_file.close()