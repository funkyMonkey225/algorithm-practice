# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 50000000.

# 1. Find all multiples of 3 and 5 below 50000000
# 2. Add those numbers to sum
# 3. Loop through until n < MAX

import datetime

def run_program(max):
    # n = 0
    # sum = 0
    # while (n < MAX):
    #     if (n % 3 == 0) or (n % 5 == 0):
    #         sum += n
    #     n += 1

    def sum_multiples(multiple):
        counter = multiple
        total = 0
        while (counter < max):
            counter += multiple
            total += counter
        return total

    total3 = sum_multiples(3)
    total5 = sum_multiples(5)
    total15 = sum_multiples(15)
    sum = total3 + total5 - total15
   

    print("The sum of all the multiples of 3 or 5 below " + str(max) + " is " + str(sum) + ".")

def run_and_measure(max):
    start_time = datetime.datetime.now()
    run_program(max)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("This program ran in " + str(duration))

for i in range(0, 6000, 1000):
    run_and_measure(i)




