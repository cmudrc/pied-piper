import os
import csv

#path: str, 
def load(name: str = 'homes', format: str = 'csv'):
    path = os.path.dirname(os.path.realpath(__file__))
    filename = name + '.' + format
    filepath = os.path.join(path, filename)
    points = []
    with open(filepath, 'r', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:
            points.append([float(row[0]), float(row[1])])
    return points


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    points = load()

    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    plt.scatter(xs, ys)  # Plot points
    plt.show()