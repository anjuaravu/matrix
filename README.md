# task

Consider a Matrix with an N x M grid which consists of alphanumeric characters, spaces and special characters (!,@,#,$,%,&).

The objective of the task is to read each column of the matrix and select only the alphanumeric characters and connect them.
The Matrix should be read from top to bottom and from the leftmost column.

While reading the script, if you encounter a special character or more than one space between two alphanumeric characters, it
should be replaced by a single space. 

The N & M will be inputs received from the user and the content of the Matrix. You can find the code to get inputs from the
the user below and only write code for the above-mentioned functionality

```
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
```


Please find the sample input below

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!


Please find the expected output for the above input below:

This is Matrix#  %!


Explanation:

* When the above Matrix is read, we will get the below value

This$#is% Matrix#  %!

* We get the expected output by replacing the special symbols and spaces between two alphanumeric characters with a single space.
