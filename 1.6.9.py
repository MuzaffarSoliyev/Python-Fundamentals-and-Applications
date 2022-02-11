class LoggableList(list, Loggable):
    def append(self, elem) -> None:
        super().append(elem)
        self.log(elem)


if __name__ == '__main__':
    a = LoggableList()
    a.append('msg 1')
    a.append('msg 2')
    print(a)