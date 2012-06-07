# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Jun 07 02:34:48 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listWidgetRss = QtGui.QListWidget(self.centralwidget)
        self.listWidgetRss.setGeometry(QtCore.QRect(0, 0, 791, 401))
        self.listWidgetRss.setObjectName(_fromUtf8("listWidgetRss"))
        self.lineEditUrl = QtGui.QLineEdit(self.centralwidget)
        self.lineEditUrl.setGeometry(QtCore.QRect(10, 450, 161, 20))
        self.lineEditUrl.setObjectName(_fromUtf8("lineEditUrl"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 430, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushAddButton = QtGui.QPushButton(self.centralwidget)
        self.pushAddButton.setGeometry(QtCore.QRect(180, 450, 75, 23))
        self.pushAddButton.setObjectName(_fromUtf8("pushAddButton"))
        self.listWidgetUrls = QtGui.QListWidget(self.centralwidget)
        self.listWidgetUrls.setGeometry(QtCore.QRect(10, 480, 291, 71))
        self.listWidgetUrls.setObjectName(_fromUtf8("listWidgetUrls"))
        self.pushRefreshButton = QtGui.QPushButton(self.centralwidget)
        self.pushRefreshButton.setGeometry(QtCore.QRect(690, 440, 75, 23))
        self.pushRefreshButton.setObjectName(_fromUtf8("pushRefreshButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave_Url_List = QtGui.QAction(MainWindow)
        self.actionSave_Url_List.setObjectName(_fromUtf8("actionSave_Url_List"))
        self.actionLoad_Url_List = QtGui.QAction(MainWindow)
        self.actionLoad_Url_List.setObjectName(_fromUtf8("actionLoad_Url_List"))
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addAction(self.actionSave_Url_List)
        self.menuMenu.addAction(self.actionLoad_Url_List)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "RSS url to add to monitoring:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAddButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRefreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Url_List.setText(QtGui.QApplication.translate("MainWindow", "Save Url List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Url_List.setText(QtGui.QApplication.translate("MainWindow", "Load Url List", None, QtGui.QApplication.UnicodeUTF8))

