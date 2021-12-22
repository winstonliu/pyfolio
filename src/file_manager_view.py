import PySide2 as ps2

class FileManagerView(ps2.QtWidgets.QTreeView):
    def mousePressEvent(self, event):
        self.clearSelection()
        super().mousePressEvent(event)
