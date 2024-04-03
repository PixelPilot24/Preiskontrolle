import json
import os.path

from checkData import CheckData
from notification import Notification
from datetime import datetime


class Data:
    data = {
        "alternate": {
            "Samsung 980 1TB M2": {
                "url": "https://www.alternate.de/SAMSUNG/980-PRO-1-TB-SSD/html/product/1670614",
                "data": {}
            }
        },
        "galaxus": {}
    }


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

            for i in Data.data:
                if len(Data.data[i]) != 0:
                    for name in Data.data[i].keys():
                        url = Data.data[i][name]["url"]

                        if i == "alternate":
                            price = CheckData.check_data_alternate(url)
                            self.insert_data(i, name, price)
                        else:
                            CheckData.check_data_galaxus(url)
                else:
                    message = "Keine URL für " + i + " gefunden"

            if message != "":
                Notification(message, False)
        else:
            self.save_json()


if __name__ == '__main__':
    DataHandler()
    # DataHandler.check_data_alternate("https://www.alternate.de/SAMSUNG/980-PRO-1-TB-SSD/html/product/1670614")
    # DataHandler.check_data_galaxus("https://www.galaxus.de/de/s1/product/kingston-nv2-1000-gb-m2-2280-ssd-21983494")
