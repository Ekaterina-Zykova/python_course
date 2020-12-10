class KeyValueStorage:
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path) as file:
            for line in file:
                key, value = line.strip().split("=")
                if not key[0].isdigit():
                    if value.isdigit():
                        self.data[key] = int(value)
                    else:
                        self.data[key] = value
                else:
                    raise ValueError(
                        "Key starts with a digit, key cannot be an attribute"
                    )

    def __getitem__(self, key):
        return self.data[key]

    def __getattr__(self, name):
        return self.__getitem__(name)
