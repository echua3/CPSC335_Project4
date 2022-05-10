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
import exhaustive

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
    best_indices =  exhaustive.stock_maximization(max, items)
    print("{total:.2f} {best}".format(total = exhaustive.total_value(items, best_indices), best = best_indices))

if __name__ == "__main__":
    main()