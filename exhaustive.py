# exhaustive.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# May 9, 2022

# Project 4: Exhaustive vs. Dynamic Programing
# Part A: The Exhaustive Search Approach
import sys
import itertools

def stock_combinations(items: list) -> list:
    """ 
    Function to get the powerset of a set(list), returned as a list.
    Utilizes the itertools python module to create iterators
        parameters -
            items (list): an iterable variable, or list
        return -
            powerset (list): a list with all possible combinations of items
    """
    s = list(items)
    return itertools.chain.from_iterable(itertools.combinations(s, r) 
        for r in range(len(s)+1))

def total_value(items: list, indices: list) -> float:
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

def verify_combination(M: float, items: list, candidate: list) -> bool:
    """
    checks if the candidate total value is less than or equal to the maximum
    value M
        parameters -
            M (float): total available investment sum
            items (list): list of lists [x = number of stocks, y = value]
            candidate (list): list of indices of values in items

        return -
            valid (bool): true if total number is less than or equal to M, false
            otherwise
    """
    return (total_value(items, candidate) <= M)
         

def stock_maximization(M: float, items: list) -> list:
    """  
    This function evaluates the number of stocks and value of all possible
    subsets, then selects the subset with the highest value that is still
    under the available fund limit. It recomputes combination at each state.
    
        parameters - 
            M (float): total available investment sum
            items (list): list of lists [x = number of stocks, y = value]
        
        return -
            best (list): subset of items with the highest value within given 
            limit
    """
    best = None
    for candidate in stock_combinations(range(len(items))):
        if verify_combination(M, items, candidate):
            if best == None or total_value(items, candidate) > total_value(items, best):
                best = candidate
    return best


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
    best_indices =  stock_maximization(max, items)
    print("{total:.2f} {best}".format(total = total_value(items, best_indices), best = best_indices))

if __name__ == "__main__":
    main()