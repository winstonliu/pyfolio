import PySide6 as ps6

class FileManagerView(ps6.QtWidgets.QTreeView):
    def mousePressEvent(self, event):
        self.clearSelection()
        self.setCurrentIndex(self.rootIndex())
        super().mousePressEvent(event)
