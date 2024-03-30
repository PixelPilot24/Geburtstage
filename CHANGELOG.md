# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

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