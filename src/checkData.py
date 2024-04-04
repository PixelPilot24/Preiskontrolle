import requests

from bs4 import BeautifulSoup
from data import Data


class CheckData:
    @staticmethod
    def check_data_alternate(url: str) -> float:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            results = soup.find_all("div", class_="col-12 col-md-auto")

            for elem in results:
                price = elem.text
                splice = price.split(" ")

                if len(splice) == 2:
                    price_list = price[2:].split(",")
                    new_price = price

                    if len(price_list) > 1:
                        new_price = price_list[0] + "." + price_list[1]

                    return float(new_price)
        else:
            print("Fehler: ", response.status_code)

    @staticmethod
    def check_data_galaxus(url: str) -> float:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            results = soup.find_all("button", class_="sc-125c42c7-5 hMyxKO")

            for elem in results:
                price = elem.text
                price_list = price.split(",")
                new_price = price

                if len(price_list) > 1:
                    new_price = price_list[0] + "." + price_list[1]

                return float(new_price)
        else:
            print("Fehler: ", response.status_code)

    @staticmethod
    def amount_in_euro(amount: float) -> str:
        new_value = "{:.2f}".format(amount)
        new_value = new_value.split(".")

        return new_value[0] + "," + new_value[1] + " €"
    
    @staticmethod
    def calculate_percent(amount1: float, amount2: float) -> str:
        percent = ((amount1 / amount2) - 1) * 100
        
        return str(round(percent)) + " %"
        
    @classmethod
    def check_new_price(cls, site: str, name: str) -> dict:
        result_data = {"name": "", "last_day": "", "today": "", "percent": "", "site": "", "url": ""}
        data = Data.data[site][name]["data"]
        url = Data.data[site][name]["url"]
        data_length = len(data)
        data_values = list(data.values())
        data_keys = list(data.keys())
        last = data_length - 1
        second_last = data_length - 2

        if data_length >= 2:
            if data_values[last] < data_values[second_last]:
                result_data["name"] = name
                result_data["last_day"] = (str(data_keys[second_last]) + ": "
                                           + cls.amount_in_euro(data_values[second_last]))
                result_data["today"] = cls.amount_in_euro(data_values[last])
                result_data["percent"] = "- " + cls.calculate_percent(data_values[second_last], data_values[last])
                result_data["site"] = site
                result_data["url"] = url

                return result_data
            elif data_values[data_length - 1] > data_values[data_length - 2]:
                result_data["name"] = name
                result_data["last_day"] = (str(data_keys[second_last]) + ": "
                                           + cls.amount_in_euro(data_values[second_last]))
                result_data["today"] = cls.amount_in_euro(data_values[last])
                result_data["percent"] = "+ " + cls.calculate_percent(data_values[last], data_values[second_last])
                result_data["site"] = site
                result_data["url"] = url

                return result_data
            else:
                return {}
