# Function for linear search
def lin_search_fun(list_array, target):
    for item in range(len(list_array)):
        if list_array[item] == target:
            print("The number you are looking for is at the index of:", item)


# Insertion sort to sort the elements in the list
def insertionSort(list_array):
    n = len(list_array)  # Get the length of the list
    # If the list has 0 or 1 element, it is already sorted, so return
    if n <= 1:
        return
    # Iterate over the list starting from the second element
    for i in range(1, n):
        key = list_array[i]
        j = i-1
        while j >= 0 and key < list_array[j]:
            list_array[j+1] = list_array[j]
            j -= 1
        list_array[j+1] = key


def binary_search(target, list_array):
    low, high = 0, len(list_array) - 1

    # Keep iterating until low and high cross
    # Returns None if item not found
    while high >= low:
        # Find midpoint
        mid = (low + high) // 2

        # If target is found at midpoint, return
        if list_array[mid] == target:
            print(list_array[mid])
            return mid
        # Else, if item at midpoint is less than item,
        # search the second half of the list
        elif list_array[mid] < target:
            low = mid + 1
        # Else, search first half
        else:
            high = mid - 1


# The list of numbers.
list_array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# The number you looking for
target = 9

# I will use a linear search as this is not a sorted list,
# and also linear search looks an easy and simple way to apply.
lin_search_fun(list_array, target)

# Calling the function to sort the array
insertionSort(list_array)

# Calling the binary search function. Usually I would use binary search
# when the list is a long one and also sorted.
binary_search(target, list_array)
