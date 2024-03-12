from piperabm.data.utqiavik.streets.labels import filter_street_labels
from piperabm.data.utqiavik.settlements.labels import filter_settlement_meshes_labels
from piperabm.data.utqiavik.samples.uptown.info import latitude_min, latitude_max, longitude_min, longitude_max


""" Uptown """
streets_permitted_labels = filter_street_labels(
    latitude_min,
    latitude_max,
    longitude_min,
    longitude_max
)

settlement_meshes_permitted_labels = filter_settlement_meshes_labels(
    latitude_min,
    latitude_max,
    longitude_min,
    longitude_max
)


if __name__ == "__main__":
    print(len(streets_permitted_labels))
    print(len(settlement_meshes_permitted_labels))
