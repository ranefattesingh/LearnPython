squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = list(map(lambda x: x**2, [10, 20, 30, 40, 50]))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# filter out elements which are not common in both lists
comb = []
l1 = [1, 2, 3, 4]
l2 = [3, 1, 4]
for x in l1:
    for y in l2:
        if x != y:
            comb.append((x, y))
print(comb)

comb = [(x, y) for x in l1 for y in l2 if x != y]
print(comb)
