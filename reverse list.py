l = [500, 400, 300, 200, 100]
a = 4
b = 0
n = 4

print('Original list: ', l)

c = l[a - 1]
c2 = l[a]

while n >= 2:
    l[a] = l[b]
    a = a - 1
    b = b + 1
    n = n - 1

l[1] = c
l[0] = c2
print('Reversed list: ', l)
