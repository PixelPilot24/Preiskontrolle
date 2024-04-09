from tkinter import *
from data import Data


class EditName:
    @classmethod
    def save_method(cls, site: str, old_name: str, new_name: str, edit_frame: Frame, label_frame: Frame,
                    color: str, index: int):
        data = Data.data[site]
        new_data = {}
        data[new_name] = data[old_name]
        keys = list(data.keys())
        new_list = []

        old_idx = 0
        new_idx = 0

        for i in range(len(keys)):
            if keys[i] == old_name:
                old_idx = i
            if keys[i] == new_name:
                new_idx = i

        for i in keys:
            new_list.append({i: data[i]})

        new_list[old_idx], new_list[new_idx] = new_list[new_idx], new_list[old_idx]
        new_list.pop(len(new_list) - 1)

        for i in new_list:
            key = list(i.keys())[0]
            value = list(i.values())[0]
            new_data[key] = value

        Data.data[site] = new_data
        cls.cancel_method(edit_frame, label_frame, new_name, color, index, site)

    @staticmethod
    def cancel_method(edit_frame: Frame, label_frame: Frame, name: str, color: str, index: int, site):
        edit_frame.destroy()
        name_label = Label(master=label_frame, text=name, pady=5, padx=5, bg=color, fg="blue")

        def name_clicked(event):
            width = name_label.winfo_width() // 6
            EditName.rename(name_label, label_frame, index, name, width, color, site)

        name_label.grid(row=index, column=0)
        name_label.bind("<Button-1>", name_clicked)

    @classmethod
    def rename(cls, name_label: Label, frame: Frame, index: int, name: str, width: int, color: str, site: str):
        new_frame = Frame(master=frame)
        name_label.destroy()

        name_entry = Entry(master=new_frame, width=width)
        save_button = Button(master=new_frame, text="\u2713")
        cancel_button = Button(master=new_frame, text="\u2718")

        save_button.config(
            command=lambda: cls.save_method(site, name, name_entry.get(), new_frame, frame, color, index))
        cancel_button.config(command=lambda: cls.cancel_method(new_frame, frame, name, color, index, site))
        name_entry.insert(0, name)

        name_entry.grid(row=0, column=0)
        save_button.grid(row=0, column=1)
        cancel_button.grid(row=0, column=2)
        new_frame.grid(row=index, column=0)
