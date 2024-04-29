from tkinter import *
from data import Data


class EditName:
    """
    In dieser Klasse wird der Name von einem Produkt geändert.
    """
    @classmethod
    def save_method(cls, site: str, old_name: str, new_name: str, edit_frame: Frame, label_frame: Frame,
                    color: str, index: int, label_width: int):
        """
        Speichert die Änderungen an einem Datensatz, indem der alte Name durch den neuen ersetzt wird.

        :param site: Der Name der Webseite, auf der die Änderungen vorgenommen werden.
        :param old_name: Der alte Name des Datensatzes.
        :param new_name: Der neue Name der den alten Namen ersetzt.
        :param edit_frame: Das Frame, das den Editiermodus enthält.
        :param label_frame: Das Frame, das das Label für den Datensatz enthält.
        :param color: Die Hintergrundfarbe des Labels.
        :param index: Der Index des Datensatzes.
        :param label_width: Die Breite des Labels.
        """
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
        cls.cancel_method(edit_frame, label_frame, new_name, color, index, site, label_width)

    @staticmethod
    def cancel_method(edit_frame: Frame, label_frame: Frame, name: str, color: str, index: int, site: str,
                      label_width: int):
        """
         Beendet den Editiermodus und zeigt den Datensatz mit dem alten Namen an.

        :param edit_frame: Das Frame des Editiermodus.
        :param label_frame: Das Frame, das das Label für den Datensatz enthält.
        :param name: Der Name des Datensatzes.
        :param color: Die Hintergrundfarbe des Labels.
        :param index: Der Index des Datensatzes.
        :param site: Der Name der Webseite.
        :param label_width: Die Breite des Labels.
        """
        edit_frame.destroy()
        name_label = Label(master=label_frame, text=name, pady=5, padx=5, bg=color, fg="blue", width=label_width)

        def name_clicked(event):
            EditName.rename(name_label, label_frame, index, name, color, site, label_width)

        name_label.grid(row=index, column=0)
        name_label.bind("<Button-1>", name_clicked)

    @classmethod
    def rename(cls, name_label: Label, frame: Frame, index: int, name: str, color: str, site: str, label_width: int):
        """
        Ändert den Datensatznamen im Editiermodus.

        :param name_label: Das Label des Datensatzes.
        :param frame: Das Frame, in dem die Änderungen vorgenommen werden.
        :param index: Der Index des Datensatzes.
        :param name: Der aktuelle Name des Datensatzes.
        :param color: Die Hintergrundfarbe des Labels.
        :param site: Der Name der Webseite.
        :param label_width: Die Breite des Labels.
        """
        new_frame = Frame(master=frame)
        name_label.destroy()

        name_entry = Entry(master=new_frame, width=label_width)
        save_button = Button(master=new_frame, text="\u2713")
        cancel_button = Button(master=new_frame, text="\u2718")

        save_button.config(
            command=lambda: cls.save_method(site, name, name_entry.get(), new_frame, frame, color, index, label_width))
        cancel_button.config(command=lambda: cls.cancel_method(new_frame, frame, name, color, index, site, label_width))
        name_entry.insert(0, name)

        name_entry.grid(row=0, column=0)
        save_button.grid(row=0, column=1)
        cancel_button.grid(row=0, column=2)
        new_frame.grid(row=index, column=0)
