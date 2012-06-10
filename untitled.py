# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Jun 09 22:01:44 2012
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
        MainWindow.resize(584, 411)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidgetRss = QtGui.QListWidget(self.centralwidget)
        self.listWidgetRss.setMouseTracking(True)
        self.listWidgetRss.setAlternatingRowColors(True)
        self.listWidgetRss.setObjectName(_fromUtf8("listWidgetRss"))
        self.gridLayout.addWidget(self.listWidgetRss, 2, 0, 1, 1)
        self.pushRefreshButton = QtGui.QPushButton(self.centralwidget)
        self.pushRefreshButton.setObjectName(_fromUtf8("pushRefreshButton"))
        self.gridLayout.addWidget(self.pushRefreshButton, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionFilters = QtGui.QAction(MainWindow)
        self.actionFilters.setObjectName(_fromUtf8("actionFilters"))
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addAction(self.actionFilters)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FeedPy", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Mouse over any entries in the main list to see a quick summary, or click the item to launch a browser.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRefreshButton.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilters.setText(QtGui.QApplication.translate("MainWindow", "Filters", None, QtGui.QApplication.UnicodeUTF8))

