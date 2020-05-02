# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'folio.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Folio(object):
    def setupUi(self, Folio):
        if not Folio.objectName():
            Folio.setObjectName(u"Folio")
        Folio.resize(536, 391)
        Folio.setContextMenuPolicy(Qt.CustomContextMenu)
        self.actionExit = QAction(Folio)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSettings = QAction(Folio)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(Folio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(False)
        self.treeView.setExpandsOnDoubleClick(True)

        self.horizontalLayout.addWidget(self.treeView)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.textEdit.setLineWrapColumnOrWidth(80)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        Folio.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Folio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 536, 21))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        Folio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Folio)
        self.statusbar.setObjectName(u"statusbar")
        Folio.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionExit)

        self.retranslateUi(Folio)

        QMetaObject.connectSlotsByName(Folio)
    # setupUi

    def retranslateUi(self, Folio):
        Folio.setWindowTitle(QCoreApplication.translate("Folio", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("Folio", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Folio", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionSettings.setText(QCoreApplication.translate("Folio", u"Settings", None))
        self.menuSettings.setTitle(QCoreApplication.translate("Folio", u"File", None))
    # retranslateUi

