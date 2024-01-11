input_file = open("input2.txt","r")
output_file = open("output2.txt","w")

def find_max(arr):
    if len(arr)==1:
        return arr[0]
    else:
        mid = len(arr)//2
        #divides the array by half until the length list becomes 1
        a1 = find_max(arr[:mid])#a1=int
        a2 = find_max(arr[mid:])#a2=int
        #compares two numbers of the list starting from the left and keeps returning the highest number
        return highest(a1,a2)


#returns the highest number
def highest(x,y):
    if x>=y:
        return x
    else:
        return y

num = input_file.readline()
arr = list(map(int,input_file.readline().split(" ")))

maximum = find_max(arr)

output_file.write(f"{maximum} \nAnd the time complexity is O(logN)")

input_file.close()
output_file.close()