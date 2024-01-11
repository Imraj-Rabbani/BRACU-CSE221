input_file = open("input1b.txt","r")
output_file = open("output1b.txt","w")

num = int(input_file.readline())

for i in range(num):
    var = input_file.readline()
    words = var.split(" ")
    first_num = int(words[1])
    operator = words[2]
    second_num = int(words[3])
    if operator == "+":
        output_file.write(f"The result of {first_num} + {second_num} is {first_num+second_num}\n")
    elif operator == "-":
        output_file.write(f"The result of {first_num} - {second_num} is {first_num-second_num}\n")
    elif operator == "*":
        output_file.write(f"The result of {first_num} * {second_num} is {first_num*second_num}\n")
    else:
        output_file.write(f"The result of {first_num} / {second_num} is {first_num/second_num}\n")


input_file.close()
output_file.close()