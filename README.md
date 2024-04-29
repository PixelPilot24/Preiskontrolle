# Preiskontrolle

## Inhaltsverzeichnis

1. [Beschreibung](#beschreibung)
2. [Verwendung](#verwendung)
3. [Voraussetzung](#voraussetzung)
   + [requests](#requests)
   + [BeautifulSoup4](#BeautifulSoup4)
4. [Autor](#autor)
5. [Lizenz](#lizenz)


## Beschreibung

Mit dieser Anwendung werden Produkte von den Seiten [alternate](https://www.alternate.de/) und
[galaxus](https://www.galaxus.de/) abgefragt und überprüft, ob der Preis gesunken, gestiegen oder gleich geblieben ist.


## Verwendung

Nach dem Starten der main.py Datei werden, falls es schon Produkte gibt, die Produkte überprüft, ob es seit der letzten 
Überprüfung einen neuen Preis gibt. Falls es noch keine Produkte gibt, dann können diese in der Menüleiste "Datei" 
unter "Neue Datei" erstellt werden. Unter "Erstelle Daten" ist es möglich alle Produkte anzusehen, die Namen zu ändern,
die Seite zu besuchen oder das Produkt zu löschen.

## Voraussetzung
+ requests
+ BeautifulSoup4

### requests
Die requests Bibliothek wird für die HTTP Anfragen genutzt, um mit den Websites zu kommunizieren.

Den folgenden Befehl in der Kommandozeile ausführen
```shell
pip install requests
```

Die Ausgabe sollte folgende sein (Stand 29.04.2024):
````shell
...
Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Installing collected packages: requests
Successfully installed requests-2.31.0
````

### BeautifulSoup4
Die BeautifulSoup4 Bibliothek wird für das durchsuchen und analysieren von Webseiteninhalten genutzt.

Den folgenden Befehl in der Kommandozeile ausführen
````shell
pip install BeautifulSoup4
````
Die Ausgabe sollte folgende sein (Stand 29.04.2024):
````shell
...
Using cached beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
Installing collected packages: BeautifulSoup4
Successfully installed BeautifulSoup4-4.12.3
````

## Autor
[![GitHub Badge](https://img.shields.io/badge/PixelPilot24-Profile-darkgreen?style=flat&logo=github)](https://github.com/PixelPilot24)

## Lizenz
[MIT](https://choosealicense.com/licenses/mit/)