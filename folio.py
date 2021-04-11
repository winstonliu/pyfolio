import PySide2 as ps2
from ui_folio import Ui_Folio
from settings import SettingsDialog


class TextViewer():
    """
    @class
    Helper class to contain text viewer information.
    """
    def __init__(self, text_edit):
        self.text_edit = text_edit
        self.__file_path = None
        self.display_format = None

        # Set text edit to wrap on word-breaks only
        self.text_edit.setWordWrapMode(ps2.QtGui.QTextOption.WordWrap)

        # File watcher object
        self.file_watcher = ps2.QtCore.QFileSystemWatcher()

        # Setup connections
        self.file_watcher.fileChanged.connect(self.on_fileChanged)
        self.text_edit.anchorClicked.connect(self.on_anchorClicked)

    def on_fileChanged(self):
        # Reload file
        self.load_file(self.file_path, self.display_format)

    def on_anchorClicked(self, link):
        # Get string
        url = link.url()
        # Check that it's actually an anchor
        if url.startswith("#"):
            self.text_edit.scrollToAnchor(url)

    @property
    def file_path(self):
        return self.__file_path


    @file_path.setter
    def file_path(self, new_path):
        # Try to delete the file_path from the file watcher if it exists
        if self.__file_path:
            self.file_watcher.removePath(self.__file_path.absoluteFilePath())

        self.__file_path = new_path 


    def load_file(self, file_path, display_format):
        file_handle = ps2.QtCore.QFile(file_path.absoluteFilePath())
        if not file_handle.open(ps2.QtCore.QFile.ReadOnly | ps2.QtCore.QFile.Text):
            return False

        self.text_edit.clear()
        stream = ps2.QtCore.QTextStream(file_handle)
        text = stream.readAll()

        if display_format == Folio.TEXT_FORMAT_LIST[0]:
            self.text_edit.setMarkdown(text)
        elif display_format == Folio.TEXT_FORMAT_LIST[1]:
            self.text_edit.setPlainText(text)

        return True


    def show(self, display_format, file_path=None):
        # Either set the file path if it's not none, or use current file path
        if file_path:
            # Update the file path
            self.file_path = file_path 
        else:
            if self.file_path:
                file_path = self.file_path
            else:
                return;
        self.display_format = display_format

        if not self.load_file(file_path, self.display_format):
            # Clear the file path so we don't try to use it again
            self.file_path = None
            return;

        # Add path to file watcher
        self.file_watcher.addPath(self.file_path.absoluteFilePath())


class Folio(ps2.QtWidgets.QMainWindow):

    TEXT_FORMAT_LIST = [
            "Markdown",
            "Plain Text",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Folio()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Folio - for Organized Writers")

        # Set the names for the on-drive storage
        self.organization = "winstonliu"
        self.program = "folio"

        # Set configuration settings
        settings = ps2.QtCore.QSettings(self.organization, self.program)
        self.root_path = settings.value("config/rootFolderPath")
        self.exe_path = settings.value("config/executablePath")
        self.restoreGeometry(settings.value("window/geometry"))
        self.restoreState(settings.value("window/state"))

        self.model = self.setup_tree_view(self.root_path)
        self.ui.textFormatComboBox.insertItems(0, Folio.TEXT_FORMAT_LIST)

        # Set up custom objects
        self.text_viewer = TextViewer(self.ui.textBrowser)

        self.setup_connections()


    def setup_connections(self):
        """ @brief Setup connections between slots and signals
            Not using connectSlotsByName as I can't figure out how to stop it
            from double-triggering all the connections
        """
        self.ui.treeView.clicked.connect(self.on_treeView_clicked) 
        self.ui.treeView.doubleClicked.connect(self.on_treeView_doubleClicked) 
        self.ui.actionSettings.triggered.connect(self.on_actionSettings_triggered)
        self.ui.actionExit.triggered.connect(self.on_actionExit_triggered)
        self.ui.textFormatComboBox.currentIndexChanged.connect(self.on_textFormatComboBox_currentIndexChanged)


    def setup_tree_view(self, root_path):
        """ Setup the tree view panel. """
        # Set tree model
        model = ps2.QtWidgets.QFileSystemModel()
        model.setRootPath("")
        # TODO move filters list to settings
        model.setNameFilters(["*.txt", "*.markdown"])

        # Initialize tree view
        tree_view = self.ui.treeView
        tree_view.setModel(model)
        tree_view.setRootIndex(model.index(root_path))
        tree_view.setIndentation(20)
        tree_view.setWindowTitle("Dir View")

        # Set the tree view header resizing settings
        tree_view.header().setSectionResizeMode(ps2.QtWidgets.QHeaderView.ResizeToContents)

        return model


    def check_validity(self, target):
        # Check if a file is filtered
        filter_list = target.absoluteDir().entryList(self.model.nameFilters())
        return (target.fileName() in filter_list and target.exists() and
                target.isFile() and target.isReadable())


    def on_treeView_clicked(self, index):
        if not index:
            return;
        
        # Get the file 
        target = self.model.fileInfo(index)
        if not self.check_validity(target):
            return;

        # Read file
        self.text_viewer.show(self.ui.textFormatComboBox.currentText(), target)


    def on_treeView_doubleClicked(self, index):
        if not index:
            return;
        
        target = self.model.fileInfo(index)
        if not self.check_validity(target):
            return;

        process = ps2.QtCore.QProcess()
        process.setWorkingDirectory(target.absoluteDir().absolutePath())
        process.setProgram(self.exe_path)
        process.setArguments({target.absoluteFilePath()})
        process.startDetached()


    def on_textFormatComboBox_currentIndexChanged(self, index):
        self.text_viewer.show(self.ui.textFormatComboBox.currentText())


    def on_actionSettings_triggered(self):
        settings = SettingsDialog(self.root_path, self.exe_path, self)
        if settings.exec_() == ps2.QtWidgets.QDialog.Accepted:
            # Update tree view
            self.ui.treeView.setRootIndex(self.model.index(settings.root_path))
            self.exe_path = settings.exe_path


    def on_actionExit_triggered(self):
        self.close()


    def closeEvent(self, event):
        """ Save settings on close. """
        # Save settings
        settings = ps2.QtCore.QSettings(self.organization, self.program)
        settings.setValue("config/rootFolderPath", self.root_path)
        settings.setValue("config/executablePath", self.exe_path)
        settings.setValue("window/geometry", self.saveGeometry())
        settings.setValue("window/state", self.saveState())
        settings.sync()

        event.accept()
