from piperabm.matter import Matter


matter = Matter(
    name='food',
    amount=80,
    max=100,
)


if __name__ == '__main__':
    matter.print