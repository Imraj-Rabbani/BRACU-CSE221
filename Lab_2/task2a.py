input_file = open("input2a.txt","r")
output_file = open("output2a.txt","w")

size1 = int(input_file.readline())
arr1 = list(map(int,input_file.readline().split(" ")))
size2 = int(input_file.readline())
arr2 = list(map(int,input_file.readline().split(" ")))

new_arr = arr1 + arr2
sorted_arr = sorted(new_arr)
for item in sorted_arr:
    output_file.write(f"{item} ")

input_file.close()
output_file.close()