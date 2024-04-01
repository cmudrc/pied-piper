import os
import csv


def save(points: list, path: str, name: str = 'homes', format: str = 'csv'):
    filename = name + '.' + format
    filepath = os.path.join(path, filename)
    with open(filepath, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for point in points:
            writer.writerow(point)


if __name__ == "__main__":

    from piperabm.tools.coordinate.projection import xy_latlong

    from piperabm.data.utqiavik.info import location, homes_num
    from piperabm.data.utqiavik.homes.generated_data.generate import generate_homes

    latitude_0 = location['latitude']
    longitude_0 = location['longitude']

    points = generate_homes(
        homes_num=homes_num,
        latitude_0=latitude_0,
        longitude_0=longitude_0
    )

    locations = []
    for point in points:
        latitude, longitude = xy_latlong(
            latitude_0=latitude_0,
            longitude_0=longitude_0,
            x=point[0],
            y=point[1]
        )
        location = [latitude, longitude]
        locations.append(location)
    
    path = os.path.dirname(os.path.realpath(__file__))
    save(locations, path)