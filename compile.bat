@echo off
pyside2-uic folio.ui > ui_folio.py
pyside2-uic settings.ui > ui_settings.py
pyside2-rcc -o resources.py resources.qrc
echo Completed file translation ...

rem Skip exe generation if the /s flag is passed
if "%1" == "/s" (
    echo Skipping exe generation!
) else (
    pyinstaller --onefile --icon=icons\icon.ico -w -n folio main.py
)

