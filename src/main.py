import os
import json
import datetime
from delete import Delete
from plyer import notification
from create import CreateBirthday


class Birthday:
    """
    Die Birthday-Klasse verwaltet Geburtstage und benachrichtigt über bevorstehende oder aktuelle Geburtstage.
    """
    @classmethod
    def check_birthdays(cls, dates: dict):
        """
        Überprüft die Geburtstage in der Liste und benachrichtigt über heutige oder morgige Geburtstage.
        :param dates: Eine Liste mit den Namen und Geburtstagen im JSON Format.
        """
        today = datetime.date.today()
        tomorrow = (today + datetime.timedelta(days=1)).day
        day = today.day
        month = today.month
        today_list = []
        tomorrow_list = []

        for i in dates:
            birthday_day = int(dates[i][8:10])
            birthday_month = int(dates[i][5:7])

            if birthday_day == day and birthday_month == month:
                age = Delete.calculate_age(dates[i])
                message = i + " ist " + str(age) + " Jahre alt geworden\n"
                today_list.append(message)
            elif birthday_day == tomorrow and birthday_month == month:
                age = Delete.calculate_age(dates[i]) + 1
                message = i + " wird " + str(age) + " Jahre alt werden\n"
                tomorrow_list.append(message)

        if len(today_list) != 0:
            notification.notify(title="Heute", message=" ".join(today_list), toast=True, timeout=3)

        if len(tomorrow_list) != 0:
            notification.notify(title="Morgen", message=" ".join(tomorrow_list), toast=True, timeout=3)

    def open_window(self):
        """
        Öffnet ein Fenster zur Verwaltung der Geburtstage.
        """
        self.load_dates()
        CreateBirthday()

    def load_dates(self):
        """
        Lädt Geburtstagsdaten aus einer JSON Datei.
        Falls diese nicht vorhanden sein, dann wird eine neue Datei erstellt.
        """
        file_name = "geburtstage.json"

        if os.path.isfile(file_name):
            file = open(file_name, "r")
            dates = json.load(file)
            CreateBirthday.dates = dates

            self.check_birthdays(dates)
        else:
            file = open(file_name, "w")
            json.dump({}, file)


if __name__ == "__main__":
    Birthday.open_window(Birthday())
