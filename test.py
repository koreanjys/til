from itertools import combinations

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b = list(combinations(a, 3))
c = list(filter(lambda num: sum(num) == 20, b))
print(c)