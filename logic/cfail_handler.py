import json

class Handler:
    def __init__(self):
        pass

    def _write_json(self, layout):
        with open("data/data.json", "w") as fh1:
            eme = json.dump(fh1, layout)  # записываем структуру в файл
            return eme

    def _reade_json(self):
        with open("data/data.json", "r") as fh:
            ama =json.load(fh)  # записываем структуру в файл
            return ama

