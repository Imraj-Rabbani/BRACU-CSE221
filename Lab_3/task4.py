input_file = open("input4.txt","r")
output_file = open("output4.txt","w")
num = int(input_file.readline())

arr = list(map(int,input_file.readline().split(" ")))

def merge(a, b):
    global li
    arr1 = a
    arr2 = b
    arr2_new = []
    for i in arr2 :
      arr2_new.append(abs(i))
    x = max(arr1)
    y = max(arr2_new)
    cal = x+y**2
    li.append(cal)
    arr = a+b
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        a = merge(a1, a2)
        return a

li = []
a = mergeSort(arr)
max_value = max(li)
output_file.write(f"{max_value}")

#Had to copy this task's code from someone else :P