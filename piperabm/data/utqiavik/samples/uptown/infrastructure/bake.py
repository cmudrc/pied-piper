from load import infrastructure
from info import proximity_radius, search_radius


infrastructure.bake(
    save=True,
    report=False,
    proximity_radius=proximity_radius,
    search_radius=search_radius
)


if __name__ == "__main__":
    print(infrastructure.baked_streets, infrastructure.baked_neighborhood)
    infrastructure.show_stat()