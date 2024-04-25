import datetime
import validator

from plyer import notification
from json_handler import JsonHandler as Json
from baseWindow import BaseGUI


class Birthday:
    """
    Eine Klasse, um Geburtstage zu überprüfen und Benachrichtigungen anzuzeigen.
    """
    @staticmethod
    def check_birthdays():
        """
        Überprüft Geburtstage für heute und morgen aus der JSON-Datei und zeigt Benachrichtigungen an, wenn es welche gibt.
        """
        dates = Json().json_data
        today = datetime.date.today()
        tomorrow = (today + datetime.timedelta(days=1)).day
        day = today.day
        month = today.month
        today_list = []
        tomorrow_list = []
        vali = validator.DataValidator()

        for i in dates:
            birthday_day = int(dates[i][8:10])
            birthday_month = int(dates[i][5:7])

            if birthday_day == day and birthday_month == month:
                age = vali.calculate_age(dates[i])
                message = i + " ist " + str(age) + " Jahre alt geworden\n"
                today_list.append(message)
            elif birthday_day == tomorrow and birthday_month == month:
                age = vali.calculate_age(dates[i]) + 1
                message = i + " wird " + str(age) + " Jahre alt werden\n"
                tomorrow_list.append(message)

        if len(today_list) != 0:
            notification.notify(title="Heute", message=" ".join(today_list), toast=True, timeout=3)

        if len(tomorrow_list) != 0:
            notification.notify(title="Morgen", message=" ".join(tomorrow_list), toast=True, timeout=3)

    @classmethod
    def run(cls):
        """
        Lädt die JSON-Datei, überprüft die Geburtstage und zeigt Benachrichtigungen an. Startet auch die GUI.
        :return:
        """
        Json().load_json_file()
        cls.check_birthdays()
        BaseGUI().run()


if __name__ == "__main__":
    Birthday().run()
