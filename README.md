![Screenshot 2023-07-25 032842](https://github.com/Churreesha/CFG-Coding-Challenge/assets/104545210/aafbc957-bac3-4b50-9b28-d5db93b6b10b)
# CFG-Coding-Challenge
SOLVE A SERIES OF CODING CONUNDRUMS USING FLOWCHARTS AND PSEUDOCODE 

The Challenge

Each group will be presented with 5 coding problems. There will be 3 core problems and 2 additional problems. Students in teams will submit responses to 2 out of 5 questions for this challenge of their choosing. You can attempt more than 2 if time permits and will be getting additional points or doing so.

**I decided to work independently and solve all 3 core problems as well as the 2 additional problems.**

The challenges were: 

**1) (Core Problem) Should we round up the final grade?**
   
Every subject is graded from 0 to 100%. Less than 40% is failing grade and more than 80% is a distinction. 
We can round up a grade:
If the difference between the  grade and the next multiple of 5  is less than 3, round  up to the next multiple of 5.
If the value of  is less than 40, no rounding occurs as the result will still be a failing grade.

Given a input grade, round it up if appropriate and tell us if the student passed, failed or received a distinction.  Write a algorithm and produce a flow chart.

**2) (Core Problem) Sorting an array.**

You have an array of maximum size of 100 with DISTINCT integers. Write a algorithm and produce a flow chart that sorts this array from smallest to largest. 

EXAMPLE:

[1, 4, 5, 66, 3, 84, 11, 198] 

SORTED:

[1, 3, 4, 5, 11, 66, 84, 198]

**3) (Core Problem) Search a number in a sorted matrix.**

You are given a matrix (a list of lists) of DISTINCT integers and a target number. Each row in the matrix is SORTED and each column in the matrix is SORTED. Our matrix does not necessarily have the same height and width.

Write a pseudocode and produce a flowchart that:
Finds the number and report back its location (row and column indices of the target integer), if it is contained in the matrix
otherwise report back that the integer is not in the matrix.

EXAMPLE matrix:

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

EXAMPLE result:

result = [3,3]

**4) (Additional Problem) Find factorial of n.**

What are factorials: https://en.wikipedia.org/wiki/Factorial

The value of n will be small, less than 100. How could we use a lookup table to find the factorial not in the table already. If you would run the program, the first time the look up table would be empty. 

Produce a pseudo code and a flowchart that allows us to find a factorial of a integer n. 

EXAMPLE: 

Factorial of 1 is 1! = 1.

Factorial of 2 is 2! = 1 * 2 = 2.

Factorial of 3 is 3!= 1 * 2 * 3 = 3 * 2! = 6

Factorial of 4 is 4!= 1 * 2 * 3 * 4 = 4 * 3! =  4 * 6

This gives us a general formula to find factorial: n! = n * (n-1)!


**5) (Additional Problem) Hide the credit card digits.**


There are 16 digits on a credit card. Every 4 digits are separated by a space. Start by generating a random credit card number. 

For security reasons, you are going to hide the first 12 digits on the credit card.

Example:

Randomly generated credit card number: 5486 3251 6584 7855

After hiding the first 12 digits, it would be: XXXX XXXX XXXX 7855


Produce a pseudo code and a flowchart. 


