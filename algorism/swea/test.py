a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
i = 0
c = []
while i < len(a):
    c.append((a[i], b[i]))
    i += 1

print(c)