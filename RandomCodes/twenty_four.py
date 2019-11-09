number_input = input("Enter 4 integers: ")
integer_list = number_input.split(" ")

def multiple(integer_list):
    multiple_0_1 = int(integer_list[0]) * int(integer_list[1])
    multiple_0_2 = int(integer_list[0]) * int(integer_list[2])
    multiple_0_3 = int(integer_list[0]) * int(integer_list[3])
    multiple_1_2 = int(integer_list[1]) * int(integer_list[2])
    multiple_1_3 = int(integer_list[1]) * int(integer_list[3])
    multiple_2_1 = int(integer_list[2]) * int(integer_list[1])
    mult = [multiple_0_1, multiple_0_2, multiple_0_3, multiple_1_2, multiple_1_3, multiple_2_1]
    return mult

def divide(integer_list):
    divide_0_1 = int(integer_list[0]) / int(integer_list[1])
    divide_0_2 = int(integer_list[0]) / int(integer_list[2])
    divide_0_3 = int(integer_list[0]) / int(integer_list[3])
    divide_1_2 = int(integer_list[1]) / int(integer_list[2])
    divide_1_3 = int(integer_list[1]) / int(integer_list[3])
    divide_2_1 = int(integer_list[2]) / int(integer_list[1])
    divi = [divide_0_1, divide_0_2, divide_0_3, divide_1_2, divide_1_3, divide_2_1]
    return divi

def plus(integer_list):
    plus_0_1 = int(integer_list[0]) + int(integer_list[1])
    plus_0_2 = int(integer_list[0]) + int(integer_list[2])
    plus_0_3 = int(integer_list[0]) + int(integer_list[3])
    plus_1_2 = int(integer_list[1]) + int(integer_list[2])
    plus_1_3 = int(integer_list[1]) + int(integer_list[3])
    plus_2_1 = int(integer_list[2]) + int(integer_list[1])
    add = [plus_0_1, plus_0_2, plus_0_3, plus_1_2, plus_1_3, plus_2_1]
    return add

def subtract(integer_list):
    subtract_0_1 = int(integer_list[0]) - int(integer_list[1])
    subtract_0_2 = int(integer_list[0]) - int(integer_list[2])
    subtract_0_3 = int(integer_list[0]) - int(integer_list[3])
    subtract_1_2 = int(integer_list[1]) - int(integer_list[2])
    subtract_1_3 = int(integer_list[1]) - int(integer_list[3])
    subtract_2_1 = int(integer_list[2]) - int(integer_list[1])
    sub = [subtract_0_1, subtract_0_2, subtract_0_3, subtract_1_2, subtract_1_3, subtract_2_1]
    return sub

def overall(mult, divi, add, sub):
    mult = multiple(integer_list)
    divi = divide(integer_list)
    add = plus(integer_list)
    sub = subtract(integer_list)
    return [mult,divi,add, sub]

print(overall(integer_list, integer_list, integer_list, integer_list))