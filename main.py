import sys
import resources
import folio

import PySide2 as ps2

if __name__=="__main__":
    app = ps2.QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(ps2.QtGui.QIcon(":/default.png"));

    window = folio.Folio()
    window.show()

    sys.exit(app.exec_())
