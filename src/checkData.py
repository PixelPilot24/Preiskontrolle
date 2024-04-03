import requests
from bs4 import BeautifulSoup


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
    def check_data_galaxus(url: str):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            results = soup.find_all("button", class_="sc-125c42c7-5 hMyxKO")

            for elem in results:
                price = elem.text
                print(price)
        else:
            print("Fehler: ", response.status_code)

