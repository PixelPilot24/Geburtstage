# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

## [0.2.0] - 22.04.2024

### Added
+ [check.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/check.py)
Datei wo der eingegebene Geburtstag überprüft wird
  + [calculate_age()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/check.py#L81) 
  Berechnung vom Alter
  + [save_in_json()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/check.py#L92)
  speicherung der Daten in JSON

### Changed
+ [create.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py)
  + aus der [init(self)](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L16) 
  wurde die Erstellung der Widgets in die
  [create_widgets()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L30) und 
  [create_menubar()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py#L49) Methode verschoben
  + [check_year()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L84) und
  [check_int_len()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L30) wurden nach
  [check.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/check.py) verschoben
  + in [birthday_save()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L61) wird,
  wenn erfolgreich gespeichert oder der Name vergessen wurde, eine Messagebox angezeigt
+ [main.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/main.py)
  + Attribute an die neuen Klassen angepasst
+ aus [delete.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/delete.py) wurde 
[createDataWindow.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/createDataWindow.py)
  + die Klasse [Delete](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/delete.py#L7) wurde
  in die Klassen [CreateDataWindow](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/delete.py#L7)
  und [DataHandler](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/delete.py#L80) aufgeteilt

### Deleted
+ [create.py](https://github.com/PixelPilot24/Preiskontrolle/blob/0.2.0/src/create.py)
  + [birthdays_list()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L64)
  + [close_program()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L71)
  + [error_text()](https://github.com/PixelPilot24/Preiskontrolle/blob/0.1.1/src/create.py#L77)


## [0.1.1] - 30.03.2024

### Added
+ autostart.py
+ Dokumentationen in main.py, create.py, delete.py

### Changed
+ in allen Dateien bei den Methoden die Parameter benötigen, wurden die Datentypen hinzugefügt.
+ README.md angepasst


## [0.1.0] - 30.03.2024

### Added
+ delete.py
  + init()
  + create_window() Methode in die create_list() umbenannt()
  + calculate_age()
  + format_date() von YYYY-MM-DD zu DD.MM.YYYY
  + remove_birthday() zum Löschen von Geburtstagen
+ create.py
  + check_birthday() überprüft und benachrichtigt gleichzeitig

### Changed
+ create.py, delete.py, main.py in den "src" Ordner verschoben

### Removed
+ create.py
  + create_birthday(self)
  + notification(name)


## [0.0.2] - 28.03.2024

### Added
+ create.py
  + birthdays_list() Methode zum Anzeigen und löschen der Geburtstage
  + close_program() Methode fürs Schließen des Programms
  + Menüleiste mit "Geburtstage löschen" und "Schließen" erstellt
+ delete.py
  + Delete class
    + create_window() Methode zum Erstellen eines Fensters zum Anzeigen oder löschen der Geburtstage

### Changed
+ create.py
  + die days Liste von int auf String umgestellt
  + die Größe des Fensters angepasst
  + von den Tagen und den Monaten OptionMenu durch Combobox ersetzt
  + die pack Methode bei den Elementen durch place ersetzt


## [0.0.1] - 26.03.2024

### Added
+ main.py erstellt
  + JSON Datei wird erstellt
  + JSON Datei wird ausgelesen
+ create.py erstellt
  + GUI erstellt
  + speicherung vom Namen und Geburtstag
  + Fehlertext hinzugefügt
+ delete.py erstellt