# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created: Wed Jun 06 21:16:28 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 462)
        Dialog.setSizeGripEnabled(True)
        self.treeView = QtGui.QTreeView(Dialog)
        self.treeView.setGeometry(QtCore.QRect(40, 60, 551, 361))
        self.treeView.setAutoFillBackground(True)
        self.treeView.setObjectName("treeView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

