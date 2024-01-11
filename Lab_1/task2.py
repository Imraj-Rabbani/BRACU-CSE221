input_file=open("input2.txt","r")
output_file=open("output2.txt","w")


num = input_file.readline()
line = input_file.readline()
arr = list(map(int,line.split(" ")))


def bubbleSort(arr):

    for i in range(len(arr)-1):
        flag = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=False

        if flag == True:
            break

    for item in arr:
        output_file.write(f"{item} ") 
    
bubbleSort(arr)
'''
In the best case scenario, the condition within the inner loop does not become true at any point,
so the value of flag does not change to false if the given array is already sorted. After the 
inner loop has been traversed once, we check if the flag is true, if it is true it means the
array was sorted as it could not enter the loop.Therefore, making the time comlexity for 
the inner loop constant. Hence, we can acheive 0(n) in best case scenario.
'''


input_file.close()
output_file.close()