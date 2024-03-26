import os
import json
from create import CreateBirthday


class Birthday:
    @staticmethod
    def check_birthdays(dates):
        print(dates)

    def create_birthday(self):
        pass

    @staticmethod
    def notification(name):
        pass

    def load_dates(self):
        file_name = "geburtstage.json"
        if os.path.isfile(file_name):
            file = open(file_name, "r")
            dates = json.load(file)
            CreateBirthday.dates = dates

            if not len(dates) == 0:
                self.check_birthdays(dates)
                print("Datei geladen: " + str(dates))
                CreateBirthday()
                self.check_birthdays(dates)
            else:
                CreateBirthday()
        else:
            file = open(file_name, "w")
            json.dump({}, file)
            CreateBirthday()


if __name__ == "__main__":
    Birthday.load_dates(Birthday())
