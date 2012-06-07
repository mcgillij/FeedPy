# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Jun 06 20:18:15 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuHi_what_can_I_do_for_you_today = QtGui.QMenu(self.menubar)
        self.menuHi_what_can_I_do_for_you_today.setObjectName("menuHi_what_can_I_do_for_you_today")
        self.menuHi = QtGui.QMenu(self.menubar)
        self.menuHi.setObjectName("menuHi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDsgsdgfs = QtGui.QAction(MainWindow)
        self.actionDsgsdgfs.setObjectName("actionDsgsdgfs")
        self.menuHi_what_can_I_do_for_you_today.addSeparator()
        self.menuHi_what_can_I_do_for_you_today.addSeparator()
        self.menuHi_what_can_I_do_for_you_today.addAction(self.actionDsgsdgfs)
        self.menubar.addAction(self.menuHi_what_can_I_do_for_you_today.menuAction())
        self.menubar.addAction(self.menuHi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHi_what_can_I_do_for_you_today.setTitle(QtGui.QApplication.translate("MainWindow", "Hi what can I do for you today", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHi.setTitle(QtGui.QApplication.translate("MainWindow", "Hi", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDsgsdgfs.setText(QtGui.QApplication.translate("MainWindow", "dsgsdgfs", None, QtGui.QApplication.UnicodeUTF8))

