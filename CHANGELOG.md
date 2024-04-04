# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

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