import PySide6 as ps6
from PySide6.QtCore import QStandardPaths, QFileInfo
from PySide6.QtWidgets import QFileDialog, QMessageBox
from ui_settings import Ui_Settings

class SettingsDialog(ps6.QtWidgets.QDialog):
    def __init__(self, root_folder_path, executable_path, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.root_path = root_folder_path
        self.exe_path = executable_path

        # Initialize the contents of the settings box
        self.ui.rootFolderEntry.setText(self.root_path)
        self.ui.executablePathEntry.setText(self.exe_path)

        self.setup_connections()


    def setup_connections(self):
        self.ui.change_rootFolder.clicked.connect(self.on_change_rootFolder_clicked)
        self.ui.change_executablePath.clicked.connect(self.on_change_executablePath_clicked)
        self.ui.buttonBox.accepted.connect(self.on_buttonBox_accepted)


    def on_change_rootFolder_clicked(self):
        root_path = QFileDialog.getExistingDirectory(self, 
                "Select Root Folder", 
                QStandardPaths.writableLocation(QStandardPaths.HomeLocation), 
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

        if root_path:
            self.ui.rootFolderEntry.setText(root_path)


    def on_change_executablePath_clicked(self):
        exe_path = QFileDialog.getOpenFileName(
                self, 
                "Select Text Editor",
                QStandardPaths.writableLocation(
                    QStandardPaths.ApplicationsLocation),
                    "Executables (*.bat *.exe)")

        if exe_path:
            self.ui.executablePathEntry.setText(exe_path)


    def on_buttonBox_accepted(self):
        """ Check that the text is either a valid path or empty """
        root_path = self.ui.rootFolderEntry.text()
        exe_path = self.ui.executablePathEntry.text()

        # Check if the root_path is valid
        message_box = QMessageBox()
        if not (QFileInfo(root_path).isDir() or root_path.isEmpty()):
            message_box.critical(self, "Error", "Root folder path is invalid!")
            return;

        if not (QFileInfo(exe_path).isExecutable() or exe_path.isEmpty()):
            message_box.critical(self, "Error", "Root folder path is invalid!")
            return;

        # Update paths
        self.root_path = root_path 
        self.exe_path = exe_path

        # Otherwise the fields are correct and we can accept
        self.accept()
