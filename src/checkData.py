import requests

from bs4 import BeautifulSoup
from data import Data


class CheckData:
    """
    Eine Klasse zum Überprüfen der Preise von den Webseiten und ob es einen veränderten Preis gibt.
    """
    @staticmethod
    def check_data_alternate(url: str) -> float:
        """
        Überprüft die Webseite "alternate" ob es einen Preis gibt und, falls vorhanden, gibt diesen dann aus.
        :param url: Die URL von der "alternate" Webseite.
        :return: Gibt den Preis aus oder ein -1 bei einem Fehler (z.B. Preis nicht gefunden).
        :raises: AttributeError, wenn das Preiselement nicht gefunden werden kann.
        """
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            try:
                result = soup.find("div", class_="col-12 col-md-auto")
                price = result.text[2:].replace(",", ".")

                return float(price)
            except AttributeError:
                return -1
        else:
            return -1

    @staticmethod
    def check_data_galaxus(url: str) -> float:
        """
        Überprüft die Webseite "galaxus" ob es einen Preis gibt und, falls vorhanden, gibt diesen dann aus.
        :param url: Die URL von der "galaxus" Webseite.
        :return: Gibt den Preis aus oder ein -1 bei einem Fehler (z.B. Preis nicht gefunden).
        :raises: AttributeError, wenn das Preiselement nicht gefunden werden kann.
        """
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            try:
                result = soup.find("button", class_="sc-d112a1b0-5 hMnFnN")

                new_price = result.text[:-4]
                new_price = new_price.replace(",", ".")
                return float(new_price)
            except AttributeError:
                return -1
        else:
            return -1

    @staticmethod
    def amount_in_euro(amount: float) -> str:
        """
        Wandelt den Preis in einen String mit dem € Symbol um.
        :param amount: Der Preis als Kommazahl.
        :return: Gibt den Preis als String aus "99,99 €"
        """
        new_value = "{:.2f}".format(amount)
        new_value = new_value.split(".")

        return f"{new_value[0]},{new_value[1]} €"
    
    @staticmethod
    def __calculate_percent(amount1: float, amount2: float) -> str:
        """
        Berechnet den Prozentwert und rundet ihn. Die Ausgabe ist ein String.
        :param amount1: Der vorletzte Preis des Produktes.
        :param amount2: Der letzte Preis des Produktes.
        :return: Gibt den gerundet Preis mit dem Prozentzeichen aus.
        """
        percent = ((amount1 / amount2) - 1) * 100
        
        return str(round(percent)) + " %"
        
    @classmethod
    def check_new_price(cls, site: str, name: str) -> dict:
        """
        Überprüft, ob für ein Produkt ein Preisunterschied vorhanden ist.
        :param site: Der Name der Webseite für den Preisvergleich.
        :param name: Der Name des Produkts für den Preisvergleich.
        :return: Gibt eine Dictionary mit den relevanten Informationen zum Preisunterschied.

        Die Methode durchsucht die Preisverlaufsdaten für den angegebenen Artikel und Webseite.
        Wenn mindestens zwei Datenpunkte vorhanden sind, wird der Preisunterschied zwischen dem letzten
        und vorletzten Datenpunkt berechnet.

        Wenn der Preisunterschied mindestens 1 % oder weniger als -1 %beträgt, dann wird eine Dictionary mit den folgenden Informationen ausgegeben:

        - name: der Name des Produkts
        - last_day: der Preis am vorletzten Tag
        - today: der aktuelle Preis
        - percent: gerundeter Preisunterschied in Prozent (+ Preisanstieg, - Preisrückgang)
        - site: der Name der Webseite
        - url: die URL der Webseite

        Wenn kein Preisunterschied gefunden wurde, dann wird ein leeres Dictionary ausgegeben.
        """
        result_data = {"name": "", "last_day": "", "today": "", "percent": "", "site": "", "url": ""}
        data = Data.data[site][name]["data"]
        url = Data.data[site][name]["url"]
        data_length = len(data)
        data_values = list(data.values())
        data_keys = list(data.keys())
        last = data_length - 1
        second_last = data_length - 2

        if data_length >= 2:
            percent = ((data_values[second_last] / data_values[last]) - 1) * 100

            if percent >= 1 or percent <= -1:
                if data_values[last] < data_values[second_last]:
                    result_data["name"] = name
                    result_data["last_day"] = (str(data_keys[second_last]) + ": "
                                               + cls.amount_in_euro(data_values[second_last]))
                    result_data["today"] = cls.amount_in_euro(data_values[last])
                    result_data["percent"] = "- " + cls.__calculate_percent(data_values[second_last], data_values[last])
                    result_data["site"] = site
                    result_data["url"] = url

                    return result_data
                elif data_values[data_length - 1] > data_values[data_length - 2]:
                    result_data["name"] = name
                    result_data["last_day"] = (str(data_keys[second_last]) + ": "
                                               + cls.amount_in_euro(data_values[second_last]))
                    result_data["today"] = cls.amount_in_euro(data_values[last])
                    result_data["percent"] = "+ " + cls.__calculate_percent(data_values[last], data_values[second_last])
                    result_data["site"] = site
                    result_data["url"] = url

                    return result_data
                else:
                    return {}
