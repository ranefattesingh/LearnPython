l1 = [1, 2, 3, 4]
print (l1)
l1.append(5)    # appends only single element
print(l1)
print(l1[1:4])
print(l1[-4: -1])
e = l1.pop()        #inplace remove and return removed element
print(e)
print(l1)

l2 = [ 6, 7, 8, 9, 10]
l3 = [11, 12, 13, 14]
print(l1 + l2 + l3)
l1.extend(l2)
print(l1)

l1.sort(reverse=True)
print(l1)

l1.reverse()    #No args
print(l1)

l3 = l1.copy()
print(l3)

l3[2], l3[3], l3[4] = l3[4], l3[2], l3[3]
print(l3)