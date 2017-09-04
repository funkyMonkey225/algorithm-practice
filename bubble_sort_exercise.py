# Implement the bubble sort algorithm in the bubble_sort method.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=8Kp-8OGwphY
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
#

def bubble_sort(my_array):
    cont = True
    while (cont):
        cont = False
        for i in range(len(my_array)-1):
            if (my_array[i] > my_array[i+1]):
                swap = my_array[i]
                my_array[i] = my_array[i+1]
                my_array[i+1] = swap
                cont = True

    return my_array

input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = bubble_sort(array)
    print("Output: " + str(sorted_array))
