import json
import os


class JsonHandler:

    def create_file_str(filename: str, format: str):
        """
        Create a string for file name by attaching format
        """
        return filename + "." + format
    
    def create_filepath(path, filename: str, format: str):
        """
        Create full file path
        """
        file = JsonHandler.create_file_str(filename, format)
        return os.path.join(path, file)
    
    def save(data, path, filename: str, format: str="json"):
        """
        Save the data to file as json using atomic file writing
        """
        filename_temp = filename + "_" + "temp"
        filepath_main = JsonHandler.create_filepath(path, filename, format)
        filepath_temp = JsonHandler.create_filepath(path, filename_temp, format)

        # Write data to the temporary file, overwriting if it already exists
        with open(filepath_temp, "w") as f:
            json.dump(data, f)

        # Remove the main file if it exists to prevent errors on renaming
        if os.path.exists(filepath_main):
            os.remove(filepath_main)

        # Rename the temporary file to the main file"s name
        os.rename(filepath_temp, filepath_main)

    def load(path, filename: str, format: str="json"):
        """
        Load the data from a file as json
        """
        filepath = os.path.join(path, filename + "." + format)
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = None
            print(f"The file {filename} was not found.")
        return data

    def append(entry, path, filename: str, format: str="json"):
        """
        Add new entry to save file
        """
        data = JsonHandler.load(path, filename, format)
        if isinstance(data, list):
            data.append(entry)
        else:
            print("Data is not list.")
            raise ValueError
        JsonHandler.save(data, path, filename, format)

    def remove(path, filename: str, format: str="json"):
        """
        Remove file if exists
        """
        filepath = os.path.join(path, filename + "." + format)
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == "__main__":
    data = []
    path = os.path.dirname(os.path.realpath(__file__))
    filename = "sample"
    JsonHandler.save(data, path, filename)

    data = JsonHandler.load(path, filename)
    print(data)

    entry = {"a": 1}
    JsonHandler.append(entry, path, filename)
    data = JsonHandler.load(path, filename)
    print(data)
    JsonHandler.remove(path, filename)
    