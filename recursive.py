def example_one(number):
    if number >= 10:
        return
    print(number)
    example_one(number + 1)

# example_one(0)

def countdown(number):
    if number < 0:
        return
    print(number)
    countdown(number - 1)

# countdown(10)


def fibonacci(number, x, j):
    if number == 0:
        return
    print(x)
    fibnum = x + j
    fibonacci(number - 1, j, fibnum)

# fibonacci(10, 0, 1)


def startriangle(n, counter=1):
    if n == 0:
        return
    print(counter * "*")
    startriangle(n-1, counter + 1)

# startriangle(5)

# call function with optional parameter if you set default def foo(x=5)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
    

# print(factorial(6))

def reversearray(array, i=0):
    if i >= (len(array) / 2) or array == None:
        return array

    j = len(array) - 1 - i
    array[i], array[j] = array[j], array[i] 
    return reversearray(array, i + 1)


input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]

# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = reversearray(array)
#     print("Output: " + str(sorted_array))

def bubble_sort(array, i=0, swap=0):
    if swap==1 or array == None:
        return array
    swap = 1
    if i < (len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swap = 0

    return bubble_sort(array, i + 1, 0)

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = bubble_sort(array)
    print("Output: " + str(sorted_array))

input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]
