from infrastructure import Infrastructure

from core.entity import Entity


class City(Entity):
    def __init__(self, name, pos, resources, infrastructures):
        super().__init__(Entity(
            name=name,
            pos=pos
        ))
    
        self.resources = resources
        self.infrastructures = infrastructures


if __name__ == "__main__":
    from datetime import date

    i = Infrastructure(
        name='sample road',
        type='road',
        start='city_1',
        end='city_2',
        two_sided=True,
        resources={
            'water': 5,
        },
        cost=1000,
        project_start_date=date(2000, 1, 1),
        coeff=0.01,
        degree=2,
        seed=202
    )
