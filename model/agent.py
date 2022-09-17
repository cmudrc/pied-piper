from core.entity import Entity


class Agent(Entity):
    def __init__(self, name, pos, active=True):
        super().__init__(
            name=name,
            pos=pos,
            active=active
        )


if __name__ == "__main__":
    a = Agent(
        name='person_1',
        pos=[0.5, 0.7],
        active=True
    )