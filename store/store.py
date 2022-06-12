class Store:
    def __init__(self, name, store_id, file_format):
        self.name = name
        self.id = store_id
        self.format = file_format

    def __str__(self):
        return f"{self.id}_{self.name}, report format: {self.format}"
