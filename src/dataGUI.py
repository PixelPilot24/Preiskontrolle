import notification
import checkData
import main

from tkinter import messagebox
from tkinter import *
from data import Data
from edit import EditName


class DataGUI:
    """
    Eine Klasse wo die Daten angezeigt, bearbeitet und gelöscht werden können.
    """
    def __init__(self):
        """
        Erstellt das Fenster und im Anschluss die Widgets mit den Produkten.
        """
        self.__root = Tk()
        self.__root.title("Erstellte Daten")
        self.__root.geometry("600x400")
        self.__root.focus_force()
        self.__max_width = (0, 0)
        self.__frame_list = []

        self.__canvas = Canvas()
        self.__create_data_list()

    def __create_label_and_button(self, frame_site: Frame, index: int, site: str):
        """
        In dieser Methode wird das Label und die Buttons für "Seite besuchen" und "Löschen" erstellt.
        :param frame_site: Das Frame für die Seite, in der die Widgets erstellt werden sollen.
        :param index: Der Index gibt die Zeile in der die Widgets erstellt werden.
        :param site: Der Name der Webseite.

        Die Farbe für die jeweilige Zeile ist weiß und jede zweite Zeile ist grün um diese besser zu unterscheiden.
        """
        pad = 5
        frame_item = Frame(master=frame_site, padx=pad, pady=pad)

        def delete_data():
            """
            Es wird abgefragt, ob das Produkt gelöscht werden soll. Falls ja, dann wird das Produkt gelöscht.
            """
            result = messagebox.askyesno("Löschen", "Sollen die Daten wirklich gelöscht werden?")

            if result:
                Data.data[site].pop(name)
                frame_item.destroy()
                main.DataHandler.save_json()

        data = Data.data
        color = "#ffffff" if index % 2 == 0 else "#82ee82"
        data_names = list(data[site].keys())
        name = data_names[index]
        data_name = data[site][name]
        data_values = list(data_name["data"].values())
        data_length = len(data_values)
        point_price = data_values[data_length - 1]
        price = checkData.CheckData.amount_in_euro(point_price)
        url = data_name["url"]

        name_label = Label(master=frame_item, text=name, padx=pad, pady=pad, bg=color, fg="blue")
        price_label = Label(master=frame_item, text=price, padx=pad, pady=pad, bg=color)
        name_label.grid(row=index, column=0)
        price_label.grid(row=index, column=1)

        def name_clicked(event):
            """
            Ändert das Label in ein Entry Feld, wenn auf diesen geklickt wird, um den Namen zu ändern.
            """
            label_width = self.__max_width[0]
            EditName.rename(name_label, frame_item, index, name, color, site, label_width)

        name_label.bind("<Button-1>", name_clicked)

        Button(master=frame_item, text="Seite besuchen", padx=pad, pady=pad,
               command=lambda u=url: notification.Notification.open_webpage(u)).grid(row=index, column=2)
        Button(master=frame_item, text="Löschen", padx=pad, pady=pad,
               command=delete_data).grid(row=index, column=3)

        frame_item.config(bg=color)
        frame_item.grid(row=index + 1)
        """
        Der unterer Code speichert das Label vom Namen und dem Preis. Die Länge der beiden Labels wird addiert und,
        wenn diese größer sind als das __max_width, wird der Wert verändert. In der __create_data_list() werden 
        alle Labels auf die gleiche Länge geändert.
        """
        self.__frame_list.append((name_label, price_label))
        current_length = len(name) + len(price)
        max_length = sum(self.__max_width)

        if max_length < current_length:
            self.__max_width = (len(name), len(price))

    def __create_scrollbar(self, frame: Frame):
        """
        Erstellt die Scrollleisten im Fenster.
        :param frame: Das Frame vom __root
        """
        scrollbar_x = Scrollbar(master=frame, orient="horizontal")
        scrollbar_y = Scrollbar(master=frame, orient="vertical")
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.config(command=self.__canvas.xview)
        scrollbar_y.config(command=self.__canvas.yview)
        self.__canvas.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    def __on_mouse_wheel(self, event: Event):
        """
        Ermöglicht das scrollen mit dem Mausrad in dem Fenster.
        """
        self.__canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def __create_data_list(self):
        """
        Erstellt eine Liste von den Produkten für jede Webseite.

        Diese Methode erstellt ein Canvas im Hauptframe und fügt ein inneres Frame hinzu, um die Daten anzuzeigen.
        Für jede Webseite werden Labels und Buttons erstellt, um die Daten anzuzeigen und Aktionen auszuführen.
        Die Labels werden basierend auf der maximalen Breite der Namen und Preise angepasst.
        Eine Scrollleiste wird hinzugefügt.
        """
        data = Data.data

        frame_main = Frame(master=self.__root)

        self.__canvas = Canvas(master=frame_main, scrollregion=(0, 0, 700, 700))
        self.__canvas.bind_all("<MouseWheel>", self.__on_mouse_wheel)

        inner_frame = Frame(self.__canvas)
        self.__canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        for site in data:
            frame_site = Frame(master=inner_frame, relief="ridge", borderwidth=4)
            Label(master=frame_site, text=site).grid(row=0, column=0)

            for index in range(len(data[site])):
                self.__create_label_and_button(frame_site, index, site)

            frame_site.grid()

        for name, price in self.__frame_list:
            name.config(width=self.__max_width[0])
            price.config(width=self.__max_width[1])

        inner_frame.update_idletasks()
        self.__canvas.config(scrollregion=self.__canvas.bbox("all"))
        self.__create_scrollbar(frame_main)

        self.__canvas.pack(side="left", fill="both", expand=True)
        frame_main.pack(side="left", fill="both", expand=True)

    def run(self):
        self.__root.mainloop()
