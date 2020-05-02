import PySide2 as ps2
from ui_settings import Ui_Settings

class Settings(ps2.QtWidgets.QtDialog):
    def __init__(self, root_folder_path, executable_path, parent):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.root_folder_path = root_folder_path
        self.executable_path = executable_path

        # Set text fields
        self.ui.rootFolderEntry.setText(self.root_folder_path)
        self.ui.executablePathEntry.setText(self.executable_path)

