@echo off
pyside2-uic folio.ui > ui_folio.py
pyside2-uic settings.ui > ui_settings.py
pyside2-rcc -o resources.py resources.qrc
pyinstaller --onefile --icon=icons\icon.ico -w -n folio main.py
