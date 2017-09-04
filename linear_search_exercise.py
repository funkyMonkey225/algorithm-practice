# Implement the lineaer search algorithm.
# Return the index of the target value.
#
# Helpful Resources
# https://www.youtube.com/watch?v=CX2CYIJLwfg
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html
#

def linear_search(array, target):
    for i in range(0, len(array)):
        if target == array[i]: 
            return i
        elif i >= (len(array)-1) or array == None:
            return -1
       


def linear_search_recursive(array, target, i=0):
    if i >= (len(array)) or array == None:
        return -1
    elif target == array[i]:
        return i
    
    return linear_search_recursive(array, target, i + 1)

data = [
    [[], 5],
    [[1, 3, 5, 7, 10], 5],
    [range(0, 20, 3), 19],
    [range(0, 20, 2), 18],
    [[1, 2, 3], 10]
]

for d in data:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = linear_search_recursive(d[0], d[1])
    print(" Index: " + str(index_of_target))
