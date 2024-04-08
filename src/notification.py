import webbrowser
import delete
import threading
import main
import checkData

from tkinter import *
from tkinter import ttk
from create import CreateNewPriceControl as Create
from data import Data


class Notification:
    def __init__(self):
        self.root = Tk()

    def create_window(self, autostart: bool, item_data: list):
        self.root.title("Preiskontrolle")
        self.root.geometry("600x300")

        self.create_menubar(self.root)

        if not autostart:
            self.loading_progress()
        else:
            self.create_treeview(item_data)

        self.root.mainloop()

    def create_treeview(self, item_data: list):
        tree = ttk.Treeview(master=self.root)

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
            selected_item = tree.identify_row(event.y)

            if selected_item:
                item_text = tree.item(selected_item, "values")
                url = item_text[5]
                self.open_webpage(url)

        for item in item_data:
            tree.insert("", "end", text="",
                        values=(
                            item["name"], item["last_day"], item["today"], item["percent"], item["site"], item["url"]))

        tree.bind("<Button-1>", handle_link)

        scrollbar = Scrollbar(master=self.root, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack(expand=True, fill="both")

    @staticmethod
    def create_menubar(root: Tk):
        menubar = Menu(master=root)
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="Neue Datei", command=Create)
        option_menu.add_command(label="Erstellte Dateien", command=delete.DeleteData)
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Datei", menu=option_menu)

        root.config(menu=menubar)

    @staticmethod
    def open_webpage(url: str):
        webbrowser.open(url)

    def loading_progress(self):
        def load_data(progress_bar: ttk.Progressbar):
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
                            message += "Für " + name + "(" + site + ")" + " konnte kein Preis gefunden werden\n"

                        step += 1
                        progress_value = int(step / total_steps * 100)
                        progress_bar.config(value=progress_value)
                        progress_bar.update()
                else:
                    message += "Keine URL für " + site + " gefunden\n"
            if message != "":
                self.message_label(message)
            elif len(notification_data) != 0:
                self.create_treeview(notification_data)
            else:
                self.message_label("Keine Preisveränderungen")

            progress_bar.pack_forget()

        progressbar = ttk.Progressbar(master=self.root, orient="horizontal", length=200, mode="determinate")
        progressbar.pack(pady=10)

        thread = threading.Thread(target=load_data, args=(progressbar,))
        thread.start()

    def message_label(self, message: str):
        Label(master=self.root, text=message, font=("Arial", 12)).pack()
