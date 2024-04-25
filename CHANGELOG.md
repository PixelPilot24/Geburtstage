# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.


## [2.1.0] - 25.04.2024
### Added
+ [search.py](https://github.com/PixelPilot24/Geburtstage/blob/2.1.0/src/search.py)
  + Suchfunktion um in der Geburtstagsliste nach bestimmten Namen zu suchen

### Changed
+ [createDataWindow.py](https://github.com/PixelPilot24/Geburtstage/blob/2.1.0/src/createDataWindow.py)
  + die Attribute [__search_frame](https://github.com/PixelPilot24/Geburtstage/blob/2.1.0/src/createDataWindow.py#L15)
  und [__widget_frame](https://github.com/PixelPilot24/Geburtstage/blob/2.1.0/src/createDataWindow.py#L16) erstellt um
  die Widgets und die Suche zu trennen
  + in [__save_change](https://github.com/PixelPilot24/Geburtstage/blob/2.1.0/src/createDataWindow.py#L154) eine Methode,
  für die Löschung des alten Namen nach der Bearbeitung, hinzugefügt

## [2.0.0] - 25.04.2024
### Changed
+ es wird jetzt anstatt das Erstellen des Geburtstages, die Liste mit den Geburtstagen als erstes Fenster angezeigt
+ [createDataWindow.py](https://github.com/PixelPilot24/Geburtstage/blob/2.0.0/src/createDataWindow.py)
  + [create_widgets()](https://github.com/PixelPilot24/Geburtstage/blob/2.0.0/src/createDataWindow.py#L83) wurde aus
  der Klasse herausgenommen, da nach dem Löschen und dem Erstellen eines Geburtstages die Widgets erneut erstellt werden
  + die Menübar wird in
  [create_widgets()](https://github.com/PixelPilot24/Geburtstage/blob/2.0.0/src/createDataWindow.py#L69) erstellt
  + in [__resize_window()](https://github.com/PixelPilot24/Geburtstage/blob/2.0.0/src/createDataWindow.py#L61) wurde
  ein If Statement eingefügt, falls es weniger als 3 Daten gibt, dann wird eine bestimmte Größe vom Fenster erzeugt
+ [create.py](https://github.com/PixelPilot24/Geburtstage/blob/2.0.0/src/create.py) angepasst, anstatt das in der init
ein Tk() erstellt wird, wird ein Toplevel erstellt
  + alle Attribute und Methoden wurden auf private gestellt


## [1.0.0] - 24.04.2024
### Added
+ [json_handler.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/json_handler.py) in der Datei wird die
JSON Datei gespeichert und aufgerufen

### Changed
+ die Klassen in [createDataWindow.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/createDataWindow.py)
überarbeitet und anders verteilt
+ [validator.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/validator.py)
  + [save_in_json()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py#L107) wurde nach
  [json_handler.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/json_handler.py#L10) verschoben
+ [main.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/main.py)
  + [open_window()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/main.py#L47) zu
  [run()](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/main.py#L47) geändert
  + [load_dates()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/main.py#L54) nach
  [json_handler.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/json_handler.pyL#15) verschoben und wurde
  in load_json_file umbenannt
+ [autostart.py](https://github.com/PixelPilot24/Geburtstage/blob/1.0.0/src/autostart.py#L4) angepasst

## [0.3.0] - 22.04.2024
### Added
+ [validator.py](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py)
  + [check_input()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py#L10) überprüft, ob
  die Eingabe für den Tag, Monat und Jahr Zahlen benutzt wurden und ob die maximale Länge nicht überschritten
  wurde
+ [create.py](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/create.py)
  + in [create_widgets()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/create.py#L29) wurden die Entrys
  für den Tag, Monat und Jahr mit der
  [check_input()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py#L10) Methode verknüpft

### Changed
+ [check.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/check.py) wurde zu
[validator.py](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py)
  + die Klasse [CheckData](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/validator.py#L8) wurde zu
  [DataValidator](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/validator.py#L8) umbenannt
  + [calculate_age()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py#L96) und
  [save_in_json()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/validator.py#L107) wurden in
  die Klasse [DataValidator](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/validator.py#L8)
  mitaufgenommen
+ [createDataWindow.py](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/createDataWindow.py)
  + in [__save_change()](https://github.com/PixelPilot24/Geburtstage/blob/0.3.0/src/createDataWindow.py#L104)
  wurde eine if Abfrage hinzugefügt um zu überprüfen, ob die eingegebenen Werte korrekt sind

## [0.2.0] - 22.04.2024

### Added
+ [check.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/check.py)
Datei wo der eingegebene Geburtstag überprüft wird
  + [calculate_age()](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/check.py#L81) 
  Berechnung vom Alter
  + [save_in_json()](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/check.py#L92)
  speicherung der Daten in JSON

### Changed
+ [create.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/create.py)
  + aus der [init(self)](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L16) 
  wurde die Erstellung der Widgets in die
  [create_widgets()](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/create.py#L30) und 
  [create_menubar()](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/create.py#L49) Methode verschoben
  + [check_year()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L84) und
  [check_int_len()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L30) wurden nach
  [check.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/check.py) verschoben
  + in [birthday_save()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L61) wird,
  wenn erfolgreich gespeichert oder der Name vergessen wurde, eine Messagebox angezeigt
+ [main.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/main.py)
  + Attribute an die neuen Klassen angepasst
+ aus [delete.py](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/delete.py) wurde 
[createDataWindow.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/createDataWindow.py)
  + die Klasse [Delete](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/delete.py#L7) wurde
  in die Klassen [CreateDataWindow](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/delete.py#L7)
  und [DataHandler](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/delete.py#L80) aufgeteilt

### Deleted
+ [create.py](https://github.com/PixelPilot24/Geburtstage/blob/0.2.0/src/create.py)
  + [birthdays_list()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L64)
  + [close_program()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L71)
  + [error_text()](https://github.com/PixelPilot24/Geburtstage/blob/0.1.1/src/create.py#L77)


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