import webbrowser
import dataGUI
import threading
import main
import checkData

from tkinter import *
from tkinter import ttk
from create import CreateNewPriceControl as Create
from data import Data


class Notification:
    """
    Eine Klasse zur Anzeige von Benachrichtigungen und Daten in einem Fenster.
    """
    def __init__(self):
        self.__root = Tk()

    def __create_window(self, autostart: bool, item_data: list):
        """
        Erstellt das Hauptfenster mit Menüleiste und Anzeige der Daten in einem Treeview.

        :param autostart: Ein Boolean, der angibt, ob der Autostart aktiviert ist.
        :param item_data: Eine Liste von Daten für die Anzeige im Treeview.
        """
        self.__root.title("Preiskontrolle")
        self.__root.geometry("600x300")

        self.__create_menubar()

        if not autostart:
            self.__loading_progress()
        else:
            self.__create_treeview(item_data)

    def __create_treeview(self, item_data: list):
        """
        Erstellt einen Treeview zur Anzeige von Daten in tabellarischer Form.

        :param item_data: Eine Liste von Daten für die Anzeige im Treeview.
        """
        tree = ttk.Treeview(master=self.__root)

        tree.config(columns=("name", "last_day", "today", "percent", "site"))

        tree.column("#0", width=0, stretch=NO)
        tree.column("name", width=160)
        tree.column("last_day", width=120)
        tree.column("today", width=100)
        tree.column("percent", width=100, anchor="center")
        tree.column("site", width=100, anchor="center")

        tree.heading("#0", text="")
        tree.heading("name", text="Name")
        tree.heading("last_day", text="Letzter Tag")
        tree.heading("today", text="Heute")
        tree.heading("percent", text="Prozent")
        tree.heading("site", text="Seite")

        def handle_link(event):
            """
            Ermöglicht das beim Anklicken des Textes die Webseite geöffnet wird.
            """
            selected_item = tree.identify_row(event.y)

            if selected_item:
                item_text = tree.item(selected_item, "values")
                url = item_text[5]
                self.open_webpage(url)

        for item in item_data:
            tree.insert("", "end", text="",
                        values=(
                            item["name"], item["last_day"], item["today"],
                            item["percent"], item["site"], item["url"])
                        )

        tree.bind("<Button-1>", handle_link)

        scrollbar = Scrollbar(master=self.__root, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack(expand=True, fill="both")

    def __create_menubar(self):
        """
        Erstellt die Menüleiste mit verschiedenen Optionen wie "Neue Datei", "Erstellte Dateien" und "Schließen".
        """
        menubar = Menu(master=self.__root)
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="Neue Datei", command=lambda: Create().run())
        option_menu.add_command(label="Erstellte Dateien", command=dataGUI.DataGUI)
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Datei", menu=option_menu)

        self.__root.config(menu=menubar)

    @staticmethod
    def open_webpage(url: str):
        """
        Öffnet die angegebene URL in einem Webbrowser.

        :param url: Die URL, die geöffnet werden soll.
        """
        webbrowser.open(url)

    def __loading_progress(self):
        """
        Zeigt einen Ladebalken während des Datenladeprozesses an.
        """
        progressbar = ttk.Progressbar(master=self.__root, orient="horizontal", length=200, mode="determinate")
        progressbar.pack(pady=10)

        thread = threading.Thread(target=self.__load_data, args=(progressbar,))
        thread.start()

    def __load_data(self, progress_bar: ttk.Progressbar):
        """
        Lädt Daten von verschiedenen Webseiten, überprüft Preise und aktualisiert die Anzeige.

        :param progress_bar: Der Fortschrittsbalken zur Anzeige des Ladefortschritts.
        """
        total_steps = len(Data.data["alternate"]) + len(Data.data["galaxus"])
        step = 0
        message = ""
        notification_data = []

        for site in Data.data:
            if len(Data.data[site]) != 0:
                for name in Data.data[site].keys():
                    check = checkData.CheckData
                    url = Data.data[site][name]["url"]

                    if site == "alternate":
                        price = check.check_data_alternate(url)
                    else:
                        price = check.check_data_galaxus(url)

                    if price > 0:
                        main.DataHandler.insert_data(site, name, price)
                        data_list = check.check_new_price(site, name)

                        if data_list is not None and len(data_list) != 0:
                            notification_data.append(data_list)
                    else:
                        message += f"Für {name} ({site}) konnte kein Preis gefunden werden\n"

                    step += 1
                    progress_value = int(step / total_steps * 100)
                    progress_bar.config(value=progress_value)
                    progress_bar.update()
            else:
                message += f"Keine URL für {site} gefunden\n"
        if message != "":
            self.__message_label(message)
        elif len(notification_data) != 0:
            self.__create_treeview(notification_data)
        else:
            self.__message_label("Keine Preisveränderungen")

        progress_bar.pack_forget()

    def __message_label(self, message: str):
        """
        Zeigt eine Nachricht im Fenster an.

        :param message: Die Nachricht, die angezeigt werden soll.
        """
        Label(master=self.__root, text=message, font=("Arial", 12)).pack()

    def run(self, autostart: bool, item_data: list):
        """
        Startet die Benachrichtigungsanwendung mit den übergebenen Daten.

        :param autostart: Ein Boolean, der angibt, ob der Autostart aktiviert ist.
        :param item_data: Eine Liste von Daten für die Anzeige im Treeview.
        """
        self.__create_window(autostart, item_data)
        
        self.__root.mainloop()
