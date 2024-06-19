import json
import os


class JsonFile:
    """
    Json file handling
    """

    def __init__(self, path, filename: str, format: str = "json"):
        if path is None:
            print("path is not defined.")
            raise ValueError
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
            print(f"The file {self.file} was not found.")
        data = JsonFile.convert_keys(data)
        return data
    
    def convert_keys(obj):
        """
        Recursively converts string keys to integers if possible in any JSON-like structure 
        which may include dictionaries and lists.
        """
        if isinstance(obj, dict):
            new_obj = {}
            for k, v in obj.items():
                new_key = int(k) if k.isdigit() else k  # Convert key if it's a digit
                new_obj[new_key] = JsonFile.convert_keys(v)  # Recurse into values
            return new_obj
        elif isinstance(obj, list):
            return [JsonFile.convert_keys(item) for item in obj]  # Apply recursively to each item in the list
        else:
            return obj  # Return the item itself if it's neither a dict nor a list
    
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

    data = []
    file.save(data)

    entry = {"a": 1}
    file.append(entry)

    data = file.load()
    print("Test: ", data == [{"a": 1}])

    file.remove()
    