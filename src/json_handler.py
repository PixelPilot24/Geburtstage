import json
import os.path


class JsonHandler:
    """
    In dieser Klasse wird die JSON Datei gespeichert, geladen und abgerufen.
    """
    __file_name = "geburtstage.json"
    __json_data = {}

    @classmethod
    def save_in_json(cls, dates: dict):
        file = open(cls.__file_name, "w")
        json.dump(dates, file)

    @classmethod
    def load_json_file(cls):
        if os.path.isfile(cls.__file_name):
            file = open(cls.__file_name, "r")
            data = json.load(file)
            cls.__json_data = data
        else:
            cls.save_in_json({})

    @property
    def json_data(self) -> dict:
        return self.__json_data
