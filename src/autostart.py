import main
import checkData
import notification

from data import Data


class Autostart:
    @staticmethod
    def load_and_check_data():
        _main = main.DataHandler
        _main.load_json(_main(), True)
        notification_data = []

        for site in Data.data:
            data_site = Data.data[site]

            if len(data_site) != 0:
                for name in data_site.keys():
                    check = checkData.CheckData
                    url = data_site[name]["url"]

                    if site == "alternate":
                        price = check.check_data_alternate(url)
                    else:
                        price = check.check_data_galaxus(url)

                    if price > 0:
                        main.DataHandler.insert_data(site, name, price)
                        data_list = check.check_new_price(site, name)

                        if data_list is not None and len(data_list) != 0:
                            notification_data.append(data_list)

        if len(notification_data) != 0:
            noti = notification.Notification
            noti.create_window(noti(), True, notification_data)


if __name__ == '__main__':
    Autostart.load_and_check_data()
