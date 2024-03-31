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

    from piperabm.data.utqiavik.info import location, homes_num
    from piperabm.data.utqiavik.homes.generated_data.generate import generate_homes

    points = generate_homes(
        homes_num=homes_num,
        latitude_0=location['latitude'],
        longitude_0=location['longitude']
    )
    path = os.path.dirname(os.path.realpath(__file__))
    save(points, path)