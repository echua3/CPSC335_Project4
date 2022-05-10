# exhaustive.py
# Epiphany Chua
# echua@csu.fullerton.edu
# Spring 2022 CPSC 335 (2)
# Instructor: Dr. Sampson Akwafuo
# May 9, 2022

# Project 4: Exhaustive vs. Dynamic Programing
# Part A: The Exhaustive Search Approach
import sys

def main():
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
        items = [[1, 2], [3, 3], [5, 6], [6, 7]]
        max = 10


if __name__ == "__main__":
    main()