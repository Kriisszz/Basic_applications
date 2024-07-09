def largest_num_fun(numbers_list):
    """This function takes in a list of integer as a parameter,
    and checks which one is the largest number of the list"""
    # When the length of the list is 1 the function returns the largest number
    if len(numbers_list) == 1:
        return numbers_list[0]
    # Using the built in function "max" it finds the largest
    # number and slice the list.
    else:
        return max(numbers_list[0], largest_num_fun(numbers_list[1:]))


# The list.
numbers_list = [72, 23, 45, 9, 3, 31, 123]
# Calling the function and saving it into a variable.
largest_num = largest_num_fun(numbers_list)
# Printing the largest number.
print("The largest number is: ", largest_num)
