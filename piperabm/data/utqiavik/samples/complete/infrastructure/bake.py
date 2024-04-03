from load import infrastructure
from info import proximity_radius, search_radius
from piperabm.time import Date


start = Date.today()
infrastructure.bake(
    save=True,
    report=False,
    proximity_radius=proximity_radius,
    search_radius=search_radius
)
end = Date.today()


if __name__ == "__main__":
    print(end - start)
    infrastructure.show_stat()