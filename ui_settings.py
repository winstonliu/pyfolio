# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(491, 139)
        Settings.setMinimumSize(QSize(491, 139))
        Settings.setMaximumSize(QSize(491, 139))
        self.gridLayoutWidget = QWidget(Settings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 471, 80))
        self.settingsLayout = QGridLayout(self.gridLayoutWidget)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setContentsMargins(0, 0, 0, 0)
        self.change_rootFolder = QPushButton(self.gridLayoutWidget)
        self.change_rootFolder.setObjectName(u"change_rootFolder")

        self.settingsLayout.addWidget(self.change_rootFolder, 0, 2, 1, 1)

        self.executablePathEntry = QLineEdit(self.gridLayoutWidget)
        self.executablePathEntry.setObjectName(u"executablePathEntry")

        self.settingsLayout.addWidget(self.executablePathEntry, 1, 1, 1, 1)

        self.change_executablePath = QPushButton(self.gridLayoutWidget)
        self.change_executablePath.setObjectName(u"change_executablePath")

        self.settingsLayout.addWidget(self.change_executablePath, 1, 2, 1, 1)

        self.rootFolderEntry = QLineEdit(self.gridLayoutWidget)
        self.rootFolderEntry.setObjectName(u"rootFolderEntry")

        self.settingsLayout.addWidget(self.rootFolderEntry, 0, 1, 1, 1)

        self.label_treeViewRootFolder = QLabel(self.gridLayoutWidget)
        self.label_treeViewRootFolder.setObjectName(u"label_treeViewRootFolder")

        self.settingsLayout.addWidget(self.label_treeViewRootFolder, 0, 0, 1, 1)

        self.label_executablePath = QLabel(self.gridLayoutWidget)
        self.label_executablePath.setObjectName(u"label_executablePath")

        self.settingsLayout.addWidget(self.label_executablePath, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(320, 100, 156, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Settings)
        self.buttonBox.rejected.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Dialog", None))
        self.change_rootFolder.setText(QCoreApplication.translate("Settings", u"Change...", None))
        self.change_executablePath.setText(QCoreApplication.translate("Settings", u"Change...", None))
        self.label_treeViewRootFolder.setText(QCoreApplication.translate("Settings", u"Tree view root folder:", None))
        self.label_executablePath.setText(QCoreApplication.translate("Settings", u"Text editor executable path:", None))
    # retranslateUi

