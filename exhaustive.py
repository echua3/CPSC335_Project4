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
            powerset (list): a list wit all possible combinations of items
    """
    s = list(items)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def stock_maximization(M: int, items: list) -> list:
    """  
    This function evaluates the number of stocks and value of all possible
    subsets, then selects the subset with the highest value that is still
    under the available fund limit. It recomputes combination at each state.
    
    parameters - 
        M (int): total available investment sum
        items (list): list of lists [ x = number of stocks, y = value]
    
    return -
        best (list): subset of items with the highest value within given limit

    """
    best = None
    for candidates in stock_combinations(items):
        print(candidates)


def main():
    # check for file input argument
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:   
            max = int(next(file))   # read max from first line
            items = []
            for line in file:       # read items
                current_item = line.rstrip('\n').split(", ")
                items.append(list(map(int, current_item)))
        print("Items:", items)
        print("Max:", max)
        file.close
    else:
        # default values
        max = 10
        items = [[1, 2], [3, 3], [5, 6], [6, 7]]

    stock_maximization(max, items)


if __name__ == "__main__":
    main()