input_file = open("input6.txt","r")
output_file = open("output6.txt","w")

num = int(input_file.readline()) - 1
arr = list(map(int,input_file.readline().split(" ")))
queries = int(input_file.readline())


#we pass in the asked nth smallest number
def quickAlgo(arr,n,query):
    if n == -1:
        return
    else:
        count = partition(arr,n)#1
        #if the number of smaller values is equal to the query we just write that element in the output
        if count == query:
            output_file.write(f"{arr[n]}\n")
        #otherwise we call the function again, decreasing the n value by 1 so that we can omit the value that has been checked once.
        else:
            quickAlgo(arr,n-1,query)



def partition(arr,n):
    pivot = arr[n]
    count = 0
    for num in range(len(arr)):
        if arr[num]<=pivot:
            count+=1
    # print(count,"count")
    #returns the number of terms smaller the pivot number
    return count

for i in range(queries):
    query = int(input_file.readline())
    quickAlgo(arr,num,query)  



input_file.close()
output_file.close()