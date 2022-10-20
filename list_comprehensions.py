import numpy as np


int_arr = np.arange(0, 21, 1)
#print(f"Original array: {int_arr}")

# Do action for each element in the array, template:
# *action* for *iteration element name* in *array name*
add_10_arr = [num+10 for num in int_arr]
#print(f"Original array + 10: {add_10_arr}")

pow_arr = [2**num for num in int_arr]
#print(f"2 with different pow value: {pow_arr}")

# add condition to filter array, template:
# *action* for *iteration element name* in *array name* if *condition*
pow_even_num_arr = [2**num for num in int_arr if num % 2 == 0]
#print(f"2 with different even pow values: {pow_even_num_arr}")

bigger_then_10_arr = [num for num in int_arr if num > 10]
#print(f"only numbers bigger then 10: {bigger_then_10_arr}")

# nesting if statements:
range_arr = [num for num in int_arr if num > 5 and num < 20]
#print(f"range arr: {range_arr}")

# if else action
calculated_arr = [num/2 if num % 2 == 0 else num * 2 for num in int_arr]
#print(f"divide by 2 if even, multiple by 2 if odd : {calculated_arr}")


# nesting for loops, template:
# *action* for *iteration 1 var name* in * first iteration arr* for *sub-for loop iteration 2 var name* in *second iteration arr*
colours = ["red", "green", "blue"]
clothes = ["t-shirt", "shirt"]
combined_options = [
    f"{colour} {clothing}" for colour in colours for clothing in clothes]
# print(combined_options)


# function as action
def multiply_by_two(num):
    return num *2

calculated_arr = [multiply_by_two(num) for num in int_arr]
#print(f"multiplied by two: {calculated_arr}")


#summing file numbers
with open("some_data.txt") as file:
    datasum = 0
    for line in file:
        line_data = line.rstrip().split(",")
        datasum += sum([float(num) for num in line_data])
    print(datasum)
        
        


