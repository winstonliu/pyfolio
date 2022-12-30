import PySide6 as ps6

TEXT_FORMAT_LIST = [
        "Markdown",
        "Plain Text",
]

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
        self.text_edit.setWordWrapMode(ps6.QtGui.QTextOption.WordWrap)

        # File watcher object
        self.file_watcher = ps6.QtCore.QFileSystemWatcher()

        # Setup connections
        self.file_watcher.fileChanged.connect(self.on_fileChanged)
        self.text_edit.anchorClicked.connect(self.on_anchorClicked)


    def on_fileChanged(self):
        # set watcher to watch the current file
        if not self.file_path in self.file_watcher.files():
            self.file_watcher.addPath(self.file_path.absoluteFilePath())

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
        file_handle = ps6.QtCore.QFile(file_path.absoluteFilePath())
        if not file_handle.open(ps6.QtCore.QFile.ReadOnly | ps6.QtCore.QFile.Text):
            return False

        self.text_edit.clear()
        stream = ps6.QtCore.QTextStream(file_handle)
        text = stream.readAll()

        if display_format == TEXT_FORMAT_LIST[0]:
            self.text_edit.setMarkdown(text)
        elif display_format == TEXT_FORMAT_LIST[1]:
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

