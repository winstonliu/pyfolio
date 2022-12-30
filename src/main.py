import sys
import resources
import folio

import PySide6 as ps6

if __name__=="__main__":
    app = ps6.QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(ps6.QtGui.QIcon(":/default.png"));

    window = folio.Folio()
    window.show()

    sys.exit(app.exec_())
