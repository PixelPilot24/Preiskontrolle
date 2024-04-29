import threading
import checkData
import main

from tkinter import *
from data import Data
from tkinter import messagebox


class CreateNewPriceControl:
    """
    Diese Klasse erstellt ein Fenster zum Erstellen von einer neuen Preiskontrolle.
    """
    def __init__(self):
        """
        Erstellt ein neues Fenster, im anschluss dann die Widgets.
        """
        self.__root = Tk()
        self.__root.title("Neue Datei erstellen")
        self.__root.geometry("350x150")

        self.__name_entry = Entry()
        self.__url_entry = Entry()

        self.__create_widgets()

    def __create_widgets(self):
        """
        Erstellt die Widgets für die Erstellung einer neuen Preiskontrolle.
        """
        font = ("Arial", 12)

        frame = Frame(master=self.__root)
        name_label = Label(master=frame, text="Name", font=("Arial", 10))
        url_label = Label(master=frame, text="URL", font=("Arial", 10))

        self.__name_entry = Entry(master=frame, font=font)
        self.__url_entry = Entry(master=frame, font=font)

        save_button = Button(master=frame, text="Speichern", command=self.__save_data)

        name_label.pack(anchor=W)
        self.__name_entry.pack()
        url_label.pack(anchor=W)
        self.__url_entry.pack()
        save_button.pack(pady=10)
        frame.pack()

    @staticmethod
    def __check_url(url: str) -> str:
        """
        Überprüft die URL und gibt den richtigen Namen aus. Falls in der URL nicht der passende Name ist, dann wird ein
        "error" ausgegeben.
        :param url: Die URL von der Seite.
        :return: Gibt den Namen der Seite aus oder, falls nicht die richtige Seite beinhaltet ist, ein error aus.
        """
        if "alternate" in url:
            return "alternate"
        elif "galaxus" in url:
            return "galaxus"
        else:
            return "error"
        
    @staticmethod
    def __check_and_save_data(name: str, url: str, site: str):
        """
        Überprüft, ob die URL zu den Webseiten gehört, falls nicht oder kein Preis gefunden wurde, dann wird das
        Fenster mit der Information angezeigt.
        :param name: Der Name des Produkts.
        :param url: Die URL von dem Produkt.
        :param site: Der Name der Webseite.
        """
        check = checkData.CheckData

        if site == "alternate":
            price = check.check_data_alternate(url)
        else:
            price = check.check_data_galaxus(url)

        Data.data[site].update({name: {"url": url, "data": {}}})
        main.DataHandler.insert_data(site, name, price)
        messagebox.showinfo("Daten gespeichert", "Daten wurden erfolgreich gespeichert.")

    def __save_data(self):
        """
        Überprüft den Namen und die URL des Produkts. Falls der Name oder die URL leer sind, dann wird ein Fenster
        mit dem passenden Text ausgegeben. Wenn keine Fehler vorhanden sind, dann werden die Informationen gespeichert.
        """
        name = self.__name_entry.get()
        url = self.__url_entry.get()
        site = self.__check_url(url)

        if name == "":
            messagebox.showerror("Name", "Der Name darf nicht leer sein.")
        elif url == "":
            messagebox.showerror("URL", "Die URL darf nicht leer sein.")
        elif site == "error":
            messagebox.showerror("Falsche URL", "Die URL enthält weder alternate noch galaxus.")
        else:
            thread = threading.Thread(target=self.__check_and_save_data, args=(name, url, site))
            thread.start()
            self.__name_entry.delete(0, "end")
            self.__url_entry.delete(0, "end")
    
    def run(self):
        """
        Setzt den Fokus auf das Fenster und startet es.
        """
        self.__root.focus_force()
        self.__root.mainloop()
