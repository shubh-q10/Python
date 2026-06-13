'''
Given an integer n (where n > 0), print a "V" shaped pattern with n rows. The pattern should use backslashes (\) and forward slashes (/) for each row, with the v character at the bottom. There should be no spaces to the right of the pattern.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format

    • A single integer n, representing the number of rows in the pattern.

Output Format

    • A "V" shaped pattern with n rows, as described.

Constraints

    • 1 <= n

Examples

Input:

1
Output:

v
Input:

2
Output:

\ /
 v
Input:

3
Output:

\   /
 \ /
  v

'''
n = int(input())  # user enters number of rows

for i in range(1, n + 1):  # loop from 1 to n
    if i == n:  # if it is the last row
        print(' ' * (i - 1) + 'v')
    else:
        print(' ' * (i - 1) + '\\' + ' ' * (2 * (n - i) - 1) + '/')
