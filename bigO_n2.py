
'''
<> Big O: O(n^2)
In this task, you are required to implement a function called print_items(n).

This function takes one integer argument, n, and prints out a pair of numbers (i, j) for every possible combination of i and j in the range of 0 up to but not including n.

Each pair (i, j) is printed on a new line. i and j iterate over the range independently, so every combination of i and j in the range should be printed.

The output of the function should be a series of pairs, printed one after the other, each on a new line. The pairs should be printed in the order that they are generated by the nested loops.

Here's an example output for print_items(3):

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
The pairs are generated by the nested loops, with i taking on every value from 0 to n - 1 in the outer loop, and j taking on every value from 0 to n - 1 in the inner loop for each value of i.

Remember, the goal of this function is to print all the pairs (i, j) where i and j are in the range of 0 up to n - 1.
'''

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
print_items(10)