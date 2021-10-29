#same as list, difference is tuples are immutable
t = 12345, 54321, 'hello!'
print(t)
u = t, (1, 2, 3, 4, 5), [1, 2, 3]
print(u)

u[2].append(4)

print(u)

singleton = 'hello',
print(singleton)