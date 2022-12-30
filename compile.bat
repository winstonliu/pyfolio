@echo off
set SOURCE_FOLDER=src

rem TODO split out generated files into a separate folder
pyside6-uic %SOURCE_FOLDER%\folio.ui > %SOURCE_FOLDER%\ui_folio.py
pyside6-uic %SOURCE_FOLDER%\settings.ui > %SOURCE_FOLDER%\ui_settings.py
pyside6-rcc -o %SOURCE_FOLDER%\resources.py resources.qrc
echo Completed file translation ...

rem Skip exe generation if the /s flag is passed
if "%1" == "/s" (
    echo Skipping exe generation!
) else (
    pyinstaller --onefile --icon=icons\icon.ico -w -n folio %SOURCE_FOLDER%\main.py
)

