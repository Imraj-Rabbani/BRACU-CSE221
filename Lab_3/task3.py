input_file = open("input3.txt","r")
output_file = open("output3.txt","w")

num = int(input_file.readline())

array = list(map(int,input_file.readline().split(" ")))


def mergesort(arr,count):
    if len(arr)==1:
        return (arr,count)
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    a = mergesort(left,count)#a=([],int)
    b = mergesort(right,count)
    count = a[1]+b[1]
    return merge(a[0],b[0],count)

'''
Receives two list that are sorted. While merging we can keep a count how many elements
in the right/b list is smaller than that element in the left/a list. 
'''
def merge(a,b,count):
    i = 0
    j = 0
    sorted_arr = []

    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            sorted_arr.append(a[i])
            i+=1
        else:
            sorted_arr.append(b[j])
            count += (len(a)-i)
            j+=1


    if i==len(a):
        sorted_arr += b[j:]
    else:
        sorted_arr += a[i:]
    return(sorted_arr,count)
    #recursively send merged list and a count

result = mergesort(array,0)

output_file.write(f"{result[1]}")

input_file.close()
output_file.close()
