def total_num_fun(index_num, int_list):
    """The function takes in 2 arguments(list and the
    required index number until and including the point
    we need to add up the numbers) and adds up the values on the indexes until
    we reach a negative index_num. Change index_num to set the index"""

    # Return the number if index num reached a negative value
    if index_num < 0:
        return 0
    # Adds up the values on the indexes,
    # the index of the list is decreasing by 1.
    else:
        return int_list[index_num] + total_num_fun(index_num - 1, int_list)


# The list
int_list = [10, 20, 30, 40, 50, 60, 70]
# The index number(integer)
index_num = 4
# Calling the function and store in a variable
total = total_num_fun(index_num, int_list)
# Print the result
print("Total of the list added up until the index point ", total)
