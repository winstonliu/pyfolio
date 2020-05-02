import PySide2 as ps2
from ui_folio import Ui_Folio

class Folio(ps2.QtWidgets.QMainWindow):
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

        # This allows us to avoid calling all connects manually
        ps2.QtCore.QMetaObject.connectSlotsByName(self)


    def setup_tree_view(self, root_path):
        """ Setup the tree view panel. """
        # Set tree model
        model = ps2.QtWidgets.QFileSystemModel()
        model.setRootPath(root_path)
        # TODO move filters list to settings
        model.setNameFilters(["*.txt", "*.markdown"])

        # Initialize tree view
        tree_view = self.ui.treeView
        tree_view.setModel(model)
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


    @ps2.QtCore.Slot(ps2.QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        if not index:
            return;
        
        # Get the file 
        target = self.model.fileInfo(index)
        if not self.check_validity(target):
            return;

        # Read file
        read_file = ps2.QtCore.QFile(target.absoluteFilePath())
        if not read_file.open(ps2.QtCore.QFile.ReadOnly or
                ps2.QtCore.QFile.Text):
            return;

        # Clear preview window
        self.ui.textEdit.clear(); 
        stream = ps2.QtCore.QTextStream(read_file)
        while not stream.atEnd():
            self.ui.textEdit.append(stream.readLine())


    def on_actionSettings_triggered(self):
        pass


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
