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
import timeit
import time
import exhaustive
import dynamic

def exhaustive_time():
    """ 
    function to measure execution time of exhaustive search approach using the 
    timeit built-in python library
    """
    SETUP_CODE = '''
import exhaustive '''
    TEST_CODE = '''
max = 10
items = [[1, 2], [3, 3], [5, 6], [6, 7]]
exhaustive.stock_maximization(max, items)'''

    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10000)
    # print time
    print('Exhaustive Search Approach Time: {}'.format(min(times))) 

def dynamic_time():
    """ 
    function to measure execution time of dynamic programming approach using the 
    timeit built-in python library
    """
    SETUP_CODE = '''
import dynamic '''
    TEST_CODE = '''
max = 10
items = [[1, 2], [3, 3], [5, 6], [6, 7]]
dynamic.stock_maximization(max, items)'''

    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10000)
    # print time
    print('Dynamic Programming Approach Time: {}'.format(min(times))) 

def main():
    # check for file input argument
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:   
            max = float(next(file))     # read max from first line
            items = []
            for line in file:           # read items
                current_item = line.rstrip('\n').split(", ")
                current_item[0] = int(current_item[0])
                current_item[1] = float(current_item[1])
                items.append(list(current_item))
        file.close
    else:
        # default values
        max = 10
        items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    
    print("Total Available:", max)
    print("Items:", items)

    start_time_e = time.time()      # track runtime
    best_indices_e =  list(exhaustive.stock_maximization(max, items))
    time_e = start_time_e - time.time()

    start_time_d = time.time()      # track runtime
    best_indices_d =  dynamic.stock_maximization(max, items)
    time_d = start_time_d - time.time()

    # print results
    print("Exhaustive Approach Result:")
    print("{total:.2f} {best}".format(total = exhaustive.total_value(items, best_indices_e)[1], best = best_indices_e))
    print("Runtime: ", time_e)      # print runtime 

    print("Dynamic Approach Result:")
    print("{total} {best}".format(total = dynamic.total_value(items, best_indices_d), best = best_indices_d))
    print("Runtime: ", time_d)      # print runtime
    print()
    exhaustive_time()
    dynamic_time()

if __name__ == "__main__":
    main()