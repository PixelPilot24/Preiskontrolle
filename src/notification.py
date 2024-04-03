from tkinter import *
import webbrowser


class Notification:
    def __init__(self, message: str, new_price: bool, url=""):
        root = Tk()
        root.title("Preiskontrolle")
        root.geometry("300x300")

        font = ("Arial", 12)

        Label(master=root, text=message, font=font).pack()
        if new_price:
            got_to_site_button = Button(master=root, text="Seite besuchen", font=font)
            got_to_site_button.config(command=lambda: self.open_webpage(url))
            got_to_site_button.pack()

        menubar = Menu(master=root)
        option_menu = Menu(menubar, tearoff=0)
        option_menu.add_command(label="Neue Datei", command=self.new_data)
        option_menu.add_command(label="Erstellte Dateien", command=self.created_data)
        option_menu.add_separator()
        option_menu.add_command(label="Schließen", command=lambda: exit())
        menubar.add_cascade(label="Datei", menu=option_menu)

        root.config(menu=menubar)
        root.mainloop()

    @staticmethod
    def open_webpage(url: str):
        webbrowser.open(url)

    def new_data(self):
        pass

    def created_data(self):
        pass

    def check_new_price(self):
        pass
