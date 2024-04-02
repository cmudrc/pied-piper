from load import infrastructure
from info import proximity_radius, search_radius


infrastructure.bake(
    save=True,
    report=True,
    proximity_radius=proximity_radius,
    search_radius=search_radius
)


if __name__ == "__main__":
    infrastructure.show_stat()