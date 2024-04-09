import threading
import checkData
import main

from tkinter import *
from data import Data


class CreateNewPriceControl:
    def __init__(self):
        self.root = Tk()
        self.root.title("Neue Datei erstellen")
        self.root.geometry("350x250")

        self.error_text = Label()
        self.name_entry = Entry()
        self.url_entry = Entry()

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        font = ("Arial", 12)

        Label(master=self.root, text="Name", font=font).place(x=10, y=10)
        Label(master=self.root, text="URL", font=font).place(x=10, y=50)
        self.error_text = Label(master=self.root, text="", fg="red")

        self.name_entry = Entry(master=self.root, font=font)
        self.url_entry = Entry(master=self.root, font=font)

        save_button = Button(master=self.root, text="Speichern", command=self.save_data)

        self.error_text.place(relx=0.5, y=90, anchor="center")
        self.name_entry.place(x=70, y=10)
        self.url_entry.place(x=70, y=50)
        save_button.place(relx=0.5, y=120, anchor="center")

    @staticmethod
    def check_url(url: str) -> str:
        if "alternate" in url:
            return "alternate"
        elif "galaxus" in url:
            return "galaxus"
        else:
            return "error"

    def check_and_save_data(self, name: str, url: str, site: str):
        check = checkData.CheckData

        if site == "alternate":
            price = check.check_data_alternate(url)
        else:
            price = check.check_data_galaxus(url)

        Data.data[site].update({name: {"url": url, "data": {}}})
        main.DataHandler.insert_data(site, name, price)
        self.error_text.config(text="Daten gespeichert", fg="green")

    def save_data(self):
        name = self.name_entry.get()
        url = self.url_entry.get()
        site = self.check_url(url)

        if site == "error":
            self.error_text.config(text="Die URL enthält weder alternate noch galaxus", fg="red")
        else:
            thread = threading.Thread(target=self.check_and_save_data, args=(name, url, site))
            thread.start()
            self.name_entry.delete(0, "end")
            self.url_entry.delete(0, "end")
