# Implement the binary search.
# Return the index of the target number.
#
# Helpful Resources
# https://www.youtube.com/watch?v=D5SrAga1pno
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
#

def binary_search(array, target):
    mid = len(array) / 2
    left = 0
    right = (len(array) - 1)
    while left <= right:
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
            mid = (left + (right - left) / 2)
        elif target < array[mid]:
            right = mid - 1
            mid = (left + (right - left) / 2)

    return -1

def binary_search_recursive(array, target, left, right):

    if right == None:
        right = len(array) -1

    if left > right:
        return -1

    mid = left + (right - left) / 2
    value = array[mid]

    if value == target:
        return mid
    elif value > target:
        right = mid - 1
    elif value < target:
        left = mid + 1

    return binary_search_recursion(array, target, left, right)

data = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8],
]

# for d in data:
#     print("")
#     print(" Array: " + str(d[0]))
#     print("Target: " + str(d[1]))
#     index_of_target = binary_search(d[0], d[1])
#     print(" Index: " + str(index_of_target))



#  Rotated Array
#  Loop through array
#  Find where array decreases instead of increasing, return this index
#  If target greater than number at this index, begin linear search to left, otherwise search to right


def rotated_search(array, target):
    for i in range(len(array)):
        temp = 0
        if target == array[i]: 
            return i
        elif array[i] > array[i + 1]:
            if target > array[i + 1]:
                left = i + 1
                right = len(array)
                mid = left + (right - left) / 2
                while left <= right:
                    if target == array[mid]:
                        return mid
                    elif target > array[mid]:
                        left = mid + 1
                        mid = (left + (right - left) / 2)
                    elif target < array[mid]:
                        right = mid - 1
                        mid = (left + (right - left) / 2)
                return -1 

            elif target < array[i + 1]:
                left = 0
                right = i
                mid = left + (right - left) / 2
                while left <= right:
                    if target == array[mid]:
                        return mid
                    elif target > array[mid]:
                        left = mid + 1
                        mid = (left + (right - left) / 2)
                    elif target < array[mid]:
                        right = mid - 1
                        mid = (left + (right - left) / 2)
                return -1
    return -1

dataz = [
    [[5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 0],
    [[9, 10, 1, 2, 3, 4, 5, 6, 7, 8], 3],
    [[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 2],
    [[7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 8],
]

for d in dataz:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = rotated_search(d[0], d[1])
    print(" Index: " + str(index_of_target))


