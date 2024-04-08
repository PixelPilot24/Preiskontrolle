import json
import os.path
import notification

from datetime import datetime
from data import Data


class DataHandler:
    @staticmethod
    def save_json():
        with open("price-control.json", "w") as file:
            json.dump(Data.data, file)

    @classmethod
    def insert_data(cls, site: str, name: str, price: float):
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
        file_name = "price-control.json"

        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                Data.data = json.load(file)

            if not autostart:
                noti = notification.Notification
                noti.create_window(noti(), False, [])

            cls.save_json()
        else:
            cls.save_json()


if __name__ == '__main__':
    DataHandler.load_json(False)
