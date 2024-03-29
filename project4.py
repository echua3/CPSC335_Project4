# project4.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# May 9, 2022

# Project 4: Exhaustive vs. Dynamic Programing
# Part A: The Exhaustive Search Approach
# Part B: The Dynamic Programming Approach
import sys
import math
import timeit
import exhaustive
import dynamic

def exhaustive_time(max = 10, items = [[1, 2], [3, 3], [5, 6], [6, 7]]):
    """ 
    function to measure execution time of exhaustive search approach using the 
    timeit built-in python library
    """
    SETUP_CODE = '''
import exhaustive '''
    TEST_CODE = '''
max = {max}
items = {items}
exhaustive.stock_maximization(max, items)'''.format(max = max, items = items)
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
    # print time
    print('Exhaustive Search Approach Time: {}'.format(min(times))) 

def dynamic_time(max = 10, items = [[1, 2], [3, 3], [5, 6], [6, 7]]):
    """ 
    function to measure execution time of dynamic programming approach using the 
    timeit built-in python library
    """
    SETUP_CODE = '''
import dynamic '''
    TEST_CODE = '''
max = {max}
items = {items}
dynamic.stock_maximization(max, items)'''.format(max = max, items = items)
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
    # print time
    print('Dynamic Programming Approach Time: {}'.format(min(times))) 

def main():
    # check for file input argument
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:   
            max = int(math.floor(float(next(file))))  # read max from first line
            items = []
            for line in file:           # read items
                current_item = line.rstrip('\n').split(", ")
                current_item[0] = int(current_item[0])
                current_item[1] = math.floor(float(current_item[1]))
                items.append(list(current_item))
        file.close
    else:
        # default values
        max = 10
        items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    
    print("Total Available:", max)
    print("Items:", items)

    best_indices_e =  list(exhaustive.stock_maximization(max, items))
    best_indices_d =  dynamic.stock_maximization(max, items)

    # print results
    print()
    print("Exhaustive Approach Result:")
    print("{total:.2f} {best}".format(total = exhaustive.total_value(items,
        best_indices_e)[1], best = best_indices_e))

    print("Dynamic Approach Result:")
    print("{total} {best}".format(total = dynamic.total_value(items,
        best_indices_d), best = best_indices_d))
    print()

    # print execution times
    exhaustive_time(max, items)
    dynamic_time(max, items)

if __name__ == "__main__":
    main()