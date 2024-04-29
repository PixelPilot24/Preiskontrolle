import json
import os.path
import notification

from datetime import datetime
from data import Data


class DataHandler:
    """
    Diese Klasse enthält Methoden zum Speichern, Laden und Bearbeiten von Daten in einer JSON-Datei.
    """
    @staticmethod
    def save_json():
        """
        Speichert die Daten in der "price-control.json" Datei.
        """
        with open("price-control.json", "w") as file:
            json.dump(Data.data, file)

    @classmethod
    def insert_data(cls, site: str, name: str, price: float):
        """
        Fügt zur richtigen Webseite und Namen das Datum mit dem aktuellen Preis.
        :param site: Webseite, zu der die Daten gehören.
        :param name: Der Name des Produkts.
        :param price: Der Preis des Produkts
        """
        today = datetime.now()
        formatted_date = today.strftime("%d.%m.%Y")

        if site not in Data.data:
            print("Diese Seite wurde nicht gefunden")
        elif name not in Data.data[site]:
            print("Dieser Name wurde nicht gefunden")
        else:
            Data.data[site][name]["data"][formatted_date] = price

        cls.save_json()

    @classmethod
    def load_json(cls, autostart: bool):
        """
        Lädt die JSON Datei "price-control.json".
        :param autostart: Ein Boolean der angibt, ob es sich um einen Autostart handelt.
        """
        file_name = "price-control.json"

        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                Data.data = json.load(file)

            if not autostart:
                noti = notification.Notification()
                noti.run(False, [])

            cls.save_json()
        else:
            cls.save_json()


if __name__ == '__main__':
    DataHandler.load_json(False)
