import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix))
string = str()
for i in matrix:
    for j in i:
        sample += j
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', string))

