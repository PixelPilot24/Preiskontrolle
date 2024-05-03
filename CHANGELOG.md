# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.


## [0.5.0] - 03.05.2024
### Changed
+ [checkData.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.5.0/src/checkData.py)
  + in [check_new_price()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.5.0/src/checkData.py#117) neue Kondition
  hinzugefügt da der neue Preis erst dann angezeigt wurde, wenn es mehr als 1 % ist aber nicht weniger

## [0.4.0] - 29.04.2024
### Added
+ README.md
+ Dokumentationen

### Changed
+ [delete.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/delete.py) umbenannt zu 
[dataGUI.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.4.0/src/dataGUI.py)
  + [DeleteData](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/delete.py#L11) Klasse umbenannt in
  [DataGUI](https://github.com/PixelPilot24/Preiskontrolle/blob/0.4.0/src/dataGUI.py#L11)

## [0.3.0] - 09.04.2024

### Added
+ [edit.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/edit.py) Bearbeitung
  + [rename()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/edit.py#L51) tauscht den Text gegen
  ein Eingabefeld und zwei Buttons für speichern und abbrechen
  + [cancel_method()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/edit.py#L39): das Eingabefeld
  wird wieder zurück in den Text umgewandelt
  + [save_method()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/edit.py#L7) speichert die
  Datei mit dem neuen Namen ab

### Changed
+ [delete.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/delete.py)
  + in der [delete_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/delete.py#L28) wurde
  die Farbe des Textes des Namens geändert und eine Methode hinzugefügt zum Ändern des Namens 
  [name_clicked()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/delete.py#L49)
+ [create.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/create.py)
  + in der [save_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.3.0/src/create.py#L61) wurde
  hinzugefügt das, nachdem der speichern Knopf betätigt wurde, das Feld für den Namen und die URL wieder 
  leer werden


## [0.2.0] - 08.04.2024

### Added
+ [create.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py) neues Produkt erstellen
  + [create_widgets()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L23) erstellt
  die benötigten Widgets
  + [check_url()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L41) überprüft, ob
  die URL zu alternate oder galaxus gehört. Falls nicht, dann ist die Ausgabe "error"
  + [check_and_save_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L49),
  speichert den neuen Preis ab
  + [save_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L61) führt die
  Speicherung der Datei im Hintergrund aus
+ [delete.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py)
  + [create_data_list()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py#L68) erstellt
  eine Liste mit den Namen und dem aktuellen Preis
  + [on_mouse_wheel](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py#L65) Methode für
  das scrollen der Liste
  + [create_scrollbar()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py#L56) erstellt
  eine horizontale und vertikale Scrollbar
  + [create_label_and_button()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py#L23)
  erstellt zwei Buttons für das Löschen und die Seite besuchen. Außerdem noch die Labels für den Namen und den
  Preis
+ [autostart.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/autostart.py) Datei für das
automatische Starten des Programms beim Hochfahren des Computers
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py)
  + [loading_progress()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py#L86)
  das ausgelagerte überprüfen und hinzufügen von [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/main.py).
  Ein Ladebalken der anzeigt wie weit die Daten überprüft wurden

### Changed
+ [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/main.py)
  + [load_json()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/main.py#L30) autostart bool
  hinzugefügt und das Überprüfen und hinzufügen der Preise nach 
  [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py#L99) ausgelagert
+ [checkData.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/checkData.py)
  + [check_data_alternate()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/checkData.py#L9)
  try except hinzugefügt, die Preissuche überarbeitet und bei Fehlern gibt der return -1 wieder
  + [check_data_galaxus()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/checkData.py#L26)
  try except hinzugefügt, die Preissuche überarbeitet und bei Fehlern gibt der return -1 wieder
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py)
  + root = Tk() -> [self.root = Tk()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py#L15)
  + die Fenstererstellung von init auf die [create_window()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/notification.py#L17)
  Methode umgestellt

### Removed
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py)
  + [new_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L77) leere Methode
  (Platzhalter)
  + [created_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L80) leere Methode
  (Platzhalter)
  + [check_new_price()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L83) leere Methode
  (Platzhalter)
+ [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/main.py)
  + [init()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/main.py#L11) gelöscht, weil die Funktion
  load_json() jetzt direkt von der main() ausgeführt wird


## [0.1.0] - 04.04.2024

### Added
+ [data.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/data.py)
  + Data Klasse erstellt
+ [checkData.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py)
  + [amount_in_euro()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py#L54) Methode
  um gegebenenfalls eine Null am Ende der Zahl hinzuzufügen, den Punkt in ein Komma umzuwandeln und ein Euro
  Zeichen anzuhängen
  + [calculate_percent()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py#L61)
  berechnet den Prozentwert und gibt ihn mit dem Prozentzeichen am Ende aus
  + [check_new_price()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py#L67)
  überprüft, ob es einen älteren Eintrag gibt und wenn ja, dann werden die Daten für die Benachrichtigung 
  ausgegeben
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py)
  + [create_treeview()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L22)
  es wird eine Tabelle mit den Daten erstellt
  + [create_menubar()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L62)
  erstellt die Menübar

### Changed
+ [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/main.py)
  + [load_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/main.py#L33) öffnet erst dann
  ein Fenster, wenn der Preis sich verändert hat
+ [checkData.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py)
  + [check_data_galaxus()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/checkData.py#L33),
  gibt den richtigen Preis wieder
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py)
  + [GUI](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.0/src/notification.py#L7) angepasst und 
  in Methoden ausgelagert


## [0.0.2] - 03.04.2024

### Added
+ [notification.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/notification.py)
  + [GUI](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/notification.py#L7)
  + [open_webpage()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/notification.py#L31)
  zum Öffnen vom Link, falls es einen günstigeren Preis gibt
+ [checkData.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/checkData.py)
  + [check_data_alternate()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/checkData.py#L7) 
  und [check_data_galaxus()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/checkData.py#L31) von main.py verschoben
+ [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/main.py)
  + [save_json()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/main.py#L26) 
  um die Daten in JSON abzuspeichern
  + [insert_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/main.py#L31) 
  um das Datum und den Preis in die Dictionary zu speichern
  + [load_data()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.0.2/src/main.py#L44) die Daten werden geladen und, falls keine existieren, dann soll eine erstellt werden


## [0.0.1] - 02.04.2024

### Added
+ main.py
  + es ist möglich von den Webseiten alternate.de und galaxus.de den Preis von Waren aufzurufen