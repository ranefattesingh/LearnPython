
matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
]

print(matrix)

matrix = [[row[i] for row in matrix] for i in range(3)]
print(matrix)

transpose = []
for i in range(3):
    transpose.append([row[i] for row in matrix])
print(transpose)
transpose = list(zip(*matrix))
print(transpose)

del transpose[0]
print(transpose)

print(len(transpose))