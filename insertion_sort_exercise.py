# Implement the insertion sort algorithm.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=DFG-XuyPYUQ
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
#

import datetime

# exponential complexity
def insertion_sort(my_array):
    
    for i in range(1, len(my_array)):
        temp = my_array[i]
        j=i
        while (j > 0 and my_array[j] < my_array[j-1]):
            my_array[j] = my_array[j-1]
            my_array[j-1] = temp
            j = j-1

    return my_array

input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2],
    ["ham", "cheese", "string", "heavy", "toast"]
]

# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = insertion_sort(array)
#     print("Output: " + str(sorted_array))


# Reverse an array -- linear complexity(only one loop)
def reverse_array(my_array):
    j = len(my_array) - 1
    for i in range(0, len(my_array) /  2):
        my_array[i], my_array[j] = my_array[j], my_array[i]
        j = j - 1

    return my_array

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = reverse_array(array)
    print("Output: " + str(sorted_array))


# range(0, 6)
# [0, 1, 2, 3, 4, 5]
# >>> range(1,6)
# [1, 2, 3, 4, 5]
# >>> range(0,7, 2)
# [0, 2, 4, 6]
# >>> range(1000, 5000, 1000)
# [1000, 2000, 3000, 4000]
# >>> range(4000, 0, -1000)
# [4000, 3000, 2000, 1000]

# >>> range(12, -9, -3)
# [12, 9, 6, 3, 0, -3, -6]

# >>> range(10, 2, -3)
# [10, 7, 4]

