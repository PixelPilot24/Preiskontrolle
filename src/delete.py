import notification
import checkData
import main

from tkinter import messagebox
from tkinter import *
from data import Data
from edit import EditName


class DeleteData:
    def __init__(self):
        self.root = Tk()
        self.root.title("Erstellte Daten")
        self.root.attributes("-topmost", True)
        self.root.geometry("600x400")

        self.canvas = Canvas()
        self.create_data_list()

        self.root.mainloop()

    @staticmethod
    def create_label_and_button(frame_site: Frame, index: int, site: str):
        pad = 5
        frame_item = Frame(master=frame_site, padx=pad, pady=pad)

        def delete_data():
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
        data_length = len(data_name["data"].values())
        point_price = list(data_name["data"].values())[data_length - 1]
        price = checkData.CheckData.amount_in_euro(point_price)
        url = data_name["url"]

        name_label = Label(master=frame_item, text=name, padx=pad, pady=pad, bg=color, fg="blue")
        name_label.grid(row=index, column=0)

        def name_clicked(event):
            width = name_label.winfo_width() // 6
            EditName.rename(name_label, frame_item, index, name, width, color, site)

        name_label.bind("<Button-1>", name_clicked)
        Label(master=frame_item, text=price, padx=pad, pady=pad, bg=color).grid(row=index, column=1)
        Button(master=frame_item, text="Seite besuchen", padx=pad, pady=pad,
               command=lambda u=url: notification.Notification.open_webpage(u)).grid(row=index, column=2)
        Button(master=frame_item, text="Löschen", padx=pad, pady=pad,
               command=delete_data).grid(row=index, column=3)

        frame_item.config(bg=color)

        frame_item.grid(row=index + 1)

    def create_scrollbar(self, frame: Frame):
        scrollbar_x = Scrollbar(master=frame, orient="horizontal")
        scrollbar_y = Scrollbar(master=frame, orient="vertical")
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.config(command=self.canvas.xview)
        scrollbar_y.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    def on_mouse_wheel(self, event: Event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_data_list(self):
        data = Data.data

        frame_main = Frame(master=self.root)

        self.canvas = Canvas(master=frame_main, scrollregion=(0, 0, 700, 700))
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        for site in data:
            frame_site = Frame(master=inner_frame, relief="ridge", borderwidth=4)
            Label(master=frame_site, text=site).grid(row=0, column=0)

            for index in range(len(data[site])):
                self.create_label_and_button(frame_site, index, site)

            frame_site.grid()

        inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.create_scrollbar(frame_main)

        self.canvas.pack(side="left", fill="both", expand=True)
        frame_main.pack(side="left", fill="both", expand=True)
