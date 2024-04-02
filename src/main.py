import requests
from bs4 import BeautifulSoup


class Data:
    @staticmethod
    def check_data_alternate(url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            results = soup.find(id="j_idt364")
            elements = results.find_all("div", class_="col-12 col-md-auto")

            for elem in elements:
                price = elem.text
                splice = price.split(" ")

                if len(splice) == 2:
                    print(splice[1])
        else:
            print("Fehler: ", response.status_code)

    @staticmethod
    def check_data_galaxus(url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            results = soup.find(id="pageContent")
            elements = results.find_all("button", class_="sc-125c42c7-5 hMyxKO")

            for elem in elements:
                price = elem.text
                print(price)
        else:
            print("Fehler: ", response.status_code)


if __name__ == '__main__':
    Data.check_data_alternate("https://www.alternate.de/SAMSUNG/980-PRO-1-TB-SSD/html/product/1670614")
    Data.check_data_galaxus("https://www.galaxus.de/de/s1/product/kingston-nv2-1000-gb-m2-2280-ssd-21983494")
