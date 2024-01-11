input_file = open("input1a.txt","r")
output_file = open("output1a.txt","w")


num = int(input_file.readline())

for i in range(num):
    value = int(input_file.readline())
    if value%2==0:
        output_file.write(f"{value} is an Even number.\n")
    else:
        output_file.write(f"{value} is a Odd number.\n")


input_file.close()
output_file.close()
