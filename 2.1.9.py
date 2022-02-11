class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x >= 0:
            super().append(x)
        else:
            raise NonPositiveError


if __name__ == '__main__':
    a = PositiveList()
    a.append(1)
    a.append(-1)
    # print(a)