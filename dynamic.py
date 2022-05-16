# dynamic.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# May 9, 2022

# Project 4: Exhaustive vs. Dynamic Programing
# Part B: The Dynamic Programming Approach
import sys
import math

def first_valid(iterable, default=False, pred=lambda x: x is not None):
    """
    Returns the first non None value in the iterable (list).
    Function based on first_true recipe in the itertools documentation

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item for which pred(item) is true.
    """
    return next(filter(pred, iterable), default)

def total_stocks(items: list, indices: list) -> int:
    """
    Function that calculates the total number of stocks given in items with
    the indices listed in indices.

        parameters -
            items (list): list of lists [x = number of stocks, y = value]
            indices (list): list of indices in items

        return -
            total (int): total value of all the x inputs in list
    """
    total = 0
    for i in indices:
        total += items[i][0]
    return total

def total_value(items: list, indices: list) -> int:
    """
    Function that calculates the total value of the stocks given in items with
    the indices listed in indices.

        parameters -
            items (list): list of lists [x = number of stocks, y = value]
            indices (list): list of indices in items

        return -
            total (float): total value of all the y inputs in list
    """
    total = 0
    for i in indices:
        total += items[i][1]
    return total

def stock_maximization(M: int, items: list) -> list:
    """  
    This function uses top-down dynamic programming to handle the overlapping
    subproblems. A two-dimensional array is used to store the results of all
    the solved sub-problems.
    
    parameters - 
        M (int): total available investment sum
        items (list): list of lists [x = number of stocks, y = value]
    
    return -
        best (list): subset of items with the highest value within given limit
    """
    result = [None] * (M + 1)
    result[0] = list()
    # print(result)
    for value in range(1, M+1):
        for i, item in enumerate(items):
            _, y = item
            # print("current item: ", item)
            # print("current result: ", result)
            if value >= y and result[value - y] is not None and (i not in 
                result[value - y]):
                candidate = [i] + result[value - y]
                # print("candidate:", candidate)
                if result[value] is None or (total_stocks(items, candidate) > 
                    total_stocks(items, result[value])):
                    # print("update result: ", candidate)
                    result[value] = candidate
    # print("Result: ", result)
    return first_valid(result[::-1])


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
    best_indices =  stock_maximization(max, items)
    print("{total:.2f} {best}".format(total = total_value(items, best_indices),
        best = best_indices))

if __name__ == "__main__":
    main()