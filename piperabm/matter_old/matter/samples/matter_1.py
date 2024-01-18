from piperabm.matter import Matter


matter = Matter(
    name='water',
    amount=40,
    max=100,
)


if __name__ == '__main__':
    matter.print