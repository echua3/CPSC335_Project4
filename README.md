# CPSC335_Project4
## Project 4: Exhaustive vs. Dynamic Programing 
## Spring 2022 CPSC 335 - Algorithm Engineering 
### Instructor: Dr. Sampson Akwafuo

### Epiphany Chua echua@csu.fullerton.edu

[Github Repo link](https://github.com/echua3/CPSC335_Project4 "CPSC 335 Project 4 git repository")

Includes **Part A: The Exhaustive Search Approach** and **Part B: The Dynamic Programming Approach**
### Part A: The Exhaustive Search Approach
The script **exhaustive.py** accepts a txt document as input and prints the
indices of the subset of items with the highest value that is still under the 
available fund limit.

The txt document must be in the format depicted below.
```
# test1.txt
10
1, 2
3, 3
5, 6
6, 7
```
running `python3 exhaustive.py test1.txt`
```
Total Available: 10.0
Items: [[1, 2.0], [3, 3.0], [5, 6.0], [6, 7.0]]
10.00 (1, 3)
```

If no document is passed, running `python3 exhaustive.py` will print the 
resulting lists from the given input found in the assignment and test1.txt.

### Part B: The Dynamic Programming Approach
The script **dynamic.py** accepts a txt document as input and prints the
indices of the subset of items with the highest value that is still under the 
available fund limit.
The txt document must be in the format depicted below, which is the same as Part A; however, dynamic.py does not take floats as inputs.
```
# test1.txt
10
1, 2
3, 3
5, 6
6, 7
```
running `python3 dynamic.py test1.txt`
```
Total Available: 10
Items: [[1, 2], [3, 3], [5, 6], [6, 7]]
10.00 [1, 3]
```
If no document is passed, running `python3 dynamic.py` will print the 
resulting lists from the given input found in the assignment and test1.txt.

### Project 4
The script **project4.py** accepts one txt document as input. It runs both exhaustive.py and dynamic.py.