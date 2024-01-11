input_file = open("input5.txt","r")
output_file = open("output5.txt","w")

high = int(input_file.readline()) - 1

arr = list(map(int,input_file.readline().split(" ")))


def quickSort(arr,low,high):
    if low<high:
        pivot_idx = partition(arr,low,high)
        quickSort(arr,low,pivot_idx-1)
        quickSort(arr,pivot_idx+1,high)
        #recursively sends the list without the previous pivot element to reduce time complexity
    return arr

#partition function returns a list that sorts the pivot element
def partition(arr,low,high):
    pivot_idx = low-1
    pivot = arr[high]

    for num in range(low,high):
        if arr[num]<=pivot:
            pivot_idx+=1
            arr[pivot_idx],arr[num]=arr[num],arr[pivot_idx]
    arr[pivot_idx+1],arr[high]=arr[high],arr[pivot_idx+1] 

    return pivot_idx+1


sorted_arr = quickSort(arr,0,high)

output_file.write(f'{sorted_arr}')

input_file.close()
output_file.close()