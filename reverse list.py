s = int(input('What is your favorite number?'))
l = []
a = s - 1
a2 = a
b = 0
n = 0

while s >= 1:
    n = n + 100
    l.append(n)
    s = s - 1

print('Original list :', l)

c = l[a - 1]
d = l[a]

while a > a2 / 2:
    l[a] = l[b]
    a = a - 1
    b = b + 1

l[1] = c
l[0] = d
print('Reversed list :', l)
