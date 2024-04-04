import json
import os.path

from checkData import CheckData
from notification import Notification
from datetime import datetime
from data import Data


class DataHandler:
    def __init__(self):
        self.load_data()

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

    def load_data(self):
        file_name = "price-control.json"
        message = ""

        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                Data.data = json.load(file)

            notification_data = []

            for i in Data.data:
                if len(Data.data[i]) != 0:
                    for name in Data.data[i].keys():
                        url = Data.data[i][name]["url"]

                        if i == "alternate":
                            # TODO versuchen das überprüfen über mehrere Kerne laufen zu lassen
                            price = CheckData.check_data_alternate(url)
                        else:
                            price = CheckData.check_data_galaxus(url)

                        self.insert_data(i, name, price)

                        data_list = CheckData.check_new_price(i, name)

                        if len(data_list) != 0:
                            notification_data.append(data_list)
                else:
                    message = "Keine URL für " + i + " gefunden"

            if message != "":
                Notification(message, False, [])
            elif len(notification_data) != 0:
                Notification("", True, notification_data)
        else:
            self.save_json()


if __name__ == '__main__':
    DataHandler()
