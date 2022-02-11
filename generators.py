from random import random
import itertools


def generators(k):
    for i in range(k):
        yield random()


print(list(itertools.takewhile(lambda x : x <= 31, generators())))