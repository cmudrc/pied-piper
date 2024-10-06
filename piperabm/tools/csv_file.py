import csv
import os


class CsvFile:
    """
    Json file handling
    """

    def exists(self):
        """
        Check if the file already exists
        """
        return os.path.exists(self.filepath)
    


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    filename = "sample"
    file = CsvFile(path, filename)

    data = []
    file.save(data)

    entry = {"a": 1}
    file.append(entry)

    data = file.load()
    print("Test: ", data == [{"a": 1}])

    file.remove()