import json
import os


class JsonHandler:

    format = "." + "json"
    
    def save(data, path, filename: str = "sample"):
        file = filename + JsonHandler.format
        filepath = os.path.join(path, file)
        with open(filepath, "w") as f:
            json.dump(data, f)

    def load(path, filename: str = "sample"):
        file = filename + JsonHandler.format
        filepath = os.path.join(path, file)
        with open(filepath, "r") as f:
            data = json.load(f)
        return data

    def append(entry, path, filename: str = "sample"):
        data = JsonHandler.load(path, filename)
        data.append(entry)
        JsonHandler.save(data, path, filename)

    def remove(path, filename: str = "sample"):
        file = filename + JsonHandler.format
        filepath = os.path.join(path, file)
        os.remove(filepath)

    def exists(path, filename: str = "sample"):
        file = filename + JsonHandler.format
        filepath = os.path.join(path, file)
        return os.path.exists(filepath)


if __name__ == "__main__":
    data = [{}]
    path = os.path.dirname(os.path.realpath(__file__))
    filename = "sample"
    JsonHandler.save(data, path, filename)
    entry = {'a': 1}
    JsonHandler.append(entry, path, filename)
    data = JsonHandler.load(path, filename)
    print(data)
    JsonHandler.remove(path, filename)
    