a = [1, 2, 3, 4, 5, 6, 7, 8]
b = map(lambda x:x+4,a)
print(b)
c = reduce(lambda x, y: x + y, a)
print (c)