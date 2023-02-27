from log import Log


class First:

    log = Log()

    def do(self):
        self.log.add('from first')


if __name__ == "__main__":
    s = First()
    s.do()