input_file = open("input1.txt","r")
output_file = open("output1.txt","w")

num = int(input_file.readline())

arr = list(map(int,input_file.readline().split(" ")))

#Merging the two sorted list, passed the mergeSort function
def merge(a, b):
    i = 0
    j = 0
    sorted_arr = []
    #loop breaks when any one list is completely iterated
    while i<len(a) and j<len(b) :
        #checks which element is smaller and then appends that element into the sorted_arr.
        if a[i]<=b[j]:
            sorted_arr.append(a[i])
            i+=1
        else:
            sorted_arr.append(b[j])
            j+=1
    if i == len(a):
        sorted_arr=sorted_arr+b[j:]
    else:
        sorted_arr=sorted_arr+a[i:]
    return sorted_arr  


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])   
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)          

new_list = mergeSort(arr)
for item in new_list:
   output_file.write(f"{item} ") 

input_file.close()
output_file.close()