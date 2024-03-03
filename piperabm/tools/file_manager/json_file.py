import json
import os


class JsonFile:

    def __init__(self, path, filename: str, format: str = "json"):
        self.file = JsonFile._create_file_str(filename, format)
        self.file_temp = JsonFile._create_file_str(filename + "_" + "temp", format)
        self.filepath = os.path.join(path, self.file)
        self.filepath_temp = os.path.join(path, self.file_temp)

    def _create_file_str(filename: str, format: str):
        """
        Create a string for file name by attaching format
        """
        return filename + "." + format
    
    def save(self, data):
        """
        Save the data to file as json using atomic file writing
        """
        # Write data to the temporary file, overwriting if it already exists
        with open(self.filepath_temp, "w") as f:
            json.dump(data, f)

        # Remove the main file if it exists to prevent errors on renaming
        if self.exists():
            self.remove()

        # Rename the temporary file to the main file"s name
        os.rename(self.filepath_temp, self.filepath)

    def load(self):
        """
        Load the data from a file as json
        """
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = None
            print(f"The file {filename} was not found.")
        return data
    
    def exists(self):
        """
        Check if the file already exists
        """
        return os.path.exists(self.filepath)

    def append(self, entry):
        """
        Add new entry to save file
        """
        data = self.load()
        if isinstance(data, list):
            data.append(entry)
        else:
            print("Data is not list.")
            raise ValueError
        self.save(data)

    def remove(self):
        """
        Remove file if exists
        """
        if self.exists():
            os.remove(self.filepath)


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    filename = "sample"
    file = JsonFile(path, filename)
    #print(file.exists())
    data = []
    file.save(data)
    #print(file.exists())
    #data = file.load()
    #print(data)

    entry = {"a": 1}
    file.append(entry)
    data = file.load()
    print(data)
    file.remove()
    