
l = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
a = 0
while 0 in l :
    l.remove(0)
    a += 1
while a :
    l.append(0)
    a -= 1
print(l, a)
