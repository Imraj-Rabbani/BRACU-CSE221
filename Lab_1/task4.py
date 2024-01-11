input_file = open("input4.txt","r")
output_file = open("output4.txt","w")

num = int(input_file.readline())

arr = [0]*num
for i in range(num):
    words = input_file.readline().split(" ")
    arr[i] = [words[0],words[4],words[6]]

def sort(arr):
    #sorting in lexicological order
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j][0]>arr[j+1][0]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    
    #checking if names are same
    for item in range(len(arr)):
        if item==len(arr)-1:
            break
        if arr[item][0]==arr[item+1][0]:
            if arr[item][2]<arr[item+1][2]:
                arr[item],arr[item+1]=arr[item+1],arr[item]

    #writing the sorted list in the output file
    for item in arr:  
        output_file.write(f"{item[0]} will departure for {item[1]} at {item[2]}")

sort(arr)

input_file.close()
output_file.close()