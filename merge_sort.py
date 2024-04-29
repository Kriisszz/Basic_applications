# Function to merge the 3 lists
def merge_sort_three(string_list1, string_list2, string_list3):
    merged_list = string_list1 + string_list2 + string_list3
    return merge_sort(merged_list)


# Function to sort the list
def merge_sort(merged_list):
    if len(merged_list) <= 1:
        return merged_list

    # Split the list
    mid = len(merged_list) // 2
    left_half = merged_list[:mid]
    right_half = merged_list[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


string_list1 = ["something", "sometimes", "element", "id", "whatever", "six",
                "appeal", "thumb", "ice", "snow"]
string_list2 = ["someone", "boneless", "creative", "exact", "try", "hexagon",
                "ghost", "impressive", "taken", "beetroot"]
string_list3 = ["timeless", "accurate", "dental", "fixed", "jogging", "peanut",
                "cashew", "banana", "apple", "strawberry"]

sorted_list = merge_sort_three(string_list1, string_list2, string_list3)
print(sorted_list)
