from tkinter import *
import webbrowser
from tkinter import ttk


class Notification:
    def __init__(self, message: str, new_price: bool, data: list):
        root = Tk()
        root.title("Preiskontrolle")
        root.geometry("600x300")
        root["bg"] = "#ac9fa9"

        self.create_menubar(root)

        if new_price:
            self.create_treeview(root, data)
        else:
            Label(master=root, text=message, font=("Arial", 12)).pack()

        root.mainloop()

    def create_treeview(self, root: Tk, item_data: list):
        tree = ttk.Treeview(master=root)

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

        scrollbar = Scrollbar(master=root, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack(expand=True, fill="both")

    def create_menubar(self, root: Tk):
        menubar = Menu(master=root)
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="Neue Datei", command=self.new_data)
        option_menu.add_command(label="Erstellte Dateien", command=self.created_data)
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Datei", menu=option_menu)

        root.config(menu=menubar)

    @staticmethod
    def open_webpage(url: str):
        webbrowser.open(url)

    def new_data(self):
        pass

    def created_data(self):
        pass

    def check_new_price(self):
        pass
