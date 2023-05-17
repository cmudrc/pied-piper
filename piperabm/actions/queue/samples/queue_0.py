from copy import deepcopy

from piperabm.actions import Queue
from piperabm.actions.move.samples import move_0


queue = Queue()
queue.add(deepcopy(move_0))


if __name__ == "__main__":
    queue.print()
    