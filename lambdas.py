import functools
import operator

x = [
    (1, 2),
    (2, 3),
    (2, 2)
]

x.sort(key=operator.itemgetter(1))

print(x)
