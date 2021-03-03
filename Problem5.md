Given the created and deleted dates for a server, create a program that calculates the cost. The fee structure is as follows:

If the server is deleted on the same day it is created, there is a fixed cost of 20.   
If the server is deleted after a day but still within a month cost = 30 * (the number of days).    
If the server is deleted after a month but still within a year, the cost = 1000 * (the number of months).    
If the server is deleted after a year in which it was created, there is a fixed cost of 20000.    

Function Description

Complete the server_cost function in the file. It must return an integer representing the cost.

server_cost has the following parameter(s):

d1, m1, y1: created date day, month and year
d2, m2, y2: deleted date day, month and year

Output Format

Print a single integer denoting the cost for the server as input.


Sample Input

6 6 2020     
9 6 2020

Sample Output

90
